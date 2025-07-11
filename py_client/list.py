import requests
from getpass import getpass
auth_endpoint = "http://localhost:8000/api/auth/"
username = input("Whatis your username?\n ")
password = getpass("what is your password?\n")

auth_response = requests.post(auth_endpoint, json={'username': username,'password':password}) #HTTP Request

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    print(token)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers) #HTTP Request

    print(get_response.json())