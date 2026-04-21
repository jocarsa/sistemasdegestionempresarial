import requests
import chromadb

OLLAMA_URL = "http://localhost:11434/api/embed"
MODEL = "nomic-embed-text:v1.5"
CHROMA_PATH = "./mi_chromadb"
COLLECTION_NAME = "palabras"

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
    return data["embeddings"][0]

# 1. Abrir la base persistente
client = chromadb.PersistentClient(path=CHROMA_PATH)

# 2. Recuperar la colección
collection = client.get_collection(name=COLLECTION_NAME)

# 3. Texto a buscar
query_text = "felino"

# 4. Embedding de la consulta
query_embedding = get_embedding(query_text)

# 5. Buscar similitud en Chroma
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

# 6. Mostrar resultados
print("Consulta:", query_text)
print()

ids = results.get("ids", [[]])[0]
documents = results.get("documents", [[]])[0]
metadatas = results.get("metadatas", [[]])[0]
distances = results.get("distances", [[]])[0]

for i, (doc_id, doc, meta, dist) in enumerate(zip(ids, documents, metadatas, distances), start=1):
    print(f"Resultado {i}")
    print(f"  ID: {doc_id}")
    print(f"  Documento: {doc}")
    print(f"  Metadata: {meta}")
    print(f"  Distancia: {dist}")
    print()