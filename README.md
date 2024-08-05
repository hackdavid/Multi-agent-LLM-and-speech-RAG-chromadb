# Assessment Repository

## Introduction

This repository contains solutions to the assessment problems provided as part of a technical evaluation. The focus is on demonstrating problem-solving skills and coding capabilities. The repository includes two distinct problems along with their respective solutions. 

## Problem Statements and Solutions

### Problem 1: 
Build an agent-based language models system that can take in different roles to complete tasks.
- The input prompt should be a task that the system needs to complete.
- The system should create task-specific workers that should interact to get the task done. 
- The final output can be in text format. 


**Solution:**
### Customer Support Automation System
Design an automated customer support system that can handle support tickets. The system should:
1. Classify incoming support tickets into categories.
2. Generate responses to common customer queries.
3. Determine if a ticket should be escalated to a human agent.
4. Analyze customer feedback and generate responses accordingly.

The solution is implemented using an agent-based architecture combined with language models. Key components include:
- **Ticket Classifier**: Uses a zero-shot classification model to categorize tickets.
- **Response Generator**: Utilizes the Gemma2 model to generate responses based on ticket content.
- **Escalation Manager**: Decides on escalation based on ticket urgency.
- **Feedback Analyzer**: Processes feedback to generate appropriate responses.

For detailed implementation and code, please refer to the [Customer Support Automation System](https://github.com/hackdavid/Multi-agent-LLM-and-speech-RAG-chromadb/tree/master/agent_based_lm).

### Problem 2:
Build a chatbot that can understand context from a collection of speech data.
- Open-source/proprietary models can be used. 
- The language model should be an instruction fine-tuned model. 
- The speech data should be embedded into a vector database for retrieval.


### Solution : Steps Involved in Code Flow

1. **During System Startup**
   - Download dataset.
   - Initialize Whisper model.
   - Extract text from speech using Whisper.
   - Initialize SentenceTransformers embedding model.
   - For each text:
     - Calculate embedding of the text.
     - Store embedding in ChromaDB.
   - Repeat for all texts in dataset.

2. **During Inference**
   - Receive user query.
   - Calculate embedding of user query.
   - Fetch top 2 or 5 documents from ChromaDB.
   - Apply prompt template with user query and context.
   - Tokenize prompt.
   - Generate response using language model.
   - Decode model tokens to text.
   - Return response to user.

For detailed implementation and code, please refer to the [Event Planning Task Management System](https://github.com/hackdavid/Multi-agent-LLM-and-speech-RAG-chromadb/tree/master/contextual_chatbot).

## Repository Links

- [Customer Support Automation System](https://github.com/hackdavid/Multi-agent-LLM-and-speech-RAG-chromadb/tree/master/agent_based_lm)
- [Centextual Speech base chatbot](https://github.com/hackdavid/Multi-agent-LLM-and-speech-RAG-chromadb/tree/master/contextual_chatbot)

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
