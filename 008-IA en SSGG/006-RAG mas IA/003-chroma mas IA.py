#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import urllib.request
import urllib.error
import chromadb

# =========================
# CONFIGURACIÓN CHROMADB
# =========================
DB_PATH = "chromadb_ubuntu_server"
COLLECTION_NAME = "ubuntu_server_parrafos"
N_RESULTADOS = 5
MIN_PALABRAS = 10
MOSTRAR_CONTEXTO = True

# =========================
# CONFIGURACIÓN OLLAMA
# =========================
USE_OLLAMA = True
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "llama3.1:8b"   # cámbialo por el que tengas instalado
OLLAMA_TIMEOUT = 120
OLLAMA_KEEP_ALIVE = "10m"

SYSTEM_PROMPT = """Eres un asistente que responde preguntas sobre un libro técnico.
Tu trabajo es responder de forma clara, humana y útil, basándote SOLO en el contexto recuperado.
No inventes información.
Si el contexto no es suficiente, dilo claramente.
Responde en español.
Si es posible, explica el contenido de manera didáctica y resumida.
"""

# =========================
# FUNCIONES CHROMADB
# =========================
def obtener_documento_por_id(collection, doc_id: str):
    res = collection.get(ids=[doc_id], include=["documents", "metadatas"])
    if not res["ids"]:
        return None
    return {
        "id": res["ids"][0],
        "document": res["documents"][0],
        "metadata": res["metadatas"][0]
    }


def mostrar_resultado(collection, idx: int, doc_id: str, doc: str, meta: dict, distancia=None):
    print("=" * 80)
    print(f"RESULTADO {idx}")
    print(f"ID: {doc_id}")
    print(f"Capítulo: {meta.get('capitulo')}")
    print(f"Índice: {meta.get('indice')}")
    print(f"Palabras: {meta.get('num_palabras')}")
    print(f"Es título: {meta.get('es_titulo')}")
    if distancia is not None:
        print(f"Distancia: {distancia}")
    print("-" * 80)
    print(doc)
    print()

    if MOSTRAR_CONTEXTO:
        prev_id = meta.get("prev_id", "")
        next_id = meta.get("next_id", "")

        if prev_id:
            prev_doc = obtener_documento_por_id(collection, prev_id)
            if prev_doc:
                print("---- PÁRRAFO ANTERIOR ----")
                print(prev_doc["document"])
                print()

        if next_id:
            next_doc = obtener_documento_por_id(collection, next_id)
            if next_doc:
                print("---- PÁRRAFO SIGUIENTE ----")
                print(next_doc["document"])
                print()


def filtrar_resultados(resultados, min_palabras: int):
    docs_filtrados = []
    metas_filtradas = []
    ids_filtrados = []
    distancias_filtradas = []

    ids = resultados.get("ids", [[]])[0]
    docs = resultados.get("documents", [[]])[0]
    metas = resultados.get("metadatas", [[]])[0]
    distancias = resultados.get("distances", [[]])[0] if "distances" in resultados else [None] * len(docs)

    for doc_id, doc, meta, distancia in zip(ids, docs, metas, distancias):
        if not doc or not meta:
            continue
        if meta.get("num_palabras", 0) < min_palabras:
            continue

        ids_filtrados.append(doc_id)
        docs_filtrados.append(doc)
        metas_filtradas.append(meta)
        distancias_filtradas.append(distancia)

    return ids_filtrados, docs_filtrados, metas_filtradas, distancias_filtradas


# =========================
# FUNCIONES OLLAMA
# =========================
def construir_contexto(collection, ids, docs, metas, incluir_contexto=True):
    bloques = []

    for i, (doc_id, doc, meta) in enumerate(zip(ids, docs, metas), start=1):
        bloque = []
        bloque.append(f"[RESULTADO {i}]")
        bloque.append(f"ID: {doc_id}")
        bloque.append(f"Capítulo: {meta.get('capitulo')}")
        bloque.append(f"Índice: {meta.get('indice')}")
        bloque.append(f"Texto principal: {doc}")

        if incluir_contexto:
            prev_id = meta.get("prev_id", "")
            next_id = meta.get("next_id", "")

            if prev_id:
                prev_doc = obtener_documento_por_id(collection, prev_id)
                if prev_doc:
                    bloque.append(f"Párrafo anterior: {prev_doc['document']}")

            if next_id:
                next_doc = obtener_documento_por_id(collection, next_id)
                if next_doc:
                    bloque.append(f"Párrafo siguiente: {next_doc['document']}")

        bloques.append("\n".join(bloque))

    return "\n\n".join(bloques)


def preguntar_ollama(pregunta: str, contexto: str):
    prompt = f"""Contexto recuperado del libro:

{contexto}

Pregunta del usuario:
{pregunta}

Instrucciones:
- Responde de manera natural y clara.
- Resume y explica el contenido relevante.
- No inventes nada que no esté en el contexto.
- Si el contexto no basta, indícalo.
"""

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "system": SYSTEM_PROMPT,
        "stream": False,
        "keep_alive": OLLAMA_KEEP_ALIVE
    }

    data = json.dumps(payload).encode("utf-8")

    req = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=OLLAMA_TIMEOUT) as response:
            raw = response.read().decode("utf-8")
            parsed = json.loads(raw)
            return parsed.get("response", "").strip()

    except urllib.error.HTTPError as e:
        return f"[ERROR HTTP OLLAMA] {e.code} - {e.reason}"
    except urllib.error.URLError as e:
        return f"[ERROR CONEXIÓN OLLAMA] {e.reason}"
    except Exception as e:
        return f"[ERROR OLLAMA] {str(e)}"


# =========================
# PROGRAMA PRINCIPAL
# =========================
def main():
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_collection(name=COLLECTION_NAME)

    print("Consulta de libro en ChromaDB + Ollama")
    print("Escribe tu búsqueda y pulsa Enter. Vacío para salir.\n")

    while True:
        consulta = input("Consulta: ").strip()
        if not consulta:
            print("Saliendo.")
            break

        resultados = collection.query(
            query_texts=[consulta],
            n_results=N_RESULTADOS,
            include=["documents", "metadatas", "distances"]
        )

        ids, docs, metas, distancias = filtrar_resultados(resultados, MIN_PALABRAS)

        if not docs:
            print("\nNo se han encontrado resultados válidos.\n")
            continue

        print(f"\nSe han encontrado {len(docs)} resultados válidos.\n")

        # 1. Mostrar resultados en bruto
        for i, (doc_id, doc, meta, distancia) in enumerate(zip(ids, docs, metas, distancias), start=1):
            mostrar_resultado(collection, i, doc_id, doc, meta, distancia)

        # 2. Generar respuesta humanizada con Ollama
        if USE_OLLAMA:
            print("=" * 80)
            print("RESPUESTA REDACTADA POR OLLAMA")
            print("=" * 80)

            contexto = construir_contexto(
                collection=collection,
                ids=ids,
                docs=docs,
                metas=metas,
                incluir_contexto=MOSTRAR_CONTEXTO
            )

            respuesta = preguntar_ollama(consulta, contexto)
            print(respuesta)
            print()


if __name__ == "__main__":
    main()