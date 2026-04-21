# pip3 install chromadb --break-system-packages

import chromadb

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
db_path = "chromadb_boe"
collection_name = "boe_parrafos"

# -----------------------------
# CONEXIÓN A CHROMADB
# -----------------------------
client = chromadb.PersistentClient(path=db_path)
collection = client.get_collection(name=collection_name)

# -----------------------------
# BUCLE DE BÚSQUEDA
# -----------------------------
print("Buscador sobre ChromaDB")
print("Escribe una consulta y pulsa Enter")
print("Escribe 'salir' para terminar\n")

while True:
    consulta = input("Buscar: ").strip()

    if consulta.lower() in ["salir", "exit", "quit"]:
        print("Hasta luego")
        break

    if not consulta:
        print("Introduce algún texto para buscar\n")
        continue

    resultados = collection.query(
        query_texts=[consulta],
        n_results=5
    )

    ids = resultados.get("ids", [[]])[0]
    documentos = resultados.get("documents", [[]])[0]
    metadatas = resultados.get("metadatas", [[]])[0]
    distancias = resultados.get("distances", [[]])[0]

    if not ids:
        print("No se han encontrado resultados\n")
        continue

    print("\nResultados encontrados:\n")

    for i in range(len(ids)):
        print(f"Resultado {i + 1}")
        print(f"ID: {ids[i]}")
        print(f"Párrafo: {metadatas[i].get('numero_parrafo', 'N/A')}")
        print(f"Distancia: {distancias[i]}")
        print(documentos[i][:500])
        print("-" * 80)

    print()