import requests
import json

data=requests.get("https://jsonplaceholder.typicode.com/comments")

data=data.json()
print(json.dumps(data,indent=4))
with open("api.txt", "w") as file:
    json.dump(data, file, indent=4)