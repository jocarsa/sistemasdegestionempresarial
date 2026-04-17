from flask import Flask, request, redirect, render_template
import sqlite3, os

app = Flask(__name__)
DB = "clientes.db"

def db(q, args=()):
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    cur = con.execute(q, args); con.commit()
    r = cur.fetchall(); cur.close(); con.close(); return r

# Crear la tabla si no existe
if not os.path.exists(DB):
    db("""CREATE TABLE clientes(
        id INTEGER PRIMARY KEY,
        nombre TEXT, apellidos TEXT, email TEXT, telefono TEXT,
        dni TEXT, fecha_nacimiento TEXT)""")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        f = request.form
        db("INSERT INTO clientes(nombre,apellidos,email,telefono,dni,fecha_nacimiento) VALUES(?,?,?,?,?,?)",
           (f["nombre"], f["apellidos"], f["email"], f.get("telefono",""), f["dni"], f.get("fecha_nacimiento","")))
        return redirect("/")
    filas = db("SELECT * FROM clientes ORDER BY apellidos,nombre")
    return render_template("index.html", filas=filas)

if __name__ == "__main__":
    app.run(debug=True)

