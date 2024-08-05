# Problem statement

Build a chatbot that can understand context from a collection of speech data.
- Open-source/proprietary models can be used. 
- The language model should be an instruction fine-tuned model. 
- The speech data should be embedded into a vector database for retrieval.


## Model and Dataset Used to Solve the Problem

### Data Collection
We utilize Huggingface's open data sources i.e ``` openslr/librispeech_asr``` for speed and convenience. Due to the large size of the data, it has been downloaded and included in this repository.

### Model Selection
1. **Language Model**: Gemma2-it - Because it is small to test on my system
2. **Speech Model**: Whisper - it open source and good model for text to speech

### Vector Database
We use ChromaDB to store the embeddings of speech data.

### Embedding Model
We use the SentenceTransformer model to obtain embeddings as it is open-source.

## Steps Involved in Code Flow

### 1. During System Startup
- Download the dataset : i am using dataset from local because it was taking to long to download using ```load_dataset``` method that's why i downloaded a single parquet file for testing purpose .
- Initialize the Whisper model : load the model and processor .
- Extract text from speech using Whisper : get_text method will extract text from speech .
- Initialize the embedding model (SentenceTransformers).
- Calculate the embedding of the text obtained from the speech.
- Store the embedding in the vector database.
- Repeat steps a-f for the entire dataset.
### 2. During Inference
- Get user query.
-  Calculate the embedding of the query.
-  Fetch the top 2 or 5 documents from the vector database.
-  Apply a prompt template with the user query and context obtained from step c.
-  Tokenize the entire prompt.
-  Use the `model.generate` method to get the model's response.
-  Decode the model's tokens into text.
-  Return the response to the user.

## Code Structure

### 1. `speech.py`
Contains the Whisper model and methods to convert speech to text.

### 2. `vectordb.py`
Handles loading the vector database and storing all the datasets.

### 3. `models.py`
Loads the language model and tokenizer and contains the `model.generate` method to get the model's response.

### 4. `app.py`
The main application file where user queries are taken, and responses are returned from the model.

### 5. `dataset`
This directory contains a sample of the downloaded dataset from Huggingface for faster loading.

## Install the Requirements

Make sure to install all required packages before running the application:

```bash
pip install -r requirements.txt
```

## How to Run This App

```bash
python3 app.py
```
