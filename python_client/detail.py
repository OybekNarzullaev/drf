import requests

endpoint = "http://127.0.0.1:8000/api/products/1/"

get_response = requests.get(endpoint)

print(f"status: {get_response.status_code}\ndata: {get_response.json()}")