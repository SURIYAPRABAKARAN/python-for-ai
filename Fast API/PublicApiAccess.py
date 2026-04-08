import requests
import json


# get request
response = requests.get("https://api.restful-api.dev/objects/ff8081819d62221a019d6e15829112f1")

print(f"from get : {response.json()}")

# post (save)
url = "https://api.restful-api.dev/objects"

payload = {
  "name": "Apple MacBook Pro 16",
  "data": {
    "year": 2019,
    "price": 1849.99,
    "CPU model": "Intel Core i9",
    "Hard disk size": "1 TB"
  }
}

header = {
    "Content-Type" : "application/json"
}

response = requests.post(url, headers=header, data=json.dumps(payload))

if response.status_code == 200 or response.status_code == 201:
    print(f"successful : {response.json()}")
else:
    print(f"failed : {response.status_code}")
    print(f"failed msg : {response.text}")
    
    
    