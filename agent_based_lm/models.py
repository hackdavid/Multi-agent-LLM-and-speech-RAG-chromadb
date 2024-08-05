from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
# loading all model during system startup
# so we can use these model in agents 
token = ''


class GenerationModel:
    '''
    this class will load the gemma2 model for generation task 
    '''
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it",token=token)
        self.model = AutoModelForCausalLM.from_pretrained(
            "google/gemma-2b-it",
            torch_dtype=torch.bfloat16,
            token= token if token else None
        )
    def generate(self,prompt):
        input_ids = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**input_ids,max_new_tokens=100,use_cache=True)
        return self.tokenizer.decode(outputs[0])
    

# this is bert model for classification using pipeline 
classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')

generator = GenerationModel()


class ModelFactory:
    _models = {
        'classification': classifier,
        'generation': generator
    }
    
    @classmethod
    def get(cls,task):
        if task in cls._models:
            return cls._models[task]
        else:
            raise RuntimeError('Invalid task to get models ')