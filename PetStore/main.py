import requests


responseCreate = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 269,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "mermaid",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})

responceChange = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 269,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Lumina",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})


response = requests.get("https://petstore.swagger.io/v2/pet/269")

print(responseCreate.text)
print(responceChange.text)
print(response.text)
