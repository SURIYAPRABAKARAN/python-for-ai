import requests
import os

url = "https://api.restful-api.devv/objects"

api_key = os.getenv("API_KEY")

print(f"api_key {api_key}")

def getResponse(url : str):
    # try:
    #      requests.get(url)
    # except requests.exceptions.Timeout:
    #     print("Request timed out!")
    try:
        response = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=3
        )
        # print(response.json())

    except requests.exceptions.Timeout:
        print("Request timed out!")
    except ValueError:
        print("Invalid JSON response")
    
    
res = getResponse(url)