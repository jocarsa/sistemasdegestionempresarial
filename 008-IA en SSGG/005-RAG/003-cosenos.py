import requests
import math

OLLAMA_URL = "http://localhost:11434/api/embeddings"
MODEL = "nomic-embed-text:v1.5"

def get_embedding(text):
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL,
        "prompt": text
    })
    return response.json()["embedding"]

def cosine_similarity(vec1, vec2):
    dot = sum(a * b for a, b in zip(vec1, vec2))
    norm1 = math.sqrt(sum(a * a for a in vec1))
    norm2 = math.sqrt(sum(b * b for b in vec2))
    return dot / (norm1 * norm2)

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
    sim = cosine_similarity(embeddings[a], embeddings[b])
    print(f"Similitud coseno entre '{a}' y '{b}': {sim:.4f}")