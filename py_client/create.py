import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "this is new entry"
}
get_response = requests.post(endpoint, json=data) #HTTP Request

print(get_response.json())