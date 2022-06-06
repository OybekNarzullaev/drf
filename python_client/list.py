import requests
from getpass import getpass

# auth
auth_endpoint = "http://127.0.0.1:8000/api/auth/"
# username = input("Input username: ")
# password = getpass()
get_auth_response = requests.post(auth_endpoint, json={ 'username':'staff', 
                                                        'password':"Test.1234"
                                                        })
print(get_auth_response.json(), "ha")
# get products
if get_auth_response.status_code == 200:
    token = get_auth_response.json()['token']
    endpoint = "http://127.0.0.1:8000/api/products/"
    headers = {
        "Authorization": f"Bearer {token}"
    }

    get_response = requests.get(endpoint)
    data = get_response.json()
    next_url = data['next']
    results = data['results']
    print(next_url)
    print(f"status: {get_response.status_code}\ndata: {data}")