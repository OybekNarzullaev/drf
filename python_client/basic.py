import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint, params={"abs": 123}, json={"query": "Hello world"})

print(f"status: {get_response.status_code}\ndata: {get_response.json()}")