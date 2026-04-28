#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import chromadb
import requests
import traceback
import re

# =========================
# CONFIGURACIÓN
# =========================
CHROMA_DB_PATH = "chromadb_fp_legislacion"

COLLECTION_PARAGRAPHS = "fp_legislacion_parrafos"
COLLECTION_ARTICLES = "fp_legislacion_articulos"
COLLECTION_BLOCKS = "fp_legislacion_bloques"

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_MODEL = "llama3.1:8b"

SEARCH_K_ARTICLES = 8
SEARCH_K_BLOCKS = 8
SEARCH_K_PARAGRAPHS = 12

FINAL_TOP_RESULTS = 10
MAX_CONTEXT_CHARS = 18000
MIN_WORDS = 6

# =========================
# PROMPT DE SISTEMA
# =========================
SYSTEM_PROMPT = """
Eres un asistente especializado en legislación educativa española sobre Formación Profesional, centrado en ciclos formativos de la familia de Informática y Comunicaciones.

La base documental recuperada contiene normativa sobre:
- ASIR (Administración de Sistemas Informáticos en Red)
- DAM (Desarrollo de Aplicaciones Multiplataforma)
- DAW (Desarrollo de Aplicaciones Web)
- SMR (Sistemas Microinformáticos y Redes)

Tu tarea consiste en responder preguntas usando prioritariamente los fragmentos normativos recuperados.

REGLAS:
1. Basa tu respuesta en los fragmentos recuperados.
2. No inventes artículos, fechas, módulos, competencias ni disposiciones no presentes en el contexto.
3. Si la respuesta aparece de forma directa en el contexto, indícalo claramente.
4. Si la respuesta no aparece de forma literal pero puede deducirse razonablemente del contexto, puedes explicarlo, pero debes indicar expresamente que se trata de una inferencia.
5. Si el contexto es insuficiente, indícalo claramente.
6. Si puedes identificar el ciclo, artículo, capítulo, anexo o bloque normativo, menciónalo.
7. Si el usuario compara ciclos, organiza la respuesta por apartados.
8. Usa un tono formal, claro, neutro y prudente.

FORMATO:
- Primero: respuesta breve y directa.
- Después: justificación apoyada en el contexto.
- Después, si procede:
  - ciclo
  - artículo / capítulo / anexo
  - observaciones relevantes
- Si algo es inferido y no literal, dilo expresamente.
"""

# =========================
# APP
# =========================
app = Flask(__name__)
CORS(app)

# =========================
# CHROMADB
# =========================
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)

collection_paragraphs = client.get_or_create_collection(name=COLLECTION_PARAGRAPHS)
collection_articles = client.get_or_create_collection(name=COLLECTION_ARTICLES)
collection_blocks = client.get_or_create_collection(name=COLLECTION_BLOCKS)

# =========================
# FUNCIONES AUXILIARES
# =========================
def contar_palabras(texto: str) -> int:
    return len((texto or "").strip().split())


def normalizar(texto: str) -> str:
    if not texto:
        return ""
    texto = texto.lower().strip()

    reemplazos = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "à": "a", "è": "e", "ì": "i", "ò": "o", "ù": "u",
        "ä": "a", "ë": "e", "ï": "i", "ö": "o", "ü": "u",
        "ñ": "n",
    }

    for k, v in reemplazos.items():
        texto = texto.replace(k, v)

    texto = re.sub(r"\s+", " ", texto)
    return texto.strip()


def detectar_ciclo_en_pregunta(pregunta: str) -> str:
    p = normalizar(pregunta)

    if "asir" in p or "administracion de sistemas informaticos en red" in p:
        return "asir"
    if "dam" in p or "desarrollo de aplicaciones multiplataforma" in p:
        return "dam"
    if "daw" in p or "desarrollo de aplicaciones web" in p:
        return "daw"
    if "smr" in p or "sistemas microinformaticos y redes" in p:
        return "smr"

    return ""


def detectar_numero_articulo_en_pregunta(pregunta: str) -> str:
    p = normalizar(pregunta)
    m = re.search(r"articulo\s+(\d+)", p)
    return m.group(1) if m else ""


def extraer_keywords_legales(pregunta: str) -> list[str]:
    p = normalizar(pregunta)
    claves = []

    mapa = [
        "duracion",
        "2000 horas",
        "identificacion",
        "perfil profesional",
        "competencia general",
        "competencias profesionales",
        "objetivos generales",
        "modulos profesionales",
        "modulos",
        "entorno profesional",
        "cualificaciones",
        "unidades de competencia",
        "familia profesional",
        "nivel",
        "ects",
        "anexo",
        "capitulo",
        "articulo",
        "espacios",
        "equipamientos",
        "profesorado",
        "convalidaciones",
        "exenciones",
        "equivalencias",
        "accesos a otros estudios",
        "fct",
        "formacion en centros de trabajo",
        "empresa e iniciativa emprendedora",
        "formacion y orientacion laboral",
    ]

    for item in mapa:
        if item in p:
            claves.append(item)

    art = detectar_numero_articulo_en_pregunta(pregunta)
    if art:
        claves.append(f"articulo {art}")

    return claves


def expandir_consultas(pregunta: str) -> list[str]:
    queries = [pregunta.strip()]
    ciclo = detectar_ciclo_en_pregunta(pregunta)
    art = detectar_numero_articulo_en_pregunta(pregunta)
    keywords = extraer_keywords_legales(pregunta)

    ciclo_largo = {
        "asir": "Administración de Sistemas Informáticos en Red",
        "dam": "Desarrollo de Aplicaciones Multiplataforma",
        "daw": "Desarrollo de Aplicaciones Web",
        "smr": "Sistemas Microinformáticos y Redes",
    }.get(ciclo, "")

    if ciclo_largo:
        queries.append(f"{pregunta} {ciclo_largo}")

    if ciclo and keywords:
        queries.append(f"{ciclo} {' '.join(keywords)}")

    if ciclo_largo and keywords:
        queries.append(f"{ciclo_largo} {' '.join(keywords)}")

    if art:
        queries.append(f"artículo {art} {ciclo_largo or ciclo}".strip())

    # deduplicar conservando orden
    limpias = []
    vistas = set()
    for q in queries:
        q2 = q.strip()
        if q2 and q2 not in vistas:
            limpias.append(q2)
            vistas.add(q2)

    return limpias[:5]


def consultar_coleccion(collection, query_texts: list[str], n_results: int, source_name: str) -> list[dict]:
    resultados_agregados = []

    for q in query_texts:
        res = collection.query(
            query_texts=[q],
            n_results=n_results,
            include=["documents", "metadatas", "distances"]
        )

        docs = res.get("documents", [[]])[0]
        metas = res.get("metadatas", [[]])[0]
        dists = res.get("distances", [[]])[0]

        for doc, meta, dist in zip(docs, metas, dists):
            if not doc:
                continue
            if contar_palabras(doc) < MIN_WORDS:
                continue

            resultados_agregados.append({
                "document": doc,
                "metadata": meta if meta else {},
                "distance": float(dist) if dist is not None else 999.0,
                "source_collection": source_name,
                "matched_query": q,
            })

    return resultados_agregados


def deduplicar_resultados(resultados: list[dict]) -> list[dict]:
    mejores = {}

    for r in resultados:
        meta = r.get("metadata", {})
        clave = (
            r.get("source_collection", ""),
            meta.get("source_file", ""),
            meta.get("doc_type", ""),
            meta.get("indice", ""),
            normalizar(r.get("document", ""))[:500]
        )

        if clave not in mejores:
            mejores[clave] = r
        else:
            # conserva el de menor distancia inicial
            if r["distance"] < mejores[clave]["distance"]:
                mejores[clave] = r

    return list(mejores.values())


def puntuar_fragmento(fragmento: dict, pregunta: str) -> float:
    meta = fragmento.get("metadata", {})
    doc = normalizar(fragmento.get("document", ""))
    pregunta_norm = normalizar(pregunta)

    distance = float(fragmento.get("distance", 999.0))
    source_collection = fragmento.get("source_collection", "")
    doc_type = meta.get("doc_type", "")
    ciclo_pregunta = detectar_ciclo_en_pregunta(pregunta)
    art_pregunta = detectar_numero_articulo_en_pregunta(pregunta)
    keywords = extraer_keywords_legales(pregunta)

    score = 0.0

    # Base por similitud vectorial
    score += max(0.0, 15.0 - distance)

    # Prioridad por tipo de colección
    if source_collection == COLLECTION_ARTICLES:
        score += 4.5
    elif source_collection == COLLECTION_BLOCKS:
        score += 3.0
    elif source_collection == COLLECTION_PARAGRAPHS:
        score += 2.0

    # Prioridad por tipo documental
    if doc_type == "articulo":
        score += 3.0
    elif doc_type == "bloque":
        score += 2.0
    elif doc_type == "parrafo":
        score += 1.0

    # Coincidencia de ciclo
    if ciclo_pregunta and meta.get("ciclo", "") == ciclo_pregunta:
        score += 6.0

    # Coincidencia de artículo
    art_meta = str(meta.get("articulo_num", "")).strip()
    if art_pregunta and art_meta and art_meta == art_pregunta:
        score += 8.0

    # Coincidencia por palabras clave
    for kw in keywords:
        if kw in doc:
            score += 2.2

    # Coincidencia parcial con términos de la pregunta
    tokens_pregunta = [t for t in re.findall(r"[a-záéíóúñ0-9]+", pregunta_norm) if len(t) >= 4]
    coincidencias = 0
    for t in set(tokens_pregunta):
        if t in doc:
            coincidencias += 1
    score += min(coincidencias * 0.8, 6.0)

    # Bonus por temas detectados
    temas = normalizar(meta.get("temas", "").replace("|", " "))
    for kw in keywords:
        if kw in temas:
            score += 1.0

    # Bonus si el texto parece encabezado relevante
    tipo_bloque = meta.get("tipo_bloque", "")
    if art_pregunta and "articulo" in normalizar(tipo_bloque):
        score += 2.0

    # Penalizaciones
    if meta.get("num_palabras", 0) and int(meta.get("num_palabras", 0)) < 8:
        score -= 2.0

    if "sin_articulo" == normalizar(str(meta.get("articulo", ""))) and art_pregunta:
        score -= 1.5

    return score


def rerankear_resultados(resultados: list[dict], pregunta: str) -> list[dict]:
    for r in resultados:
        r["score"] = puntuar_fragmento(r, pregunta)

    resultados.sort(key=lambda x: x["score"], reverse=True)
    return resultados


def seleccionar_contexto_final(resultados: list[dict], max_items: int = FINAL_TOP_RESULTS, max_chars: int = MAX_CONTEXT_CHARS) -> list[dict]:
    seleccionados = []
    total_chars = 0

    for r in resultados:
        texto = r.get("document", "").strip()
        if not texto:
            continue

        if len(seleccionados) >= max_items:
            break

        if total_chars + len(texto) > max_chars:
            continue

        seleccionados.append(r)
        total_chars += len(texto)

    return seleccionados


def construir_prompt(pregunta: str, fragmentos: list[dict]) -> str:
    bloques = []

    for i, frag in enumerate(fragmentos, start=1):
        meta = frag.get("metadata", {})
        bloque = f"""[FRAGMENTO {i}]
Colección: {frag.get("source_collection", "")}
Score interno: {round(frag.get("score", 0.0), 3)}
Archivo: {meta.get("source_file", "desconocido")}
Tipo documento: {meta.get("doc_type", "")}
Ciclo: {meta.get("ciclo", "")}
Título oficial: {meta.get("titulo_oficial", "")}
Capítulo: {meta.get("capitulo", "")}
Artículo: {meta.get("articulo", "")}
Artículo num: {meta.get("articulo_num", "")}
Anexo: {meta.get("anexo", "")}
Temas: {meta.get("temas", "")}
Texto:
{frag.get("document", "").strip()}
"""
        bloques.append(bloque)

    contexto = "\n\n".join(bloques)

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO NORMATIVO RECUPERADO:
{contexto}

PREGUNTA DEL USUARIO:
{pregunta}

INSTRUCCIONES FINALES:
- Responde a partir del contexto recuperado.
- Si encuentras la respuesta de forma directa, dilo claramente.
- Si la respuesta no es literal pero se puede deducir razonablemente, puedes indicarlo, pero señala expresamente que es una inferencia.
- No inventes datos.
- Si el contexto es insuficiente, dilo con claridad.
- Si puedes, menciona el ciclo y el artículo, capítulo o anexo relevante.
- Si hay varias normas o ciclos en el contexto, separa claramente la información.

Redacta ahora la respuesta final.
"""
    return prompt.strip()


def consultar_ollama(prompt: str) -> str:
    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.25,
            "top_p": 0.9,
            "num_predict": 900
        }
    }

    response = requests.post(OLLAMA_URL, json=payload, timeout=240)
    response.raise_for_status()
    data = response.json()
    return data.get("response", "").strip()


def buscar_contexto_mejorado(pregunta: str) -> dict:
    query_texts = expandir_consultas(pregunta)

    resultados_art = consultar_coleccion(
        collection_articles,
        query_texts,
        SEARCH_K_ARTICLES,
        COLLECTION_ARTICLES
    )

    resultados_blocks = consultar_coleccion(
        collection_blocks,
        query_texts,
        SEARCH_K_BLOCKS,
        COLLECTION_BLOCKS
    )

    resultados_para = consultar_coleccion(
        collection_paragraphs,
        query_texts,
        SEARCH_K_PARAGRAPHS,
        COLLECTION_PARAGRAPHS
    )

    todos = resultados_art + resultados_blocks + resultados_para
    todos = deduplicar_resultados(todos)
    todos = rerankear_resultados(todos, pregunta)
    finales = seleccionar_contexto_final(todos)

    return {
        "query_texts": query_texts,
        "all_results": todos,
        "final_results": finales
    }

# =========================
# RUTAS
# =========================
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/preguntar", methods=["POST"])
def preguntar():
    try:
        data = request.get_json(silent=True)

        if not data or "pregunta" not in data:
            return jsonify({
                "ok": False,
                "error": "Debes enviar JSON con la clave 'pregunta'"
            }), 400

        pregunta = str(data["pregunta"]).strip()

        if not pregunta:
            return jsonify({
                "ok": False,
                "error": "La pregunta está vacía"
            }), 400

        busqueda = buscar_contexto_mejorado(pregunta)
        fragmentos_finales = busqueda["final_results"]

        if not fragmentos_finales:
            return jsonify({
                "ok": True,
                "pregunta": pregunta,
                "respuesta": "No he encontrado contexto normativo suficiente en la base documental.",
                "fragmentos": [],
                "queries_usadas": busqueda["query_texts"]
            })

        prompt = construir_prompt(pregunta, fragmentos_finales)
        respuesta_ia = consultar_ollama(prompt)

        return jsonify({
            "ok": True,
            "pregunta": pregunta,
            "respuesta": respuesta_ia,
            "queries_usadas": busqueda["query_texts"],
            "fragmentos": [
                {
                    "document": f["document"],
                    "metadata": f["metadata"],
                    "distance": f["distance"],
                    "score": f.get("score", 0.0),
                    "source_collection": f.get("source_collection", "")
                }
                for f in fragmentos_finales
            ]
        })

    except requests.exceptions.RequestException as e:
        return jsonify({
            "ok": False,
            "error": "Error al conectar con Ollama",
            "detalle": str(e)
        }), 500

    except Exception as e:
        return jsonify({
            "ok": False,
            "error": "Error interno del servidor",
            "detalle": str(e),
            "traceback": traceback.format_exc()
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
