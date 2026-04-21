# pip3 install chromadb --break-system-packages

import os
import re
import chromadb

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
txt_path = "pdf/BOE-A-2010-8067.txt"
db_path = "chromadb_boe"
collection_name = "boe_parrafos"

# -----------------------------
# FUNCIONES
# -----------------------------
def contar_palabras(texto: str) -> int:
    return len(texto.split())

# -----------------------------
# LEER TXT
# -----------------------------
with open(txt_path, "r", encoding="utf-8") as f:
    contenido = f.read()

# -----------------------------
# SEPARAR EN PÁRRAFOS
# -----------------------------
parrafos = re.split(r"\n\s*\n", contenido)
parrafos = [p.strip() for p in parrafos if p.strip()]

print(f"Se han encontrado {len(parrafos)} párrafos")

# -----------------------------
# INICIALIZAR CHROMADB
# -----------------------------
client = chromadb.PersistentClient(path=db_path)

# Borrar colección previa si existe
try:
    client.delete_collection(collection_name)
    print(f"Colección anterior '{collection_name}' eliminada")
except Exception:
    pass

collection = client.get_or_create_collection(name=collection_name)

# -----------------------------
# PREPARAR DATOS
# -----------------------------
ids = []
documents = []
metadatas = []

for i, parrafo in enumerate(parrafos, start=1):
    ids.append(f"parrafo_{i}")
    documents.append(parrafo)
    metadatas.append({
        "fuente": os.path.basename(txt_path),
        "numero_parrafo": i,
        "num_palabras": contar_palabras(parrafo)
    })

# -----------------------------
# INSERTAR EN CHROMADB
# -----------------------------
collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print("Párrafos guardados en ChromaDB correctamente")