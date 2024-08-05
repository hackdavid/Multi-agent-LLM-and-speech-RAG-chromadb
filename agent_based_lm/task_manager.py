from agents import (
    TicketClassifier,
    ResponseGenerator,
    EscalationManager,
    FeedbackAnalyzer
)

# Task Parsing and Execution
class TaskManager:
    def __init__(self):
        self.agents = {
            'Ticket Classifier': TicketClassifier(),
            'Response Generator': ResponseGenerator(),
            'Escalation Manager': EscalationManager(),
            'Feedback Analyzer': FeedbackAnalyzer()
        }
        self.context = {}
    
    def parse_task(self, task):
        return {
            'ticket_text': task
        }
    
    def execute_task(self, task):
        self.context = self.parse_task(task)
        for role, agent in self.agents.items():
            print(f"Executing task for {role}...")
            output = agent.perform_task(self.context)
            print(output)
        return self.context
