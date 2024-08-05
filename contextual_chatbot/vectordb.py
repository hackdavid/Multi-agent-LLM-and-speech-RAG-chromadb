import chromadb
from sentence_transformers import SentenceTransformer
from datasets import load_dataset
from typing import List
from speech import get_text
from tqdm import tqdm

# Connect to Weaviate instance
# Initialize ChromaDB
client = chromadb.Client()

# Create or get collection
collection_name = 'context_chatbot'
collection = client.create_collection(name=collection_name)


# Load sentence transformer model
embedder = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# load dataset
# Note : i am using test as split for now due to time and resource 
print('loading dataset of speech ')
'''
Right now i am loading dataset from local because it was taking too long 
to load dataset from huggingface and also dataset was too large
so for implemenation i downloaed a single parquet file to work

if you want you can load dataset from huggingface directly

'''
# dataset = load_dataset("openslr/librispeech_asr", split=f"test")
num_samples = 10 # for testing prupose,you can change this number if you want
dataset = load_dataset('parquet',data_files='dataset/test-00000-of-00001.parquet')
dataset = dataset['train'].select(range(num_samples))

print('sotring the dataset as vector in db')
# creating vectors of all the datasets 
# Prepare data for upsert

for i, record in tqdm(enumerate(dataset)):
    # get the audio
    audio = record['audio']
    text = get_text(audio=audio)
    embedding = embedder.encode(text).tolist()
    temp = {'ids': f'doc_{i}','embeddings': embedding,'metadatas': {'text': text}}
    collection.upsert(**temp)
print('vectordb is ready to use.......')

# method to fetch top 2 documents
def fetch_documents(query:str,k=2):
    try:
        embedding = embedder.encode(query)
        response = collection.query(query_embeddings=embedding.tolist(),n_results=k)
        print('***** getting response from vectordb ********** ')
        if type(response) == dict:
            response = [response]
        texts = []
        for item in response:
            texts.append(item['metadatas'][0][0]['text'])
        return '\n'.join(texts)
    except Exception as e:
        print(f'Error while fetching document : {e}')
        return []
