import requests

endpoint = "http://127.0.0.1:8000/api/products/1/update"

data = {"title": "This field is done update"}

get_response = requests.put(endpoint, json=data)

print(f"status: {get_response.status_code}\ndata: {get_response.json()}")