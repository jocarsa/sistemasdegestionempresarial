# -*- coding: utf-8 -*-
import sqlite3
from werkzeug.security import generate_password_hash
from datetime import datetime

DB_PATH = "lms.db"

SCHEMA = [
    # Usuarios
    """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'admin',
        created_at TEXT NOT NULL
    );""",
    # Alumnos
    """CREATE TABLE IF NOT EXISTS alumnos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        email TEXT UNIQUE
    );""",
    # Profesores
    """CREATE TABLE IF NOT EXISTS profesores(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellidos TEXT NOT NULL,
        email TEXT UNIQUE
    );""",
    # Cursos
    """CREATE TABLE IF NOT EXISTS cursos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT
    );""",
    # Asignaturas
    """CREATE TABLE IF NOT EXISTS asignaturas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        descripcion TEXT
    );""",
    # Relación curso-asignatura (N:M)
    """CREATE TABLE IF NOT EXISTS cursos_asignaturas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        curso_id INTEGER NOT NULL,
        asignatura_id INTEGER NOT NULL,
        UNIQUE(curso_id, asignatura_id),
        FOREIGN KEY(curso_id) REFERENCES cursos(id) ON DELETE CASCADE,
        FOREIGN KEY(asignatura_id) REFERENCES asignaturas(id) ON DELETE CASCADE
    );""",
    # Matrículas (alumno-curso)
    """CREATE TABLE IF NOT EXISTS matriculas(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        alumno_id INTEGER NOT NULL,
        curso_id INTEGER NOT NULL,
        fecha TEXT NOT NULL,
        UNIQUE(alumno_id, curso_id),
        FOREIGN KEY(alumno_id) REFERENCES alumnos(id) ON DELETE CASCADE,
        FOREIGN KEY(curso_id) REFERENCES cursos(id) ON DELETE CASCADE
    );""",
    # Imparticiones (profesor imparte asignatura en curso)
    """CREATE TABLE IF NOT EXISTS imparticiones(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        profesor_id INTEGER NOT NULL,
        asignatura_id INTEGER NOT NULL,
        curso_id INTEGER NOT NULL,
        UNIQUE(profesor_id, asignatura_id, curso_id),
        FOREIGN KEY(profesor_id) REFERENCES profesores(id) ON DELETE CASCADE,
        FOREIGN KEY(asignatura_id) REFERENCES asignaturas(id) ON DELETE CASCADE,
        FOREIGN KEY(curso_id) REFERENCES cursos(id) ON DELETE CASCADE
    );""",
    # Materiales didácticos
    """CREATE TABLE IF NOT EXISTS materiales(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descripcion TEXT,
        url TEXT,
        asignatura_id INTEGER NOT NULL,
        curso_id INTEGER NOT NULL,
        creado_en TEXT NOT NULL,
        FOREIGN KEY(asignatura_id) REFERENCES asignaturas(id) ON DELETE CASCADE,
        FOREIGN KEY(curso_id) REFERENCES cursos(id) ON DELETE CASCADE
    );"""
]

def seed(conn):
    cur = conn.cursor()
    # Usuario inicial
    cur.execute("SELECT COUNT(*) FROM users;")
    if cur.fetchone()[0] == 0:
        cur.execute(
            "INSERT INTO users (username, password_hash, role, created_at) VALUES (?, ?, ?, ?);",
            ("jocarsa", generate_password_hash("jocarsa"), "admin", datetime.utcnow().isoformat())
        )
        print("✓ Usuario inicial 'jocarsa' creado (contraseña: 'jocarsa').")
    # Datos de ejemplo mínimos
    cur.execute("SELECT COUNT(*) FROM cursos;")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO cursos (nombre, descripcion) VALUES (?, ?);", [
            ("DAM 1º", "Desarrollo de Aplicaciones Multiplataforma - 1º"),
            ("DAW 1º", "Desarrollo de Aplicaciones Web - 1º")
        ])
        print("✓ Cursos de ejemplo insertados.")
    cur.execute("SELECT COUNT(*) FROM asignaturas;")
    if cur.fetchone()[0] == 0:
        cur.executemany("INSERT INTO asignaturas (nombre, descripcion) VALUES (?, ?);", [
            ("Programación", "Fundamentos de programación"),
            ("Bases de datos", "Modelado y SQL"),
            ("Lenguajes de marcas", "HTML/CSS/JS/XML")
        ])
        print("✓ Asignaturas de ejemplo insertadas.")
    conn.commit()

def main():
    conn = sqlite3.connect(DB_PATH)
    try:
        for stmt in SCHEMA:
            conn.execute(stmt)
        conn.commit()
        print("✓ Tablas creadas/verificadas.")
        seed(conn)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
