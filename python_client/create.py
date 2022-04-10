import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {"title": "This field is done"}

get_response = requests.post(endpoint, json=data)

print(f"status: {get_response.status_code}\ndata: {get_response.json()}")