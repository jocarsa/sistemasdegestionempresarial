import requests

OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text:v1.5"

def get_embedding(text):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": text
    })
    return response.json()["embedding"]

def l1_distance(vec1, vec2):
    return sum(abs(a - b) for a, b in zip(vec1, vec2))

# Textos
texts = ["gato", "perro", "camion"]

# Obtener embeddings
embeddings = {text: get_embedding(text) for text in texts}

# Comparaciones
pairs = [
    ("gato", "perro"),
    ("gato", "camion"),
    ("perro", "camion")
]

for a, b in pairs:
    dist = l1_distance(embeddings[a], embeddings[b])
    print(f"Distancia L1 entre '{a}' y '{b}': {dist:.4f}")