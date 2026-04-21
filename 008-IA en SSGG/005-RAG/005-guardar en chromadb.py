import requests
import chromadb

OLLAMA_URL = "http://localhost:11434/api/embed"
MODEL = "nomic-embed-text:v1.5"

def get_embedding(text):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "input": text
        },
        timeout=60
    )
    response.raise_for_status()
    data = response.json()

    # /api/embed devuelve "embeddings"
    # Si enviamos un único texto, cogemos el primero
    return data["embeddings"][0]

# Palabras a guardar
words = ["gato", "perro", "camion"]

# Obtener embeddings con Ollama
embeddings = [get_embedding(word) for word in words]

# Crear cliente persistente de ChromaDB
client = chromadb.PersistentClient(path="./mi_chromadb")

# Crear o recuperar colección
collection = client.get_or_create_collection(name="palabras")

# Guardar en Chroma
collection.add(
    ids=["1", "2", "3"],
    documents=words,
    embeddings=embeddings,
    metadatas=[
        {"tipo": "animal"},
        {"tipo": "animal"},
        {"tipo": "vehiculo"}
    ]
)

print("Palabras guardadas correctamente en ChromaDB.")