import requests

endpoint = "http://127.0.0.1:8000/api/post/"

get_response = requests.post(endpoint, json={"title": "Hello world"})

print(f"status: {get_response.status_code}\ndata: {get_response.json()}")