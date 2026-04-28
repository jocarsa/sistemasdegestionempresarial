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

COLLECTION_PARAGRAPHS = "fp_legislacion_parrafos"
COLLECTION_ARTICLES = "fp_legislacion_articulos"
COLLECTION_BLOCKS = "fp_legislacion_bloques"

RECREATE_COLLECTIONS = True
BATCH_SIZE = 200

# Para bloques deslizantes de contexto
BLOCK_SIZE = 4
BLOCK_OVERLAP = 1

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


def slugify(texto: str) -> str:
    texto = texto.lower().strip()
    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "à": "a", "è": "e", "ì": "i", "ò": "o", "ù": "u",
        "ä": "a", "ë": "e", "ï": "i", "ö": "o", "ü": "u",
        "ñ": "n",
    }
    for k, v in reemplazos.items():
        texto = texto.replace(k, v)
    texto = re.sub(r"[^a-z0-9]+", "_", texto)
    texto = re.sub(r"_+", "_", texto).strip("_")
    return texto or "desconocido"


# =========================
# DETECCIÓN LEGAL
# =========================
def detectar_titulo(parrafo: str) -> bool:
    p = parrafo.strip()

    if len(p) <= 180 and p.isupper():
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
    if re.match(r"^SECCI[ÓO]N\b", p, re.IGNORECASE):
        return "seccion"
    if detectar_titulo(p):
        return "titulo"
    return "parrafo"


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


def extraer_numero_articulo(texto: str) -> str:
    m = re.search(r"Art[íi]culo\s+(\d+)", texto, re.IGNORECASE)
    return m.group(1) if m else ""


def extraer_numero_anexo(texto: str) -> str:
    m = re.search(r"ANEXO\s+([IVXLC0-9]+)", texto, re.IGNORECASE)
    return m.group(1) if m else ""


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
    encontrados = re.findall(r"Real Decreto\s+\d+/\d{4}", texto_completo, flags=re.IGNORECASE)
    unicos = []

    for e in encontrados:
        limpio = re.sub(r"\s+", " ", e.strip())
        if limpio.lower() not in [x.lower() for x in unicos]:
            unicos.append(limpio)

    return " | ".join(unicos[:20]) if unicos else ""


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


def resumir_texto(texto: str, max_chars: int = 300) -> str:
    texto = texto.strip()
    if len(texto) <= max_chars:
        return texto
    return texto[:max_chars].rstrip() + "..."


def contar_palabras(texto: str) -> int:
    return len(texto.strip().split())


# =========================
# DETECCIÓN DE TEMAS LEGALES
# =========================
def inferir_temas(texto: str) -> str:
    t = texto.lower()
    temas = []

    mapa = {
        "duracion": ["duración", "duracion", "2000 horas"],
        "identificacion": ["identificación", "identificacion"],
        "perfil_profesional": ["perfil profesional"],
        "competencia_general": ["competencia general"],
        "competencias_profesionales": ["competencias profesionales"],
        "cualificaciones": ["cualificaciones", "unidades de competencia"],
        "entorno_profesional": ["entorno profesional"],
        "prospectiva": ["prospectiva"],
        "objetivos_generales": ["objetivos generales"],
        "modulos_profesionales": ["módulos profesionales", "modulos profesionales"],
        "espacios_equipamientos": ["espacios y equipamientos", "espacios necesarios", "equipamientos"],
        "profesorado": ["profesorado", "especialidades del profesorado"],
        "convalidaciones": ["convalidaciones", "exenciones", "equivalencias"],
        "accesos": ["acceso a otros estudios", "accesos a otros estudios"],
        "ects": ["ects", "créditos europeos", "creditos europeos"],
        "fct": ["formación en centros de trabajo", "formacion en centros de trabajo"],
    }

    for tema, patrones in mapa.items():
        for patron in patrones:
            if patron in t:
                temas.append(tema)
                break

    return "|".join(temas)


# =========================
# AGRUPACIÓN EN ARTÍCULOS
# =========================
def construir_articulos_desde_parrafos(parrafos: list[str], archivo: str) -> list[dict]:
    """
    Agrupa el documento por artículos / anexos / disposiciones / capítulos mayores.
    """
    articulos = []

    capitulo_actual = "sin_capitulo"
    anexo_actual = "sin_anexo"

    bloque_actual = []
    bloque_tipo = "preliminar"
    bloque_titulo = "preliminar"
    bloque_inicio = 0

    def cerrar_bloque(fin_index: int):
        nonlocal bloque_actual, bloque_tipo, bloque_titulo, bloque_inicio, capitulo_actual, anexo_actual

        if not bloque_actual:
            return

        texto = "\n\n".join(bloque_actual).strip()
        articulos.append({
            "titulo_bloque": bloque_titulo,
            "tipo_bloque": bloque_tipo,
            "capitulo": capitulo_actual,
            "anexo": anexo_actual,
            "texto": texto,
            "inicio_parrafo": bloque_inicio,
            "fin_parrafo": fin_index
        })
        bloque_actual = []

    for idx, parrafo in enumerate(parrafos):
        capitulo_actual = extraer_capitulo_actual(parrafo, capitulo_actual)
        anexo_actual = extraer_anexo_actual(parrafo, anexo_actual)

        tipo = detectar_tipo_bloque(parrafo)
        p = parrafo.strip()

        es_inicio_de_bloque = tipo in ["articulo", "anexo", "disposicion"]

        if es_inicio_de_bloque:
            cerrar_bloque(idx - 1)
            bloque_actual = [p]
            bloque_tipo = tipo
            bloque_titulo = p
            bloque_inicio = idx
        else:
            if not bloque_actual:
                bloque_actual = [p]
                bloque_tipo = "preliminar"
                bloque_titulo = "preliminar"
                bloque_inicio = idx
            else:
                bloque_actual.append(p)

    cerrar_bloque(len(parrafos) - 1)

    return articulos


# =========================
# BLOQUES DESLIZANTES
# =========================
def construir_bloques_deslizantes(parrafos_con_meta: list[dict], block_size: int, overlap: int) -> list[dict]:
    bloques = []
    if block_size <= 0:
        return bloques

    step = max(1, block_size - overlap)

    for start in range(0, len(parrafos_con_meta), step):
        end = min(start + block_size, len(parrafos_con_meta))
        segmento = parrafos_con_meta[start:end]
        if not segmento:
            continue

        texto = "\n\n".join(item["texto"] for item in segmento).strip()

        bloques.append({
            "texto": texto,
            "inicio_parrafo_archivo": segmento[0]["indice_archivo"],
            "fin_parrafo_archivo": segmento[-1]["indice_archivo"],
            "capitulo": segmento[0]["capitulo"],
            "articulo": segmento[0]["articulo"],
            "anexo": segmento[0]["anexo"],
            "tipos": "|".join(sorted(set(item["tipo_bloque"] for item in segmento))),
            "num_parrafos": len(segmento),
            "num_palabras": contar_palabras(texto),
            "resumen": resumir_texto(texto, 350),
        })

        if end == len(parrafos_con_meta):
            break

    return bloques


# =========================
# INSERCIÓN EN CHROMA
# =========================
def insertar_en_lotes(collection, ids, documents, metadatas, batch_size=BATCH_SIZE):
    total = len(documents)
    for start in range(0, total, batch_size):
        end = min(start + batch_size, total)
        collection.add(
            ids=ids[start:end],
            documents=documents[start:end],
            metadatas=metadatas[start:end]
        )
        print(f"Insertados {start} → {end - 1} en {collection.name}")


# =========================
# MAIN
# =========================
def main():
    if not os.path.exists(TXT_FOLDER):
        print(f"ERROR: no existe la carpeta: {TXT_FOLDER}")
        return

    archivos = sorted([f for f in os.listdir(TXT_FOLDER) if f.lower().endswith(".txt")])

    if not archivos:
        print("ERROR: no se han encontrado archivos .txt en la carpeta")
        return

    print(f"Se han encontrado {len(archivos)} archivos TXT")

    client = chromadb.PersistentClient(path=DB_PATH)

    colecciones = [
        COLLECTION_PARAGRAPHS,
        COLLECTION_ARTICLES,
        COLLECTION_BLOCKS,
    ]

    if RECREATE_COLLECTIONS:
        for nombre in colecciones:
            try:
                client.delete_collection(nombre)
                print(f"Colección previa '{nombre}' eliminada")
            except Exception:
                pass

    collection_paragraphs = client.get_or_create_collection(name=COLLECTION_PARAGRAPHS)
    collection_articles = client.get_or_create_collection(name=COLLECTION_ARTICLES)
    collection_blocks = client.get_or_create_collection(name=COLLECTION_BLOCKS)

    # -------------------------
    # Acumuladores globales
    # -------------------------
    para_ids, para_docs, para_meta = [], [], []
    art_ids, art_docs, art_meta = [], [], []
    block_ids, block_docs, block_meta = [], [], []

    global_para_index = 0
    global_art_index = 0
    global_block_index = 0

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

        # =========================
        # 1. INDEXACIÓN DE PÁRRAFOS
        # =========================
        capitulo_actual = "sin_capitulo"
        articulo_actual = "sin_articulo"
        anexo_actual = "sin_anexo"

        parrafos_con_meta_archivo = []
        inicio_archivo_para = global_para_index

        for i, parrafo in enumerate(parrafos):
            capitulo_actual = extraer_capitulo_actual(parrafo, capitulo_actual)
            articulo_actual = extraer_articulo_actual(parrafo, articulo_actual)
            anexo_actual = extraer_anexo_actual(parrafo, anexo_actual)

            parrafo_id = f"parrafo_{global_para_index:08d}"
            tipo_bloque = detectar_tipo_bloque(parrafo)
            es_titulo = detectar_titulo(parrafo)
            num_palabras = contar_palabras(parrafo)
            temas = inferir_temas(parrafo)

            metadata = {
                "indice": global_para_index,
                "indice_archivo": i,
                "doc_type": "parrafo",
                "ciclo": ciclo,
                "titulo_oficial": titulo_oficial,
                "nivel": nivel,
                "familia_profesional": "informatica_y_comunicaciones",
                "tipo_norma": tipo_norma,
                "reales_decretos": reales_decretos,
                "capitulo": capitulo_actual,
                "articulo": articulo_actual,
                "articulo_num": extraer_numero_articulo(articulo_actual),
                "anexo": anexo_actual,
                "anexo_num": extraer_numero_anexo(anexo_actual),
                "tipo_bloque": tipo_bloque,
                "temas": temas,
                "num_palabras": num_palabras,
                "es_titulo": es_titulo,
                "source_file": archivo,
                "source_path": path,
                "source_slug": slugify(archivo),
                "prev_id": f"parrafo_{global_para_index - 1:08d}" if global_para_index > 0 else "",
                "next_id": "",
                "resumen_contexto": resumir_texto(parrafo, 300),
            }

            para_ids.append(parrafo_id)
            para_docs.append(parrafo)
            para_meta.append(metadata)

            parrafos_con_meta_archivo.append({
                "id": parrafo_id,
                "texto": parrafo,
                "indice_archivo": i,
                "capitulo": capitulo_actual,
                "articulo": articulo_actual,
                "anexo": anexo_actual,
                "tipo_bloque": tipo_bloque,
                "temas": temas,
                "num_palabras": num_palabras,
            })

            if global_para_index > 0:
                para_meta[-2]["next_id"] = parrafo_id

            global_para_index += 1

        fin_archivo_para = global_para_index - 1
        print(f"  → índices globales párrafos: {inicio_archivo_para} a {fin_archivo_para}")

        # =========================
        # 2. INDEXACIÓN DE ARTÍCULOS
        # =========================
        articulos = construir_articulos_desde_parrafos(parrafos, archivo)
        print(f"  → bloques legales/article-like: {len(articulos)}")

        for idx_art, art in enumerate(articulos):
            art_id = f"articulo_{global_art_index:08d}"
            texto_art = art["texto"]
            titulo_bloque = art["titulo_bloque"]
            tipo_bloque = art["tipo_bloque"]
            capitulo = art["capitulo"]
            anexo = art["anexo"]
            temas = inferir_temas(texto_art)

            metadata = {
                "indice": global_art_index,
                "indice_archivo": idx_art,
                "doc_type": "articulo",
                "ciclo": ciclo,
                "titulo_oficial": titulo_oficial,
                "nivel": nivel,
                "familia_profesional": "informatica_y_comunicaciones",
                "tipo_norma": tipo_norma,
                "reales_decretos": reales_decretos,
                "capitulo": capitulo,
                "articulo": titulo_bloque if tipo_bloque == "articulo" else "sin_articulo",
                "articulo_num": extraer_numero_articulo(titulo_bloque) if tipo_bloque == "articulo" else "",
                "anexo": anexo if anexo else ("sin_anexo" if tipo_bloque != "anexo" else titulo_bloque),
                "anexo_num": extraer_numero_anexo(titulo_bloque) if tipo_bloque == "anexo" else extraer_numero_anexo(anexo),
                "tipo_bloque": tipo_bloque,
                "titulo_bloque": titulo_bloque,
                "temas": temas,
                "num_palabras": contar_palabras(texto_art),
                "num_parrafos": art["fin_parrafo"] - art["inicio_parrafo"] + 1,
                "inicio_parrafo_archivo": art["inicio_parrafo"],
                "fin_parrafo_archivo": art["fin_parrafo"],
                "source_file": archivo,
                "source_path": path,
                "source_slug": slugify(archivo),
                "prev_id": f"articulo_{global_art_index - 1:08d}" if global_art_index > 0 else "",
                "next_id": "",
                "resumen_contexto": resumir_texto(texto_art, 400),
            }

            art_ids.append(art_id)
            art_docs.append(texto_art)
            art_meta.append(metadata)

            if global_art_index > 0:
                art_meta[-2]["next_id"] = art_id

            global_art_index += 1

        # =========================
        # 3. INDEXACIÓN DE BLOQUES DESLIZANTES
        # =========================
        bloques = construir_bloques_deslizantes(
            parrafos_con_meta_archivo,
            block_size=BLOCK_SIZE,
            overlap=BLOCK_OVERLAP
        )
        print(f"  → bloques deslizantes: {len(bloques)}")

        for idx_block, block in enumerate(bloques):
            block_id = f"bloque_{global_block_index:08d}"
            temas = inferir_temas(block["texto"])

            metadata = {
                "indice": global_block_index,
                "indice_archivo": idx_block,
                "doc_type": "bloque",
                "ciclo": ciclo,
                "titulo_oficial": titulo_oficial,
                "nivel": nivel,
                "familia_profesional": "informatica_y_comunicaciones",
                "tipo_norma": tipo_norma,
                "reales_decretos": reales_decretos,
                "capitulo": block["capitulo"],
                "articulo": block["articulo"],
                "articulo_num": extraer_numero_articulo(block["articulo"]),
                "anexo": block["anexo"],
                "anexo_num": extraer_numero_anexo(block["anexo"]),
                "tipo_bloque": block["tipos"],
                "temas": temas,
                "num_palabras": block["num_palabras"],
                "num_parrafos": block["num_parrafos"],
                "inicio_parrafo_archivo": block["inicio_parrafo_archivo"],
                "fin_parrafo_archivo": block["fin_parrafo_archivo"],
                "source_file": archivo,
                "source_path": path,
                "source_slug": slugify(archivo),
                "prev_id": f"bloque_{global_block_index - 1:08d}" if global_block_index > 0 else "",
                "next_id": "",
                "resumen_contexto": block["resumen"],
            }

            block_ids.append(block_id)
            block_docs.append(block["texto"])
            block_meta.append(metadata)

            if global_block_index > 0:
                block_meta[-2]["next_id"] = block_id

            global_block_index += 1

    # =========================
    # INSERCIÓN FINAL
    # =========================
    print("\nInsertando párrafos...")
    insertar_en_lotes(collection_paragraphs, para_ids, para_docs, para_meta)

    print("\nInsertando artículos...")
    insertar_en_lotes(collection_articles, art_ids, art_docs, art_meta)

    print("\nInsertando bloques...")
    insertar_en_lotes(collection_blocks, block_ids, block_docs, block_meta)

    # =========================
    # RESUMEN
    # =========================
    print("\nIndexación completada.")
    print(f"Ruta DB: {DB_PATH}")
    print(f"Colección párrafos: {COLLECTION_PARAGRAPHS} ({len(para_docs)} documentos)")
    print(f"Colección artículos: {COLLECTION_ARTICLES} ({len(art_docs)} documentos)")
    print(f"Colección bloques: {COLLECTION_BLOCKS} ({len(block_docs)} documentos)")

    print("\nResumen de archivos indexados:")
    for archivo in archivos:
        ciclo = inferir_ciclo_desde_nombre_archivo(archivo)
        print(f"  - {archivo} -> {ciclo}")


if __name__ == "__main__":
    main()
