#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import uuid
import sqlite3
import requests
import subprocess
import tempfile

from pathlib import Path
from datetime import datetime
from flask import Flask, request, redirect, session, render_template, jsonify
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

import chromadb

from pypdf import PdfReader
from docx import Document
from odf.opendocument import load as odt_load
from odf.text import P


APP_NAME = "jocarsa | conocimiento"

DB_FILE = "admin.sqlite"
UPLOAD_FOLDER = "documentos"
CHROMA_FOLDER = "chroma_db"

EXTENSIONES_PERMITIDAS = {".txt", ".md", ".pdf", ".docx", ".doc", ".odt"}

OLLAMA_EMBED_URL = "http://127.0.0.1:11434/api/embed"
OLLAMA_EMBED_MODEL = "nomic-embed-text:v1.5"

OLLAMA_GENERATE_URL = "http://127.0.0.1:11434/api/generate"
OLLAMA_LLM_MODEL = "qwen2.5:3b-instruct"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CHROMA_FOLDER, exist_ok=True)

app = Flask(__name__)
app.secret_key = "cambia-esta-clave-en-produccion"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

chroma_client = chromadb.PersistentClient(path=CHROMA_FOLDER)


class OllamaEmbeddingFunction:
    def name(self):
        return "ollama-nomic-embed-text-v1-5"

    def _embed(self, textos):
        embeddings = []

        for texto in textos:
            response = requests.post(
                OLLAMA_EMBED_URL,
                json={
                    "model": OLLAMA_EMBED_MODEL,
                    "input": texto
                },
                timeout=120
            )

            response.raise_for_status()
            data = response.json()
            embeddings.append(data["embeddings"][0])

        return embeddings

    def __call__(self, input):
        return self._embed(input)

    def embed_documents(self, input):
        return self._embed(input)

    def embed_query(self, input):
        return self._embed([input])


embedding_function = OllamaEmbeddingFunction()


def conectar():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn


def ahora():
    return datetime.now().isoformat(timespec="seconds")


def extension_valida(nombre_archivo):
    return Path(nombre_archivo).suffix.lower() in EXTENSIONES_PERMITIDAS


def generar_respuesta_con_ollama(consulta, fragmentos):
    contexto = "\n\n".join(fragmentos)

    prompt = f"""
Responde en español, en un solo párrafo, con lenguaje natural, claro y directo.

Usa principalmente el contexto recuperado mediante RAG.
No inventes información que no esté en el contexto.
Si el contexto no contiene suficiente información, dilo claramente.

Pregunta del usuario:
{consulta}

Contexto recuperado:
{contexto}

Respuesta:
""".strip()

    response = requests.post(
        OLLAMA_GENERATE_URL,
        json={
            "model": OLLAMA_LLM_MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=180
    )

    response.raise_for_status()
    data = response.json()

    return data.get("response", "").strip()


def init_db():
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        creado_en TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS documentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        nombre_original TEXT NOT NULL,
        nombre_archivo TEXT NOT NULL,
        ruta TEXT NOT NULL,
        notas TEXT,
        estado TEXT NOT NULL DEFAULT 'SUBIDO',
        creado_en TEXT NOT NULL,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS entrenamientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER NOT NULL,
        nombre TEXT NOT NULL,
        estado TEXT NOT NULL,
        progreso INTEGER NOT NULL DEFAULT 0,
        documentos_total INTEGER NOT NULL DEFAULT 0,
        documentos_procesados INTEGER NOT NULL DEFAULT 0,
        chunks_total INTEGER NOT NULL DEFAULT 0,
        coleccion_chroma TEXT,
        creado_en TEXT NOT NULL,
        actualizado_en TEXT NOT NULL,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS indexaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        entrenamiento_id INTEGER NOT NULL,
        documento_id INTEGER NOT NULL,
        chunks INTEGER NOT NULL DEFAULT 0,
        estado TEXT NOT NULL,
        creado_en TEXT NOT NULL,
        FOREIGN KEY(entrenamiento_id) REFERENCES entrenamientos(id),
        FOREIGN KEY(documento_id) REFERENCES documentos(id)
    )
    """)

    total = cur.execute("SELECT COUNT(*) AS total FROM usuarios").fetchone()["total"]

    if total == 0:
        cur.execute("""
        INSERT INTO usuarios (email, password_hash, creado_en)
        VALUES (?, ?, ?)
        """, (
            "admin@admin.com",
            generate_password_hash("admin"),
            ahora()
        ))

    conn.commit()
    conn.close()


def usuario_actual():
    if "usuario_id" not in session:
        return None

    conn = conectar()
    usuario = conn.execute(
        "SELECT * FROM usuarios WHERE id = ?",
        (session["usuario_id"],)
    ).fetchone()
    conn.close()

    return usuario


def requiere_login():
    return usuario_actual() is not None


def leer_txt_md(ruta):
    with open(ruta, "r", encoding="utf-8", errors="ignore") as archivo:
        return archivo.read()


def leer_pdf(ruta):
    lector = PdfReader(ruta)
    parrafos = []

    for pagina in lector.pages:
        texto = pagina.extract_text() or ""

        for linea in texto.split("\n"):
            linea = linea.strip()

            if linea:
                parrafos.append(linea)

    return "\n\n".join(parrafos)


def leer_docx(ruta):
    documento = Document(ruta)
    parrafos = []

    for p in documento.paragraphs:
        texto = p.text.strip()

        if texto:
            parrafos.append(texto)

    return "\n\n".join(parrafos)


def leer_odt(ruta):
    documento = odt_load(ruta)
    parrafos = []

    for p in documento.getElementsByType(P):
        partes = []

        for nodo in p.childNodes:
            if hasattr(nodo, "data"):
                partes.append(nodo.data)

        texto = "".join(partes).strip()

        if texto:
            parrafos.append(texto)

    return "\n\n".join(parrafos)


def convertir_doc_con_libreoffice(ruta):
    carpeta_temporal = tempfile.mkdtemp()

    subprocess.run(
        [
            "libreoffice",
            "--headless",
            "--convert-to",
            "txt:Text",
            "--outdir",
            carpeta_temporal,
            ruta
        ],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    archivos_txt = [
        os.path.join(carpeta_temporal, nombre)
        for nombre in os.listdir(carpeta_temporal)
        if nombre.lower().endswith(".txt")
    ]

    if not archivos_txt:
        raise RuntimeError("LibreOffice no ha generado ningún archivo TXT.")

    with open(archivos_txt[0], "r", encoding="utf-8", errors="ignore") as archivo:
        return archivo.read()


def leer_texto(ruta):
    extension = Path(ruta).suffix.lower()

    if extension in [".txt", ".md"]:
        return leer_txt_md(ruta)

    if extension == ".pdf":
        return leer_pdf(ruta)

    if extension == ".docx":
        return leer_docx(ruta)

    if extension == ".odt":
        return leer_odt(ruta)

    if extension == ".doc":
        return convertir_doc_con_libreoffice(ruta)

    raise ValueError("Formato no soportado: " + extension)


def crear_chunks(texto, tamano=1200, solape=200):
    texto = texto.replace("\r", "\n")

    parrafos = []

    for bloque in texto.split("\n\n"):
        bloque = " ".join(bloque.split()).strip()

        if bloque:
            parrafos.append(bloque)

    chunks = []
    actual = ""

    for parrafo in parrafos:
        if len(actual) + len(parrafo) + 2 <= tamano:
            if actual:
                actual += "\n\n" + parrafo
            else:
                actual = parrafo
        else:
            if actual:
                chunks.append(actual.strip())

            if len(parrafo) > tamano:
                inicio = 0

                while inicio < len(parrafo):
                    fragmento = parrafo[inicio:inicio + tamano].strip()

                    if fragmento:
                        chunks.append(fragmento)

                    inicio += tamano - solape

                actual = ""
            else:
                actual = parrafo

    if actual:
        chunks.append(actual.strip())

    return chunks


@app.context_processor
def variables_globales():
    return {
        "app_name": APP_NAME,
        "usuario": usuario_actual()
    }


@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/api/embed", methods=["POST"])
def api_embed():
    data = request.get_json()
    texto = data.get("texto", "").strip()

    if not texto:
        return jsonify({
            "status": "error",
            "message": "No has enviado texto."
        })

    try:
        embedding = embedding_function.embed_query(texto)[0]

        return jsonify({
            "status": "ok",
            "embedding": embedding
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        })
        
@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json()
    consulta = data.get("consulta", "").strip()

    if not consulta:
        return jsonify({
            "respuesta": "No has enviado ninguna consulta."
        })

    conn = conectar()

    entrenamiento = conn.execute("""
    SELECT *
    FROM entrenamientos
    WHERE estado = 'COMPLETADO'
    ORDER BY id DESC
    LIMIT 1
    """).fetchone()

    conn.close()

    if not entrenamiento:
        return jsonify({
            "respuesta": "Todavía no hay ninguna indexación disponible."
        })

    try:
        collection = chroma_client.get_collection(
            name=entrenamiento["coleccion_chroma"],
            embedding_function=embedding_function
        )

        resultado = collection.query(
            query_texts=[consulta],
            n_results=5
        )

        documentos = resultado.get("documents", [[]])[0]

        if not documentos:
            return jsonify({
                "respuesta": "No he encontrado información relacionada en los documentos indexados."
            })

        respuesta = generar_respuesta_con_ollama(
            consulta=consulta,
            fragmentos=documentos
        )

        if not respuesta:
            respuesta = "He encontrado información relacionada, pero no he podido generar una respuesta redactada."

        return jsonify({
            "respuesta": respuesta
        })

    except Exception as e:
        return jsonify({
            "respuesta": "Error consultando el sistema RAG: " + str(e)
        })


@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        conn = conectar()
        usuario = conn.execute(
            "SELECT * FROM usuarios WHERE email = ?",
            (email,)
        ).fetchone()
        conn.close()

        if usuario and check_password_hash(usuario["password_hash"], password):
            session["usuario_id"] = usuario["id"]
            return redirect("/admin")

        error = "Credenciales incorrectas"

    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


@app.route("/admin")
def admin():
    if not requiere_login():
        return redirect("/login")

    usuario = usuario_actual()
    conn = conectar()

    documentos = conn.execute(
        "SELECT COUNT(*) AS total FROM documentos WHERE usuario_id = ?",
        (usuario["id"],)
    ).fetchone()["total"]

    entrenamientos = conn.execute(
        "SELECT COUNT(*) AS total FROM entrenamientos WHERE usuario_id = ?",
        (usuario["id"],)
    ).fetchone()["total"]

    ultimo = conn.execute("""
    SELECT *
    FROM entrenamientos
    WHERE usuario_id = ?
    ORDER BY id DESC
    LIMIT 1
    """, (usuario["id"],)).fetchone()

    conn.close()

    progreso = ultimo["progreso"] if ultimo else 0

    return render_template(
        "dashboard.html",
        activo="dashboard",
        documentos=documentos,
        entrenamientos=entrenamientos,
        progreso=progreso,
        ultimo=ultimo
    )


@app.route("/documentos", methods=["GET", "POST"])
def documentos():
    if not requiere_login():
        return redirect("/login")

    usuario = usuario_actual()

    if request.method == "POST":
        archivo = request.files.get("archivo")
        notas = request.form.get("notas", "")

        if archivo and archivo.filename:
            nombre_original = archivo.filename

            if not extension_valida(nombre_original):
                return redirect("/documentos")

            nombre_seguro = secure_filename(nombre_original)
            nombre_final = str(uuid.uuid4()) + "_" + nombre_seguro
            ruta = os.path.join(app.config["UPLOAD_FOLDER"], nombre_final)

            archivo.save(ruta)

            conn = conectar()
            conn.execute("""
            INSERT INTO documentos
            (usuario_id, nombre_original, nombre_archivo, ruta, notas, estado, creado_en)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                usuario["id"],
                nombre_original,
                nombre_final,
                ruta,
                notas,
                "SUBIDO",
                ahora()
            ))
            conn.commit()
            conn.close()

        return redirect("/documentos")

    conn = conectar()
    docs = conn.execute("""
    SELECT *
    FROM documentos
    WHERE usuario_id = ?
    ORDER BY id DESC
    """, (usuario["id"],)).fetchall()
    conn.close()

    return render_template(
        "documentos.html",
        activo="documentos",
        docs=docs
    )


@app.route("/entrenamientos")
def entrenamientos():
    if not requiere_login():
        return redirect("/login")

    usuario = usuario_actual()
    conn = conectar()

    filas = conn.execute("""
    SELECT *
    FROM entrenamientos
    WHERE usuario_id = ?
    ORDER BY id DESC
    """, (usuario["id"],)).fetchall()

    conn.close()

    return render_template(
        "entrenamientos.html",
        activo="entrenamientos",
        entrenamientos=filas
    )


@app.route("/entrenamientos/iniciar", methods=["POST"])
def iniciar_entrenamiento():
    if not requiere_login():
        return redirect("/login")

    usuario = usuario_actual()
    conn = conectar()

    documentos = conn.execute("""
    SELECT *
    FROM documentos
    WHERE usuario_id = ?
    ORDER BY id ASC
    """, (usuario["id"],)).fetchall()

    nombre = "Indexación " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    coleccion = "indexacion_" + str(uuid.uuid4()).replace("-", "_")

    cur = conn.cursor()
    cur.execute("""
    INSERT INTO entrenamientos
    (
        usuario_id,
        nombre,
        estado,
        progreso,
        documentos_total,
        documentos_procesados,
        chunks_total,
        coleccion_chroma,
        creado_en,
        actualizado_en
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        usuario["id"],
        nombre,
        "PROCESANDO",
        0,
        len(documentos),
        0,
        0,
        coleccion,
        ahora(),
        ahora()
    ))

    entrenamiento_id = cur.lastrowid

    conn.commit()
    conn.close()

    procesar_entrenamiento(entrenamiento_id)

    return redirect("/entrenamientos")


@app.route("/entrenamientos/continuar", methods=["POST"])
def continuar_entrenamiento():
    if not requiere_login():
        return redirect("/login")

    usuario = usuario_actual()
    conn = conectar()

    entrenamiento = conn.execute("""
    SELECT *
    FROM entrenamientos
    WHERE usuario_id = ?
    ORDER BY id DESC
    LIMIT 1
    """, (usuario["id"],)).fetchone()

    conn.close()

    if entrenamiento:
        procesar_entrenamiento(entrenamiento["id"])

    return redirect("/entrenamientos")


def procesar_entrenamiento(entrenamiento_id):
    conn = conectar()

    entrenamiento = conn.execute("""
    SELECT *
    FROM entrenamientos
    WHERE id = ?
    """, (entrenamiento_id,)).fetchone()

    if not entrenamiento:
        conn.close()
        return

    documentos = conn.execute("""
    SELECT *
    FROM documentos
    WHERE usuario_id = ?
    ORDER BY id ASC
    """, (entrenamiento["usuario_id"],)).fetchall()

    collection = chroma_client.get_or_create_collection(
        name=entrenamiento["coleccion_chroma"],
        embedding_function=embedding_function
    )

    total_docs = len(documentos)
    procesados = 0
    chunks_total = 0

    if total_docs == 0:
        conn.execute("""
        UPDATE entrenamientos
        SET estado = ?, progreso = ?, actualizado_en = ?
        WHERE id = ?
        """, (
            "SIN_DOCUMENTOS",
            100,
            ahora(),
            entrenamiento_id
        ))

        conn.commit()
        conn.close()
        return

    for doc in documentos:
        ya_indexado = conn.execute("""
        SELECT *
        FROM indexaciones
        WHERE entrenamiento_id = ?
        AND documento_id = ?
        """, (entrenamiento_id, doc["id"])).fetchone()

        if ya_indexado:
            procesados += 1
            chunks_total += ya_indexado["chunks"]
            continue

        try:
            texto = leer_texto(doc["ruta"])
            chunks = crear_chunks(texto)

            ids = []
            metadatas = []

            for i, chunk in enumerate(chunks):
                ids.append(f"ent_{entrenamiento_id}_doc_{doc['id']}_chunk_{i}")
                metadatas.append({
                    "entrenamiento_id": entrenamiento_id,
                    "documento_id": doc["id"],
                    "documento": doc["nombre_original"],
                    "chunk": i
                })

            if chunks:
                collection.add(
                    ids=ids,
                    documents=chunks,
                    metadatas=metadatas
                )

            conn.execute("""
            INSERT INTO indexaciones
            (entrenamiento_id, documento_id, chunks, estado, creado_en)
            VALUES (?, ?, ?, ?, ?)
            """, (
                entrenamiento_id,
                doc["id"],
                len(chunks),
                "COMPLETADA",
                ahora()
            ))

            conn.execute("""
            UPDATE documentos
            SET estado = ?
            WHERE id = ?
            """, (
                "INDEXADO",
                doc["id"]
            ))

            procesados += 1
            chunks_total += len(chunks)

            progreso = int((procesados / total_docs) * 100)

            conn.execute("""
            UPDATE entrenamientos
            SET progreso = ?,
                documentos_procesados = ?,
                chunks_total = ?,
                actualizado_en = ?
            WHERE id = ?
            """, (
                progreso,
                procesados,
                chunks_total,
                ahora(),
                entrenamiento_id
            ))

            conn.commit()

        except Exception as e:
            conn.execute("""
            INSERT INTO indexaciones
            (entrenamiento_id, documento_id, chunks, estado, creado_en)
            VALUES (?, ?, ?, ?, ?)
            """, (
                entrenamiento_id,
                doc["id"],
                0,
                "ERROR",
                ahora()
            ))

            conn.execute("""
            UPDATE documentos
            SET estado = ?
            WHERE id = ?
            """, (
                "ERROR",
                doc["id"]
            ))

            conn.commit()
            print("Error indexando documento:", doc["nombre_original"], e)

    conn.execute("""
    UPDATE entrenamientos
    SET estado = ?,
        progreso = ?,
        documentos_procesados = ?,
        chunks_total = ?,
        actualizado_en = ?
    WHERE id = ?
    """, (
        "COMPLETADO",
        100,
        procesados,
        chunks_total,
        ahora(),
        entrenamiento_id
    ))

    conn.commit()
    conn.close()


@app.route("/indexaciones")
def indexaciones():
    if not requiere_login():
        return redirect("/login")

    usuario = usuario_actual()
    conn = conectar()

    filas = conn.execute("""
    SELECT
        i.id,
        i.estado,
        i.chunks,
        i.creado_en,
        d.nombre_original,
        e.nombre AS entrenamiento,
        e.coleccion_chroma
    FROM indexaciones i
    JOIN documentos d ON d.id = i.documento_id
    JOIN entrenamientos e ON e.id = i.entrenamiento_id
    WHERE e.usuario_id = ?
    ORDER BY i.id DESC
    """, (usuario["id"],)).fetchall()

    conn.close()

    return render_template(
        "indexaciones.html",
        activo="indexaciones",
        filas=filas
    )


@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    if not requiere_login():
        return redirect("/login")

    usuario = usuario_actual()
    consulta = ""
    resultados = []
    error = ""

    if request.method == "POST":
        consulta = request.form.get("consulta", "").strip()

        conn = conectar()
        entrenamiento = conn.execute("""
        SELECT *
        FROM entrenamientos
        WHERE usuario_id = ?
        AND estado = 'COMPLETADO'
        ORDER BY id DESC
        LIMIT 1
        """, (usuario["id"],)).fetchone()
        conn.close()

        if not entrenamiento:
            error = "Todavía no hay ninguna indexación completada."
        elif consulta:
            try:
                collection = chroma_client.get_collection(
                    name=entrenamiento["coleccion_chroma"],
                    embedding_function=embedding_function
                )

                respuesta = collection.query(
                    query_texts=[consulta],
                    n_results=5
                )

                documentos = respuesta.get("documents", [[]])[0]
                metadatas = respuesta.get("metadatas", [[]])[0]
                distances = respuesta.get("distances", [[]])[0]

                for i, texto in enumerate(documentos):
                    resultados.append({
                        "texto": texto,
                        "metadata": metadatas[i],
                        "distance": distances[i] if i < len(distances) else None
                    })

            except Exception as e:
                error = str(e)

    return render_template(
        "buscar.html",
        activo="buscar",
        consulta=consulta,
        resultados=resultados,
        error=error
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True, host="0.0.0.0", port=5000)
