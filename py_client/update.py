import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "hello world",
    "price":233
}

get_response = requests.put(endpoint, json=data) #HTTP Request

print(get_response.json())