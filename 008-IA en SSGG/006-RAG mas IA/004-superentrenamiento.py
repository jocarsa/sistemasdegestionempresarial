#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import chromadb

# =========================
# CONFIGURACIÓN
# =========================
TXT_FOLDER = "txt"
DB_PATH = "chromadb_fp_legislacion"
COLLECTION_NAME = "fp_legislacion_parrafos"

RECREATE_COLLECTION = True
BATCH_SIZE = 200

# =========================
# FUNCIONES DE LIMPIEZA
# =========================
def limpiar_texto(texto: str) -> str:
    texto = texto.replace("\r\n", "\n").replace("\r", "\n")
    texto = re.sub(r"[ \t]+", " ", texto)
    texto = re.sub(r"\n[ \t]+", "\n", texto)
    return texto.strip()


def detectar_parrafos(texto: str) -> list[str]:
    bloques = re.split(r"\n\s*\n+", texto)
    parrafos = []

    for bloque in bloques:
        bloque = bloque.strip()
        if not bloque:
            continue

        bloque = re.sub(r"\n+", " ", bloque)
        bloque = re.sub(r"\s{2,}", " ", bloque).strip()

        if bloque:
            parrafos.append(bloque)

    return parrafos


# =========================
# FUNCIONES DE DETECCIÓN LEGAL
# =========================
def detectar_titulo(parrafo: str) -> bool:
    p = parrafo.strip()

    if len(p) <= 160 and p.isupper():
        return True

    if re.match(r"^(CAP[IÍ]TULO|ANEXO|DISPOSICI[ÓO]N|SECCI[ÓO]N)\b", p, re.IGNORECASE):
        return True

    if re.match(r"^Art[íi]culo\s+\d+", p, re.IGNORECASE):
        return True

    if re.match(r"^\d+(\.\d+)*\.?\s+", p):
        return True

    if len(p.split()) <= 10 and not p.endswith("."):
        return True

    return False


def extraer_capitulo_actual(parrafo: str, capitulo_actual: str) -> str:
    p = parrafo.strip()

    m = re.match(r"^(CAP[IÍ]TULO\s+[IVXLC0-9]+(?:\s*[-–—:]\s*.*)?)$", p, re.IGNORECASE)
    if m:
        return m.group(1)

    return capitulo_actual


def extraer_articulo_actual(parrafo: str, articulo_actual: str) -> str:
    p = parrafo.strip()

    m = re.match(r"^(Art[íi]culo\s+\d+[\.º]?\s*.*)$", p, re.IGNORECASE)
    if m:
        return m.group(1)

    return articulo_actual


def extraer_anexo_actual(parrafo: str, anexo_actual: str) -> str:
    p = parrafo.strip()

    m = re.match(r"^(ANEXO\s+[IVXLC0-9]+(?:\s*[-–—:]\s*.*)?)$", p, re.IGNORECASE)
    if m:
        return m.group(1)

    return anexo_actual


def detectar_tipo_bloque(parrafo: str) -> str:
    p = parrafo.strip()

    if re.match(r"^Art[íi]culo\s+\d+", p, re.IGNORECASE):
        return "articulo"
    if re.match(r"^CAP[IÍ]TULO\b", p, re.IGNORECASE):
        return "capitulo"
    if re.match(r"^ANEXO\b", p, re.IGNORECASE):
        return "anexo"
    if re.match(r"^DISPOSICI[ÓO]N\b", p, re.IGNORECASE):
        return "disposicion"
    if detectar_titulo(p):
        return "titulo"
    return "parrafo"


def inferir_ciclo_desde_nombre_archivo(nombre_archivo: str) -> str:
    base = os.path.splitext(nombre_archivo)[0].strip().lower()

    equivalencias = {
        "asir": "asir",
        "dam": "dam",
        "daw": "daw",
        "smr": "smr",
    }

    if base in equivalencias:
        return equivalencias[base]

    if "administracion de sistemas informaticos en red" in base:
        return "asir"
    if "desarrollo de aplicaciones multiplataforma" in base:
        return "dam"
    if "desarrollo de aplicaciones web" in base:
        return "daw"
    if "sistemas microinformaticos y redes" in base:
        return "smr"

    return "desconocido"


def inferir_titulo_oficial(ciclo: str) -> str:
    titulos = {
        "asir": "Técnico Superior en Administración de Sistemas Informáticos en Red",
        "dam": "Técnico Superior en Desarrollo de Aplicaciones Multiplataforma",
        "daw": "Técnico Superior en Desarrollo de Aplicaciones Web",
        "smr": "Técnico en Sistemas Microinformáticos y Redes",
    }
    return titulos.get(ciclo, "desconocido")


def inferir_nivel(ciclo: str) -> str:
    niveles = {
        "asir": "grado_superior",
        "dam": "grado_superior",
        "daw": "grado_superior",
        "smr": "grado_medio",
    }
    return niveles.get(ciclo, "desconocido")


def detectar_tipo_norma(texto_completo: str) -> str:
    t = texto_completo.lower()

    if "real decreto" in t:
        return "real_decreto"
    if "ley orgánica" in t or "ley organica" in t:
        return "ley_organica"
    if "orden" in t:
        return "orden"
    return "desconocido"


def extraer_reales_decretos(texto_completo: str) -> str:
    encontrados = re.findall(
        r"Real Decreto\s+\d+/\d{4}",
        texto_completo,
        flags=re.IGNORECASE
    )
    unicos = []
    for e in encontrados:
        limpio = re.sub(r"\s+", " ", e.strip())
        if limpio.lower() not in [x.lower() for x in unicos]:
            unicos.append(limpio)
    return " | ".join(unicos[:10]) if unicos else ""


def resumir_texto_para_contexto(parrafo: str, max_chars: int = 1000) -> str:
    p = parrafo.strip()
    if len(p) <= max_chars:
        return p
    return p[:max_chars].rstrip() + "..."


# =========================
# PROGRAMA PRINCIPAL
# =========================
def main():
    if not os.path.exists(TXT_FOLDER):
        print(f"ERROR: no existe la carpeta: {TXT_FOLDER}")
        return

    archivos = sorted(
        [f for f in os.listdir(TXT_FOLDER) if f.lower().endswith(".txt")]
    )

    if not archivos:
        print("ERROR: no se han encontrado archivos .txt en la carpeta")
        return

    print(f"Se han encontrado {len(archivos)} archivos TXT")

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

    global_index = 0

    for archivo in archivos:
        path = os.path.join(TXT_FOLDER, archivo)

        print(f"\nProcesando: {archivo}")

        with open(path, "r", encoding="utf-8") as f:
            contenido = f.read()

        contenido = limpiar_texto(contenido)
        parrafos = detectar_parrafos(contenido)

        ciclo = inferir_ciclo_desde_nombre_archivo(archivo)
        titulo_oficial = inferir_titulo_oficial(ciclo)
        nivel = inferir_nivel(ciclo)
        tipo_norma = detectar_tipo_norma(contenido)
        reales_decretos = extraer_reales_decretos(contenido)

        print(f"  → {len(parrafos)} párrafos detectados")
        print(f"  → ciclo: {ciclo}")
        print(f"  → título: {titulo_oficial}")

        capitulo_actual = "sin_capitulo"
        articulo_actual = "sin_articulo"
        anexo_actual = "sin_anexo"

        inicio_archivo_index = global_index

        for i, parrafo in enumerate(parrafos):
            capitulo_actual = extraer_capitulo_actual(parrafo, capitulo_actual)
            articulo_actual = extraer_articulo_actual(parrafo, articulo_actual)
            anexo_actual = extraer_anexo_actual(parrafo, anexo_actual)

            parrafo_id = f"parrafo_{global_index:08d}"
            n_palabras = len(parrafo.split())
            es_titulo = detectar_titulo(parrafo)
            tipo_bloque = detectar_tipo_bloque(parrafo)

            metadata = {
                "indice": global_index,
                "indice_archivo": i,
                "ciclo": ciclo,
                "titulo_oficial": titulo_oficial,
                "nivel": nivel,
                "familia_profesional": "informatica_y_comunicaciones",
                "tipo_norma": tipo_norma,
                "reales_decretos": reales_decretos,
                "capitulo": capitulo_actual,
                "articulo": articulo_actual,
                "anexo": anexo_actual,
                "tipo_bloque": tipo_bloque,
                "num_palabras": n_palabras,
                "es_titulo": es_titulo,
                "source_file": archivo,
                "source_path": path,
                "prev_id": f"parrafo_{global_index-1:08d}" if global_index > 0 else "",
                "next_id": "",
                "resumen_contexto": resumir_texto_para_contexto(parrafo, 300)
            }

            ids.append(parrafo_id)
            documents.append(parrafo)
            metadatas.append(metadata)

            if global_index > 0:
                metadatas[-2]["next_id"] = parrafo_id

            global_index += 1

        fin_archivo_index = global_index - 1
        print(f"  → índices globales: {inicio_archivo_index} a {fin_archivo_index}")

    # =========================
    # INSERCIÓN EN BLOQUES
    # =========================
    total_docs = len(documents)

    for start in range(0, total_docs, BATCH_SIZE):
        end = min(start + BATCH_SIZE, total_docs)

        collection.add(
            ids=ids[start:end],
            documents=documents[start:end],
            metadatas=metadatas[start:end]
        )

        print(f"Insertados {start} → {end - 1}")

    print("\nBase de datos creada correctamente.")
    print(f"Total párrafos: {total_docs}")
    print(f"Ruta DB: {DB_PATH}")
    print(f"Colección: {COLLECTION_NAME}")

    print("\nResumen de archivos indexados:")
    for archivo in archivos:
        ciclo = inferir_ciclo_desde_nombre_archivo(archivo)
        print(f"  - {archivo} -> {ciclo}")


if __name__ == "__main__":
    main()