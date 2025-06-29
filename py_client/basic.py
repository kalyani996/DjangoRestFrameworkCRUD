import requests

endpoint = "http://localhost:8000/api/"

#get_response = requests.get(endpoint, json={"query":'hellow'}) #HTTP Request
#application programming intrface
get_response = requests.post(endpoint, json={"title":'Hellow World'}) #HTTP Request
#application programming intrface
# Rest api http request -> JSON
# http reuquest -> HTML
print(get_response.json())