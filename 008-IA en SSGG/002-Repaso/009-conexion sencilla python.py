import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "phi4-mini:latest",
    "prompt": "Hola, ¿qué tal?",
    "stream": False
}

response = requests.post(url, json=data)

print(response.json()["response"])