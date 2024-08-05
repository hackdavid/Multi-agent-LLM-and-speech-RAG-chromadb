from models import ModelFactory

class Agent:
    def __init__(self, role):
        self.role = role
    
    def perform_task(self, context):
        raise NotImplementedError("This method should be overridden by subclasses")

class TicketClassifier(Agent):
    def __init__(self):
        super().__init__('Ticket Classifier')
        self.task = 'classification' # to get the model from models
        self.classifier = ModelFactory.get(self.task)
    
    def perform_task(self, context):
        # create class label for task 
        categories = ["Billing", "Technical Support", "Account Management", "General Inquiry"]
        classification = self.classifier(context['ticket_text'], candidate_labels=categories)
        context['category'] = classification['labels'][0]
        return f"Ticket classified as {context['category']}."

class ResponseGenerator(Agent):
    def __init__(self):
        super().__init__('Response Generator')
        self.generator = ModelFactory.get('generation')

    def perform_task(self, context):
        prompts = {
            "Billing": "Generate a response for a billing issue: ",
            "Technical Support": "Generate a response for a technical support issue: ",
            "Account Management": "Generate a response for an account management issue: ",
            "General Inquiry": "Generate a response for a general inquiry: "
        }
        prompt = prompts.get(context['category'], "Generate a response: ") + context['ticket_text']
        response = self.generator.generate(prompt)
        context['response'] = response
        return "Response generated."

class EscalationManager(Agent):
    def __init__(self):
        super().__init__('Escalation Manager')
    
    def perform_task(self, context):
        if context['category'] == "Technical Support" and "urgent" in context['ticket_text'].lower():
            context['escalation'] = True
            return "Ticket escalated to human agent."
        context['escalation'] = False
        return "No escalation needed."

class FeedbackAnalyzer(Agent):
    def __init__(self):
        super().__init__('Feedback Analyzer')
    
    def perform_task(self, context):
        if 'feedback' in context:
            positive_feedback = "Thank you for your positive feedback!"
            context['feedback_response'] = positive_feedback if "good" in context['feedback'].lower() else "We're sorry to hear that. We'll improve."
            return "Feedback analyzed and response generated."
        return "No feedback to analyze."
    
