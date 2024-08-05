## Problem Statement 
Build an agent-based language models system that can take in different roles to complete tasks.
- The input prompt should be a task that the system needs to complete.
- The system should create task-specific workers that should interact to get the task done. 
- The final output can be in text format. 

# Solution 

### Customer Support Automation System

#### Overview

This Customer Support Automation System is designed to handle and streamline customer support tasks using an agent-based architecture combined with advanced language models. The system classifies incoming support tickets, generates responses, manages escalation, and analyzes feedback. The use of advanced language models ensures that the system can effectively understand and respond to a wide range of customer queries.


## Components

The system consists of several agents, each responsible for specific tasks:

1. **Ticket Classifier**: Classifies incoming tickets into predefined categories using zero-shot classification.
2. **Response Generator**: Generates responses to customer queries using the Gemma2 model.
3. **Escalation Manager**: Determines if a ticket needs to be escalated to a human agent based on its content.
4. **Feedback Analyzer**: Analyzes customer feedback and generates appropriate responses.

## Requirements

- Python 3.8 or higher
- `transformers` library for language models
- Pre-trained models from Hugging Face (e.g., Gemma2)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hackdavid/Multi-agent-LLM-and-speech-RAG-chromadb.git
   cd Multi-agent-LLM-and-speech-RAG-chromadb/agent_based_lm
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Define a support ticket**: Provide a string representing the ticket text.
   
   Example:
   ```python
   ticket_text = "I need help with my billing. The charges seem incorrect. It's urgent!"
   ```

2. **Define a support ticket**: Provide a string representing the ticket text.
   
   Direct Run :
   ```
   python3 main.py
   
   ```

3. **Initialize the Task Manager and Execute the Task**:
   ```python
   from task_manager import TaskManager

   # Initialize the task manager
   task_manager = TaskManager()

   # Execute the task
   final_context = task_manager.execute_task(ticket_text)

   # Display the final context
   print("\nFinal Context:")
   for key, value in final_context.items():
       print(f"{key}: {value}")
   ```

## How It Works

1. **Ticket Classification**: The `TicketClassifier` agent uses a zero-shot Bert classification model to categorize the ticket into one of the predefined categories (e.g., Billing, Technical Support, etc.).
   
2. **Response Generation**: The `ResponseGenerator` agent uses the Gemma2-it model to generate a response based on the ticket category and content.

3. **Escalation Management**: The `EscalationManager` agent assesses whether the ticket needs to be escalated to a human agent based on urgency and category.

4. **Feedback Analysis**: The `FeedbackAnalyzer` agent processes customer feedback if provided, generating appropriate responses based on the sentiment of the feedback.

## Code Structure

- `task_manager.py`: Contains the `TaskManager` class that coordinates the agents and executes tasks.
- `agents.py`: Defines the different agents (`TicketClassifier`, `ResponseGenerator`, `EscalationManager`, `FeedbackAnalyzer`) and their respective functionalities.
- `requirements.txt`: Lists the required Python packages.
- `models.py` : this will load the different different models required based on task . so later we can just use the model instead of loading everytime

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
