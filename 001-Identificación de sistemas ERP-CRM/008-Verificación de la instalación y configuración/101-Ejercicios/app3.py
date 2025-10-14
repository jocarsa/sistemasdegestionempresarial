from flask import Flask, request, redirect, render_template, url_for, abort
import sqlite3, os

app = Flask(__name__)
DB = "clientes.db"

def db(q, args=(), one=False):
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    cur = con.execute(q, args); con.commit()
    rows = cur.fetchall(); cur.close(); con.close()
    return (rows[0] if rows else None) if one else rows

# Crear tabla si no existe
if not os.path.exists(DB):
    db("""CREATE TABLE clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT, apellidos TEXT, email TEXT, telefono TEXT,
        dni TEXT, fecha_nacimiento TEXT)""")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        f = request.form
        db("INSERT INTO clientes(nombre,apellidos,email,telefono,dni,fecha_nacimiento) VALUES(?,?,?,?,?,?)",
           (f["nombre"], f["apellidos"], f["email"], f.get("telefono",""), f["dni"], f.get("fecha_nacimiento","")))
        return redirect(url_for("index"))
    filas = db("SELECT * FROM clientes ORDER BY apellidos,nombre")
    return render_template("index.html", filas=filas)

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    if request.method == "POST":
        f = request.form
        db("""UPDATE clientes SET nombre=?, apellidos=?, email=?, telefono=?, dni=?, fecha_nacimiento=?
              WHERE id=?""",
           (f["nombre"], f["apellidos"], f["email"], f.get("telefono",""),
            f["dni"], f.get("fecha_nacimiento",""), id))
        return redirect(url_for("index"))
    r = db("SELECT * FROM clientes WHERE id=?", (id,), one=True)
    if not r: abort(404)
    return render_template("edit.html", r=r)

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    db("DELETE FROM clientes WHERE id=?", (id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)

