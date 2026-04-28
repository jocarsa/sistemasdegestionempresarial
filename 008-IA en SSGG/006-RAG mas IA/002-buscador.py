#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import chromadb

# =========================
# CONFIGURACIÓN
# =========================
DB_PATH = "chromadb_ubuntu_server"
COLLECTION_NAME = "ubuntu_server_parrafos"

# Número de resultados a pedir
N_RESULTADOS = 5

# Ignorar resultados demasiado cortos
MIN_PALABRAS = 10

# Mostrar contexto anterior y posterior
MOSTRAR_CONTEXTO = True

# =========================
# FUNCIONES
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
# PROGRAMA PRINCIPAL
# =========================
def main():
    client = chromadb.PersistentClient(path=DB_PATH)
    collection = client.get_collection(name=COLLECTION_NAME)

    print("Consulta de libro en ChromaDB")
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

        for i, (doc_id, doc, meta, distancia) in enumerate(zip(ids, docs, metas, distancias), start=1):
            mostrar_resultado(collection, i, doc_id, doc, meta, distancia)


if __name__ == "__main__":
    main()