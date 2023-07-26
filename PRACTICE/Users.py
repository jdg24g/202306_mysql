import requests
import json
url =  "https://randomuser.me/api/?page=3&results=100"

#get the data
response = requests.get(url)
data = response.json()
print(json.dumps(data, indent=4))