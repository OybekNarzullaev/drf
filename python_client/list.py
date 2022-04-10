import requests

endpoint = "http://127.0.0.1:8000/api/products/"


get_response = requests.get(endpoint)

print(f"\nstatus: {get_response.status_code}\ndata: {get_response.json()}")