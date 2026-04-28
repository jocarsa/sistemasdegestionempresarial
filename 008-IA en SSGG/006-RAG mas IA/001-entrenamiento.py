#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import uuid
import chromadb
from chromadb.config import Settings

# =========================
# CONFIGURACIÓN
# =========================
TXT_PATH = "Ubuntu Server.txt"
DB_PATH = "chromadb_ubuntu_server"
COLLECTION_NAME = "ubuntu_server_parrafos"

# Si quieres borrar y recrear la colección cada vez:
RECREATE_COLLECTION = True

# =========================
# FUNCIONES
# =========================
def limpiar_texto(texto: str) -> str:
    """Normaliza saltos de línea y espacios."""
    texto = texto.replace("\r\n", "\n").replace("\r", "\n")
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r"\n[ \t]+", "\n", texto)
    return texto.strip()


def detectar_parrafos(texto: str) -> list[str]:
    """
    Divide el texto en párrafos usando una o más líneas en blanco como separador.
    Elimina bloques vacíos y limpia espacios.
    """
    bloques = re.split(r"\n\s*\n+", texto)
    parrafos = []

    for bloque in bloques:
        bloque = bloque.strip()
        if not bloque:
            continue

        # Compacta líneas internas del mismo párrafo
        bloque = re.sub(r"\n+", " ", bloque)
        bloque = re.sub(r"\s{2,}", " ", bloque).strip()

        if bloque:
            parrafos.append(bloque)

    return parrafos


def detectar_titulo(parrafo: str) -> bool:
    """
    Heurística sencilla para marcar títulos/encabezados.
    """
    if len(parrafo) > 120:
        return False

    # Empieza por numeración tipo 2.1.4 o 10.7.5
    if re.match(r"^\d+(\.\d+)*\.?\s+", parrafo):
        return True

    # Líneas muy cortas sin punto final
    if len(parrafo.split()) <= 8 and not parrafo.endswith("."):
        return True

    return False


def extraer_capitulo_actual(parrafo: str, capitulo_actual: str) -> str:
    """
    Si el párrafo parece encabezado numerado, actualiza el capítulo actual.
    """
    m = re.match(r"^(\d+(?:\.\d+)*)\.?\s+(.*)", parrafo)
    if m:
        return m.group(1)
    return capitulo_actual


# =========================
# PROGRAMA PRINCIPAL
# =========================
def main():
    if not os.path.exists(TXT_PATH):
        print(f"ERROR: no existe el archivo: {TXT_PATH}")
        return

    with open(TXT_PATH, "r", encoding="utf-8") as f:
        contenido = f.read()

    contenido = limpiar_texto(contenido)
    parrafos = detectar_parrafos(contenido)

    print(f"Se han detectado {len(parrafos)} párrafos")

    client = chromadb.PersistentClient(path=DB_PATH)

    if RECREATE_COLLECTION:
        try:
            client.delete_collection(COLLECTION_NAME)
            print(f"Colección previa '{COLLECTION_NAME}' eliminada")
        except Exception:
            pass

    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    ids = []
    documents = []
    metadatas = []

    capitulo_actual = "sin_capitulo"

    for i, parrafo in enumerate(parrafos):
        capitulo_actual = extraer_capitulo_actual(parrafo, capitulo_actual)

        parrafo_id = f"parrafo_{i:06d}"
        n_palabras = len(parrafo.split())
        es_titulo = detectar_titulo(parrafo)

        metadata = {
            "indice": i,
            "capitulo": capitulo_actual,
            "num_palabras": n_palabras,
            "es_titulo": es_titulo,
            "prev_id": f"parrafo_{i-1:06d}" if i > 0 else "",
            "next_id": f"parrafo_{i+1:06d}" if i < len(parrafos) - 1 else "",
            "source_file": os.path.basename(TXT_PATH)
        }

        ids.append(parrafo_id)
        documents.append(parrafo)
        metadatas.append(metadata)

    # Inserción por bloques para evitar problemas con libros largos
    batch_size = 200

    for start in range(0, len(documents), batch_size):
        end = start + batch_size
        collection.add(
            ids=ids[start:end],
            documents=documents[start:end],
            metadatas=metadatas[start:end]
        )
        print(f"Insertados párrafos {start} a {min(end, len(documents)) - 1}")

    print("\nBase de datos creada correctamente.")
    print(f"Ruta DB: {DB_PATH}")
    print(f"Colección: {COLLECTION_NAME}")


if __name__ == "__main__":
    main()