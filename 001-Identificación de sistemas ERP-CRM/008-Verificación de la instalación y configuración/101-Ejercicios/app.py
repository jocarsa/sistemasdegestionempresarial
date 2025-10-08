# Primero importamos la librería de Flask para montar un servidor
from flask import Flask, request, redirect
# Importamos la base de datos y la librería de sistema
import sqlite3, os

# Creamos una instancia del servidor en Python
app = Flask(__name__)
# Y creamos el apunte a una base de datos
DB = "clientes.db"

# Función de manejo de la base de datos
def db(q, args=()):
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    cur = con.execute(q, args); con.commit()
    r = cur.fetchall(); cur.close(); con.close(); return r

# Si no existe la base de datos, creala - ATENCION aqui modificáis el modelo de datos
if not os.path.exists(DB):
    db("""CREATE TABLE clientes(
        id INTEGER PRIMARY KEY,
        nombre TEXT, apellidos TEXT, email TEXT, telefono TEXT,
        dni TEXT, fecha_nacimiento TEXT)""")

# Raiz, acepta recogida de información
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
      # Si el método es post, inserta nuevo cliente
      # Esta es la estructura que RECIBE los datos
        f = request.form
        db("INSERT INTO clientes(nombre,apellidos,email,telefono,dni,fecha_nacimiento) VALUES(?,?,?,?,?,?)",
           (f["nombre"], f["apellidos"], f["email"], f.get("telefono",""), f["dni"], f.get("fecha_nacimiento","")))
        return redirect("/")
    # en cualquier otro caso, solicita
    filas = db("SELECT * FROM clientes ORDER BY apellidos,nombre")
    # HTML mínimo inline
    
    return """
<!doctype html><meta charset=utf-8>
<title>Clientes</title>
<h3>Nuevo cliente</h3>
<form method=post>
<!-- Este es el formulario que ENVIA los datos -->
  <input name=nombre placeholder=Nombre required>
  <input name=apellidos placeholder=Apellidos required>
  <input name=email type=email placeholder=Email required>
  <input name=telefono placeholder=Teléfono>
  <input name=dni placeholder=DNI required>
  <input name=fecha_nacimiento type=date>
  <button>Guardar</button>
</form>
<h3>Listado</h3>
<table border=1 cellspacing=0 cellpadding=4>
  <tr><th>Nombre</th><th>Apellidos</th><th>Email</th><th>Teléfono</th><th>DNI</th><th>Fecha nac.</th></tr>
  %s
</table>""" % "\n".join(
        f"<tr><td>{r['nombre']}</td><td>{r['apellidos']}</td><td>{r['email']}</td>"
        f"<td>{r['telefono']}</td><td>{r['dni']}</td><td>{r['fecha_nacimiento'] or ''}</td></tr>"
        for r in filas)

if __name__ == "__main__":
    app.run(debug=True)

