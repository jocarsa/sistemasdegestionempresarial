# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for, session, g, flash
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

DB_PATH = "lms.db"

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "CHANGE-ME-IN-PROD")

# --- DB helpers ---
def get_db():
    if "db" not in g:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        g.db = conn
    return g.db

@app.teardown_appcontext
def close_db(exception):
    db = g.pop("db", None)
    if db is not None:
        db.close()

# --- Auth helpers ---
def login_required(view):
    from functools import wraps
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login"))
        return view(*args, **kwargs)
    return wrapped

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        db = get_db()
        user = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        if user and check_password_hash(user["password_hash"], password):
            session["user_id"] = user["id"]
            session["username"] = user["username"]
            return redirect(url_for("dashboard"))
        flash("Usuario o contraseña incorrectos", "error")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))



# --- Dashboard ---
@app.route("/")
@login_required
def dashboard():
    db = get_db()

    # KPIs
    counts = {
        "users": db.execute("SELECT COUNT(*) AS c FROM users").fetchone()["c"],
        "alumnos": db.execute("SELECT COUNT(*) AS c FROM alumnos").fetchone()["c"],
        "profesores": db.execute("SELECT COUNT(*) AS c FROM profesores").fetchone()["c"],
        "cursos": db.execute("SELECT COUNT(*) AS c FROM cursos").fetchone()["c"],
        "asignaturas": db.execute("SELECT COUNT(*) AS c FROM asignaturas").fetchone()["c"],
        "materiales": db.execute("SELECT COUNT(*) AS c FROM materiales").fetchone()["c"],
        "matriculas": db.execute("SELECT COUNT(*) AS c FROM matriculas").fetchone()["c"],
    }

    # 1) Matrículas por mes (últimos 12 meses)
    from datetime import datetime, timedelta
    start_date = (datetime.utcnow().replace(day=1) - timedelta(days=365)).isoformat()
    rows = db.execute("""
        SELECT substr(fecha,1,7) AS ym, COUNT(*) AS c
        FROM matriculas
        WHERE fecha >= ?
        GROUP BY ym
        ORDER BY ym
    """, (start_date,)).fetchall()
    # normaliza meses faltantes
    def month_iter(n=12):
        # devuelve YYYY-MM para últimos n meses (excluyendo futuro)
        base = datetime.utcnow().replace(day=1)
        lst = []
        for i in range(n-1, -1, -1):
            y = (base.year if base.month - i > 0 else base.year - 1)
            m = ((base.month - i - 1) % 12) + 1
            lst.append(f"{y:04d}-{m:02d}")
        return lst
    months = month_iter(12)
    enrolls_map = {r["ym"]: r["c"] for r in rows}
    enrolls_series = [enrolls_map.get(m, 0) for m in months]

    # 2) Alumnos por curso (TOP 8)
    rows = db.execute("""
        SELECT c.nombre AS curso, COUNT(m.id) AS total
        FROM cursos c
        LEFT JOIN matriculas m ON m.curso_id = c.id
        GROUP BY c.id
        ORDER BY total DESC, c.nombre ASC
        LIMIT 8
    """).fetchall()
    alumnos_por_curso_labels = [r["curso"] for r in rows]
    alumnos_por_curso_data = [r["total"] for r in rows]

    # 3) Materiales por asignatura (TOP 8)
    rows = db.execute("""
        SELECT a.nombre AS asignatura, COUNT(m.id) AS total
        FROM asignaturas a
        LEFT JOIN materiales m ON m.asignatura_id = a.id
        GROUP BY a.id
        ORDER BY total DESC, a.nombre ASC
        LIMIT 8
    """).fetchall()
    materiales_por_asig_labels = [r["asignatura"] for r in rows]
    materiales_por_asig_data = [r["total"] for r in rows]

    # 4) Imparticiones por profesor (TOP 10)
    rows = db.execute("""
        SELECT p.nombre || ' ' || p.apellidos AS profesor, COUNT(i.id) AS total
        FROM profesores p
        LEFT JOIN imparticiones i ON i.profesor_id = p.id
        GROUP BY p.id
        ORDER BY total DESC, profesor ASC
        LIMIT 10
    """).fetchall()
    imparticiones_prof_labels = [r["profesor"] for r in rows]
    imparticiones_prof_data = [r["total"] for r in rows]

    # 5) Cursos ↔ Asignaturas (conteo de asignaturas por curso; TOP 10)
    rows = db.execute("""
        SELECT c.nombre AS curso, COUNT(ca.id) AS total
        FROM cursos c
        LEFT JOIN cursos_asignaturas ca ON ca.curso_id = c.id
        GROUP BY c.id
        ORDER BY total DESC, c.nombre ASC
        LIMIT 10
    """).fetchall()
    asig_por_curso_labels = [r["curso"] for r in rows]
    asig_por_curso_data = [r["total"] for r in rows]

    charts = {
        "months": months,
        "enrolls_series": enrolls_series,
        "alumnos_por_curso_labels": alumnos_por_curso_labels,
        "alumnos_por_curso_data": alumnos_por_curso_data,
        "materiales_por_asig_labels": materiales_por_asig_labels,
        "materiales_por_asig_data": materiales_por_asig_data,
        "imparticiones_prof_labels": imparticiones_prof_labels,
        "imparticiones_prof_data": imparticiones_prof_data,
        "asig_por_curso_labels": asig_por_curso_labels,
        "asig_por_curso_data": asig_por_curso_data,
    }

    return render_template("dashboard.html", counts=counts, charts=charts)


# --- Usuarios (solo admin básico) ---
@app.route("/admin/usuarios")
@login_required
def usuarios_list():
    db = get_db()
    users = db.execute("SELECT id, username, role, created_at FROM users ORDER BY id DESC").fetchall()
    return render_template("usuarios_list.html", users=users)

@app.route("/admin/usuarios/nuevo", methods=["GET","POST"])
@login_required
def usuarios_nuevo():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"]
        role = request.form.get("role","admin")
        db = get_db()
        try:
            db.execute("INSERT INTO users (username, password_hash, role, created_at) VALUES (?,?,?,?)",
                       (username, generate_password_hash(password), role, datetime.utcnow().isoformat()))
            db.commit()
            return redirect(url_for("usuarios_list"))
        except sqlite3.IntegrityError:
            flash("El usuario ya existe.", "error")
    return render_template("usuarios_form.html", user=None)

@app.route("/admin/usuarios/<int:user_id>/resetpass", methods=["POST"])
@login_required
def usuarios_resetpass(user_id):
    newpass = request.form.get("newpass","")
    if not newpass:
        flash("Proporciona una nueva contraseña", "error")
        return redirect(url_for("usuarios_list"))
    db = get_db()
    db.execute("UPDATE users SET password_hash=? WHERE id=?", (generate_password_hash(newpass), user_id))
    db.commit()
    flash("Contraseña actualizada.", "ok")
    return redirect(url_for("usuarios_list"))

@app.route("/admin/usuarios/<int:user_id>/eliminar", methods=["POST"])
@login_required
def usuarios_eliminar(user_id):
    db = get_db()
    db.execute("DELETE FROM users WHERE id=?", (user_id,))
    db.commit()
    return redirect(url_for("usuarios_list"))

# --- CRUD genérico simple para entidades base ---

# Alumnos
@app.route("/admin/alumnos")
@login_required
def alumnos_list():
    db = get_db()
    items = db.execute("SELECT * FROM alumnos ORDER BY id DESC").fetchall()
    return render_template("alumnos_list.html", items=items)

@app.route("/admin/alumnos/nuevo", methods=["GET","POST"])
@login_required
def alumnos_nuevo():
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        apellidos = request.form["apellidos"].strip()
        email = request.form.get("email","").strip() or None
        db = get_db()
        try:
            db.execute("INSERT INTO alumnos (nombre, apellidos, email) VALUES (?,?,?)", (nombre, apellidos, email))
            db.commit()
            return redirect(url_for("alumnos_list"))
        except sqlite3.IntegrityError:
            flash("Email duplicado.", "error")
    return render_template("alumnos_form.html", item=None)

@app.route("/admin/alumnos/<int:item_id>/editar", methods=["GET","POST"])
@login_required
def alumnos_editar(item_id):
    db = get_db()
    item = db.execute("SELECT * FROM alumnos WHERE id=?", (item_id,)).fetchone()
    if not item:
        return redirect(url_for("alumnos_list"))
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        apellidos = request.form["apellidos"].strip()
        email = request.form.get("email","").strip() or None
        try:
            db.execute("UPDATE alumnos SET nombre=?, apellidos=?, email=? WHERE id=?", (nombre, apellidos, email, item_id))
            db.commit()
            return redirect(url_for("alumnos_list"))
        except sqlite3.IntegrityError:
            flash("Email duplicado.", "error")
    return render_template("alumnos_form.html", item=item)

@app.route("/admin/alumnos/<int:item_id>/eliminar", methods=["POST"])
@login_required
def alumnos_eliminar(item_id):
    db = get_db()
    db.execute("DELETE FROM alumnos WHERE id=?", (item_id,))
    db.commit()
    return redirect(url_for("alumnos_list"))

# Profesores
@app.route("/admin/profesores")
@login_required
def profesores_list():
    db = get_db()
    items = db.execute("SELECT * FROM profesores ORDER BY id DESC").fetchall()
    return render_template("profesores_list.html", items=items)

@app.route("/admin/profesores/nuevo", methods=["GET","POST"])
@login_required
def profesores_nuevo():
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        apellidos = request.form["apellidos"].strip()
        email = request.form.get("email","").strip() or None
        db = get_db()
        try:
            db.execute("INSERT INTO profesores (nombre, apellidos, email) VALUES (?,?,?)", (nombre, apellidos, email))
            db.commit()
            return redirect(url_for("profesores_list"))
        except sqlite3.IntegrityError:
            flash("Email duplicado.", "error")
    return render_template("profesores_form.html", item=None)

@app.route("/admin/profesores/<int:item_id>/editar", methods=["GET","POST"])
@login_required
def profesores_editar(item_id):
    db = get_db()
    item = db.execute("SELECT * FROM profesores WHERE id=?", (item_id,)).fetchone()
    if not item:
        return redirect(url_for("profesores_list"))
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        apellidos = request.form["apellidos"].strip()
        email = request.form.get("email","").strip() or None
        try:
            db.execute("UPDATE profesores SET nombre=?, apellidos=?, email=? WHERE id=?", (nombre, apellidos, email, item_id))
            db.commit()
            return redirect(url_for("profesores_list"))
        except sqlite3.IntegrityError:
            flash("Email duplicado.", "error")
    return render_template("profesores_form.html", item=item)

@app.route("/admin/profesores/<int:item_id>/eliminar", methods=["POST"])
@login_required
def profesores_eliminar(item_id):
    db = get_db()
    db.execute("DELETE FROM profesores WHERE id=?", (item_id,))
    db.commit()
    return redirect(url_for("profesores_list"))

# Cursos
@app.route("/admin/cursos")
@login_required
def cursos_list():
    db = get_db()
    items = db.execute("SELECT * FROM cursos ORDER BY id DESC").fetchall()
    return render_template("cursos_list.html", items=items)

@app.route("/admin/cursos/nuevo", methods=["GET","POST"])
@login_required
def cursos_nuevo():
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        descripcion = request.form.get("descripcion","").strip() or None
        db = get_db()
        db.execute("INSERT INTO cursos (nombre, descripcion) VALUES (?,?)", (nombre, descripcion))
        db.commit()
        return redirect(url_for("cursos_list"))
    return render_template("cursos_form.html", item=None)

@app.route("/admin/cursos/<int:item_id>/editar", methods=["GET","POST"])
@login_required
def cursos_editar(item_id):
    db = get_db()
    item = db.execute("SELECT * FROM cursos WHERE id=?", (item_id,)).fetchone()
    if not item:
        return redirect(url_for("cursos_list"))
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        descripcion = request.form.get("descripcion","").strip() or None
        db.execute("UPDATE cursos SET nombre=?, descripcion=? WHERE id=?", (nombre, descripcion, item_id))
        db.commit()
        return redirect(url_for("cursos_list"))
    return render_template("cursos_form.html", item=item)

@app.route("/admin/cursos/<int:item_id>/eliminar", methods=["POST"])
@login_required
def cursos_eliminar(item_id):
    db = get_db()
    db.execute("DELETE FROM cursos WHERE id=?", (item_id,))
    db.commit()
    return redirect(url_for("cursos_list"))

# Asignaturas
@app.route("/admin/asignaturas")
@login_required
def asignaturas_list():
    db = get_db()
    items = db.execute("SELECT * FROM asignaturas ORDER BY id DESC").fetchall()
    return render_template("asignaturas_list.html", items=items)

@app.route("/admin/asignaturas/nuevo", methods=["GET","POST"])
@login_required
def asignaturas_nuevo():
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        descripcion = request.form.get("descripcion","").strip() or None
        db = get_db()
        db.execute("INSERT INTO asignaturas (nombre, descripcion) VALUES (?,?)", (nombre, descripcion))
        db.commit()
        return redirect(url_for("asignaturas_list"))
    return render_template("asignaturas_form.html", item=None)

@app.route("/admin/asignaturas/<int:item_id>/editar", methods=["GET","POST"])
@login_required
def asignaturas_editar(item_id):
    db = get_db()
    item = db.execute("SELECT * FROM asignaturas WHERE id=?", (item_id,)).fetchone()
    if not item:
        return redirect(url_for("asignaturas_list"))
    if request.method == "POST":
        nombre = request.form["nombre"].strip()
        descripcion = request.form.get("descripcion","").strip() or None
        db.execute("UPDATE asignaturas SET nombre=?, descripcion=? WHERE id=?", (nombre, descripcion, item_id))
        db.commit()
        return redirect(url_for("asignaturas_list"))
    return render_template("asignaturas_form.html", item=item)

@app.route("/admin/asignaturas/<int:item_id>/eliminar", methods=["POST"])
@login_required
def asignaturas_eliminar(item_id):
    db = get_db()
    db.execute("DELETE FROM asignaturas WHERE id=?", (item_id,))
    db.commit()
    return redirect(url_for("asignaturas_list"))

# Materiales
@app.route("/admin/materiales")
@login_required
def materiales_list():
    db = get_db()
    items = db.execute(
        """SELECT m.id, m.titulo, m.descripcion, m.url, m.creado_en,
                       c.nombre AS curso, a.nombre AS asignatura
               FROM materiales m
               JOIN cursos c ON c.id = m.curso_id
               JOIN asignaturas a ON a.id = m.asignatura_id
               ORDER BY m.id DESC""").fetchall()
    return render_template("materiales_list.html", items=items)

@app.route("/admin/materiales/nuevo", methods=["GET","POST"])
@login_required
def materiales_nuevo():
    db = get_db()
    cursos = db.execute("SELECT id, nombre FROM cursos ORDER BY nombre").fetchall()
    asignaturas = db.execute("SELECT id, nombre FROM asignaturas ORDER BY nombre").fetchall()
    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        descripcion = request.form.get("descripcion","").strip() or None
        url = request.form.get("url","").strip() or None
        curso_id = int(request.form["curso_id"])
        asignatura_id = int(request.form["asignatura_id"])
        db.execute("""INSERT INTO materiales
                    (titulo, descripcion, url, asignatura_id, curso_id, creado_en)
                    VALUES (?,?,?,?,?,?)""",
                   (titulo, descripcion, url, asignatura_id, curso_id, datetime.utcnow().isoformat()))
        db.commit()
        return redirect(url_for("materiales_list"))
    return render_template("materiales_form.html", cursos=cursos, asignaturas=asignaturas, item=None)

@app.route("/admin/materiales/<int:item_id>/eliminar", methods=["POST"])
@login_required
def materiales_eliminar(item_id):
    db = get_db()
    db.execute("DELETE FROM materiales WHERE id=?", (item_id,))
    db.commit()
    return redirect(url_for("materiales_list"))

# Relaciones rápidas (matrículas e imparticiones) — mínimas para demo
@app.route("/admin/matriculas", methods=["GET","POST"])
@login_required
def matriculas():
    db = get_db()
    if request.method == "POST":
        alumno_id = int(request.form["alumno_id"])
        curso_id = int(request.form["curso_id"])
        try:
            db.execute("INSERT INTO matriculas (alumno_id, curso_id, fecha) VALUES (?,?,?)",
                       (alumno_id, curso_id, datetime.utcnow().isoformat()))
            db.commit()
        except sqlite3.IntegrityError:
            flash("La matrícula ya existe.", "error")
    data = db.execute(
        """SELECT m.id, a.nombre||' '||a.apellidos AS alumno, c.nombre AS curso, m.fecha
               FROM matriculas m
               JOIN alumnos a ON a.id = m.alumno_id
               JOIN cursos c  ON c.id = m.curso_id
               ORDER BY m.id DESC""").fetchall()
    alumnos = db.execute("SELECT id, nombre||' '||apellidos AS n FROM alumnos ORDER BY n").fetchall()
    cursos = db.execute("SELECT id, nombre FROM cursos ORDER BY nombre").fetchall()
    return render_template("matriculas.html", data=data, alumnos=alumnos, cursos=cursos)

@app.route("/admin/matriculas/<int:item_id>/eliminar", methods=["POST"])
@login_required
def matriculas_eliminar(item_id):
    db = get_db()
    db.execute("DELETE FROM matriculas WHERE id=?", (item_id,))
    db.commit()
    return redirect(url_for("matriculas"))

@app.route("/admin/imparticiones", methods=["GET","POST"])
@login_required
def imparticiones():
    db = get_db()
    if request.method == "POST":
        profesor_id = int(request.form["profesor_id"])
        asignatura_id = int(request.form["asignatura_id"])
        curso_id = int(request.form["curso_id"])
        try:
            db.execute("INSERT INTO imparticiones (profesor_id, asignatura_id, curso_id) VALUES (?,?,?)",
                       (profesor_id, asignatura_id, curso_id))
            db.commit()
        except sqlite3.IntegrityError:
            flash("La impartición ya existe.", "error")
    data = db.execute(
        """SELECT i.id,
                      p.nombre||' '||p.apellidos AS profesor,
                      a.nombre AS asignatura,
                      c.nombre AS curso
               FROM imparticiones i
               JOIN profesores p ON p.id = i.profesor_id
               JOIN asignaturas a ON a.id = i.asignatura_id
               JOIN cursos c ON c.id = i.curso_id
               ORDER BY i.id DESC""").fetchall()
    profesores = db.execute("SELECT id, nombre||' '||apellidos AS n FROM profesores ORDER BY n").fetchall()
    asignaturas = db.execute("SELECT id, nombre FROM asignaturas ORDER BY nombre").fetchall()
    cursos = db.execute("SELECT id, nombre FROM cursos ORDER BY nombre").fetchall()
    return render_template("imparticiones.html", data=data, profesores=profesores, asignaturas=asignaturas, cursos=cursos)

@app.route("/admin/imparticiones/<int:item_id>/eliminar", methods=["POST"])
@login_required
def imparticiones_eliminar(item_id):
    db = get_db()
    db.execute("DELETE FROM imparticiones WHERE id=?", (item_id,))
    db.commit()
    return redirect(url_for("imparticiones"))

# ====== [A] UTILIDADES: asegurar tablas extra (si no ejecutaste el SQL manualmente) ======
def ensure_student_front_schema():
    db = get_db()
    db.executescript("""
    CREATE TABLE IF NOT EXISTS alumno_users(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      alumno_id INTEGER UNIQUE NOT NULL,
      username TEXT UNIQUE NOT NULL,
      password_hash TEXT NOT NULL,
      created_at TEXT NOT NULL,
      FOREIGN KEY(alumno_id) REFERENCES alumnos(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS actividades(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      curso_id INTEGER NOT NULL,
      asignatura_id INTEGER NOT NULL,
      titulo TEXT NOT NULL,
      descripcion TEXT,
      tipo TEXT NOT NULL DEFAULT 'Tarea',
      fecha_publicacion TEXT NOT NULL,
      fecha_entrega TEXT,
      FOREIGN KEY(curso_id) REFERENCES cursos(id) ON DELETE CASCADE,
      FOREIGN KEY(asignatura_id) REFERENCES asignaturas(id) ON DELETE CASCADE
    );
    CREATE TABLE IF NOT EXISTS entregas(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      actividad_id INTEGER NOT NULL,
      alumno_id INTEGER NOT NULL,
      url TEXT,
      comentario TEXT,
      fecha TEXT NOT NULL,
      UNIQUE(actividad_id, alumno_id),
      FOREIGN KEY(actividad_id) REFERENCES actividades(id) ON DELETE CASCADE,
      FOREIGN KEY(alumno_id) REFERENCES alumnos(id) ON DELETE CASCADE
    );
    """)
    db.commit()

@app.before_request
def _ensure_schema():
    # Garantiza que el front alumno tenga sus tablas
    ensure_student_front_schema()

# ====== [B] AUTH ALUMNO ======
def student_login_required(view):
    from functools import wraps
    @wraps(view)
    def wrapped(*args, **kwargs):
        if "student_id" not in session:
            return redirect(url_for("alumno_login"))
        return view(*args, **kwargs)
    return wrapped

@app.route("/alumno/login", methods=["GET", "POST"])
def alumno_login():
    if request.method == "POST":
        username = request.form.get("username","").strip()
        password = request.form.get("password","")
        db = get_db()
        row = db.execute("SELECT * FROM alumno_users WHERE username=?", (username,)).fetchone()
        if row and check_password_hash(row["password_hash"], password):
            session.clear()
            session["student_id"] = row["alumno_id"]
            session["student_username"] = row["username"]
            return redirect(url_for("alumno_home"))
        flash("Usuario o contraseña incorrectos", "error")
    return render_template("alumno_login.html")

@app.route("/alumno/logout")
def alumno_logout():
    session.pop("student_id", None)
    session.pop("student_username", None)
    return redirect(url_for("alumno_login"))

# Endpoint admin (rápido) para crear cuenta de alumno con hash (puedes retirarlo en prod)
@app.route("/admin/alumno_user/new", methods=["POST"])
@login_required
def admin_create_alumno_user():
    alumno_id = int(request.form["alumno_id"])
    username = request.form["username"].strip()
    password = request.form["password"]
    db = get_db()
    try:
        db.execute(
          "INSERT INTO alumno_users (alumno_id, username, password_hash, created_at) VALUES (?,?,?,?)",
          (alumno_id, username, generate_password_hash(password), datetime.utcnow().isoformat())
        )
        db.commit()
        flash("Cuenta de alumno creada.", "ok")
    except sqlite3.IntegrityError as e:
        flash(f"Error creando cuenta: {e}", "error")
    return redirect(url_for("alumnos_list"))

# ====== [C] VISTAS ALUMNO ======
@app.route("/alumno")
@student_login_required
def alumno_home():
    db = get_db()
    alumno = db.execute("SELECT * FROM alumnos WHERE id=?", (session["student_id"],)).fetchone()
    cursos = db.execute("""
        SELECT c.id, c.nombre, c.descripcion
        FROM cursos c
        JOIN matriculas m ON m.curso_id = c.id
        WHERE m.alumno_id = ?
        ORDER BY c.nombre
    """, (session["student_id"],)).fetchall()

    # Próximas actividades (de cursos matriculados)
    actividades = db.execute("""
        SELECT act.id, act.titulo, act.tipo, act.fecha_entrega, c.nombre AS curso, a.nombre AS asignatura
        FROM actividades act
        JOIN cursos c ON c.id = act.curso_id
        JOIN asignaturas a ON a.id = act.asignatura_id
        WHERE act.curso_id IN (SELECT curso_id FROM matriculas WHERE alumno_id=?)
        ORDER BY COALESCE(act.fecha_entrega, act.fecha_publicacion) ASC
        LIMIT 15
    """, (session["student_id"],)).fetchall()

    return render_template("alumno_dashboard.html", alumno=alumno, cursos=cursos, actividades=actividades)

@app.route("/alumno/curso/<int:curso_id>")
@student_login_required
def alumno_curso(curso_id):
    db = get_db()
    # Seguridad: el alumno debe estar matriculado
    ok = db.execute("SELECT 1 FROM matriculas WHERE alumno_id=? AND curso_id=?", (session["student_id"], curso_id)).fetchone()
    if not ok:
        flash("No estás matriculado en este curso.", "error")
        return redirect(url_for("alumno_home"))

    curso = db.execute("SELECT * FROM cursos WHERE id=?", (curso_id,)).fetchone()
    asignaturas = db.execute("""
        SELECT a.id, a.nombre, a.descripcion
        FROM asignaturas a
        JOIN cursos_asignaturas ca ON ca.asignatura_id = a.id
        WHERE ca.curso_id=?
        ORDER BY a.nombre
    """, (curso_id,)).fetchall()
    materiales = db.execute("""
        SELECT m.id, m.titulo, m.descripcion, m.url, m.creado_en, a.nombre AS asignatura
        FROM materiales m
        JOIN asignaturas a ON a.id = m.asignatura_id
        WHERE m.curso_id=?
        ORDER BY m.creado_en DESC
    """, (curso_id,)).fetchall()
    actividades = db.execute("""
        SELECT act.*, a.nombre AS asignatura
        FROM actividades act
        JOIN asignaturas a ON a.id = act.asignatura_id
        WHERE act.curso_id=?
        ORDER BY COALESCE(act.fecha_entrega, act.fecha_publicacion) ASC
    """, (curso_id,)).fetchall()

    # Entregas del alumno en este curso
    entregas = db.execute("""
        SELECT e.actividad_id, e.url, e.comentario, e.fecha
        FROM entregas e
        WHERE e.alumno_id=? AND e.actividad_id IN (SELECT id FROM actividades WHERE curso_id=?)
    """, (session["student_id"], curso_id)).fetchall()
    entregas_map = {e["actividad_id"]: e for e in entregas}

    return render_template("alumno_curso.html",
                           curso=curso, asignaturas=asignaturas, materiales=materiales,
                           actividades=actividades, entregas=entregas_map)

@app.route("/alumno/actividad/<int:actividad_id>/entregar", methods=["POST"])
@student_login_required
def alumno_entregar(actividad_id):
    url_submit = request.form.get("url","").strip() or None
    comentario = request.form.get("comentario","").strip() or None
    db = get_db()

    # Validación simple: actividad pertenece a un curso donde está matriculado
    valid = db.execute("""
        SELECT 1 FROM actividades WHERE id=? AND curso_id IN (SELECT curso_id FROM matriculas WHERE alumno_id=?)
    """, (actividad_id, session["student_id"])).fetchone()
    if not valid:
        flash("No puedes entregar en esta actividad.", "error")
        return redirect(url_for("alumno_home"))

    try:
        db.execute("""
            INSERT INTO entregas (actividad_id, alumno_id, url, comentario, fecha)
            VALUES (?,?,?,?,?)
            ON CONFLICT(actividad_id, alumno_id) DO UPDATE SET
              url=excluded.url, comentario=excluded.comentario, fecha=excluded.fecha
        """, (actividad_id, session["student_id"], url_submit, comentario, datetime.utcnow().isoformat()))
        db.commit()
        flash("Entrega guardada.", "ok")
    except sqlite3.IntegrityError as e:
        flash(f"Error al guardar entrega: {e}", "error")

    # Redirige al curso de la actividad
    curso_id = db.execute("SELECT curso_id FROM actividades WHERE id=?", (actividad_id,)).fetchone()["curso_id"]
    return redirect(url_for("alumno_curso", curso_id=curso_id))


if __name__ == "__main__":
    app.run(debug=True)
