# pip3 install chromadb --break-system-packages

import chromadb

# -----------------------------
# CONFIGURACIÓN
# -----------------------------
db_path = "chromadb_boe"
collection_name = "boe_parrafos"
MIN_PALABRAS = 10
N_RESULTADOS = 1

# -----------------------------
# CONEXIÓN
# -----------------------------
client = chromadb.PersistentClient(path=db_path)
collection = client.get_collection(name=collection_name)

print("Buscador del mejor párrafo")
print(f"Filtro mínimo de palabras: {MIN_PALABRAS}")
print("Escribe 'salir' para terminar\n")

while True:
    consulta = input("Consulta: ").strip()

    if consulta.lower() == "salir":
        print("Hasta luego")
        break

    if not consulta:
        print("Consulta vacía\n")
        continue

    try:
        resultados = collection.query(
            query_texts=[consulta],
            n_results=N_RESULTADOS,
            where={"num_palabras": {"$gte": MIN_PALABRAS}}
        )

        ids = resultados.get("ids", [[]])[0]
        documentos = resultados.get("documents", [[]])[0]
        metadatas = resultados.get("metadatas", [[]])[0]
        distancias = resultados.get("distances", [[]])[0] if resultados.get("distances") else []

        if not ids:
            print("No se ha encontrado ningún resultado que cumpla el mínimo de palabras\n")
            continue

        print("\n==============================")
        print("MEJOR CANDIDATO")
        print("==============================")
        print(f"ID: {ids[0]}")
        print(f"Fuente: {metadatas[0].get('fuente', 'N/A')}")
        print(f"Párrafo: {metadatas[0].get('numero_parrafo', 'N/A')}")
        print(f"Número de palabras: {metadatas[0].get('num_palabras', 'N/A')}")
        if distancias:
            print(f"Distancia: {distancias[0]}")

        print("\nTexto completo:\n")
        print(documentos[0])
        print()

    except Exception as e:
        print("Error durante la búsqueda:", e)
        print()