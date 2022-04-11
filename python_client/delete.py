import requests

id = int(input("id -> "))

endpoint = f"http://127.0.0.1:8000/api/products/{id}"

get_response = requests.delete(endpoint)

print(get_response.status_code, get_response.status_code==204 and "Deleted")