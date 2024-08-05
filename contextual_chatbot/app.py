
from models import get_response
query = "Hello, how can I help you?"

response = get_response(query=query)
print(f'model response : {response}')
