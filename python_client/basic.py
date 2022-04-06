import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"abs": 123}, json={"query": "Hello world"})

print("Response status: ",get_response.status_code)
print("Response text format: ", get_response.text)
print("Response json format", get_response.json())