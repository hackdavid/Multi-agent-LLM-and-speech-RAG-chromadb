import torch
import torchaudio
from vectordb import (
    fetch_documents
)
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


print('loading model and tokenizer .....')

# i am going to use gemma2 and it require token access so please
# your own token from huggingface

token = ''

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it",token=token)
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2b-it",
    torch_dtype=torch.bfloat16,
    token=token if token else None
)

print('model is ready to use ........')

def prompt_template(query,context):
    inputs = f'''
    ### Instruction:
    You are a helpful and knowledgeable assistant designed to provide accurate and informative responses. Please follow the given context to provide relevant information or answer the query effectively. Ensure that your response is clear, concise, and directly addresses the query.

    ### Context:
    {context}

    ### Query:
    {query}

    ### Response:
    '''
    return inputs

def get_response(query):
    # get the context from vectordb 
    # i am taking only top 2 context right now , you can get any number if you want
    context = fetch_documents(query=query,k=2)
    # get the prompt template for this query
    prompt = prompt_template(query=query,context=context)
    # get token ids for this prompt
    input_ids = tokenizer(prompt,return_tensors='pt')
    # generate the token 
    output_tokens = model.generate(**input_ids,max_new_tokens=100)
    # decode the token to text
    response = tokenizer.decode(output_tokens[0], skip_special_tokens=True)
    return response


    