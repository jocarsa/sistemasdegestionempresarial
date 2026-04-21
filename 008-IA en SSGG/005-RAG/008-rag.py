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
except:
    pass

collection = client.get_or_create_collection(name=collection_name)

# -----------------------------
# INSERTAR EN BLOQUES
# -----------------------------
ids = []
documents = []
metadatas = []

for i, parrafo in enumerate(parrafos):
    ids.append(f"parrafo_{i+1}")
    documents.append(parrafo)
    metadatas.append({
        "fuente": os.path.basename(txt_path),
        "numero_parrafo": i + 1
    })

collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas
)

print("Párrafos guardados en ChromaDB correctamente")