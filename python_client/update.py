import requests

id = int(input("id -> "))
title = input("title -> ")

endpoint = f"http://127.0.0.1:8000/api/products/{id}/"

data = {"title": title}

get_response = requests.put(endpoint, json=data)

print(f"status: {get_response.status_code}\ndata: {get_response.json()}")