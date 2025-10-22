from flask import Flask, request, jsonify
import sqlite3
import requests
import html

app = Flask(__name__)

DB_PATH = "empresa.db"

def get_conn():
    # Row factory opcional si luego quisieras dicts
    con = sqlite3.connect(DB_PATH)
    return con

# ---------- API interna ----------
@app.route("/api/tables")
def api_tables():
    con = get_conn()
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tablas = [r[0] for r in cur.fetchall() if r[0] != "sqlite_sequence"]
    con.close()
    return jsonify(tablas)

@app.route("/api/table/<table_name>")
def api_table(table_name):
    # Pequeña validación: que la tabla exista
    con = get_conn()
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    valid_tables = {r[0] for r in cur.fetchall() if r[0] != "sqlite_sequence"}
    if table_name not in valid_tables:
        con.close()
        return jsonify({"error": "Tabla no encontrada"}), 404

    # Columnas
    cur.execute(f"PRAGMA table_info({table_name});")
    columns = [row[1] for row in cur.fetchall()]

    # Filas
    cur.execute(f"SELECT * FROM {table_name};")
    rows = cur.fetchall()
    con.close()
    return jsonify({"columns": columns, "rows": rows})

# ---------- UI ----------
@app.route("/")
def index():
    # Base URL para que requests llame a nuestra propia app
    base = request.host_url.rstrip("/")
    # 1) Obtener lista de tablas mediante requests
    r = requests.get(f"{base}/api/tables")
    r.raise_for_status()
    tablas = r.json()

    # Tabla seleccionada (por querystring) o la primera disponible
    seleccion = request.args.get("table") or (tablas[0] if tablas else None)

    # 2) Si hay selección, pedir sus datos al endpoint interno
    cols, rows = [], []
    if seleccion:
        r2 = requests.get(f"{base}/api/table/{seleccion}")
        if r2.status_code == 200:
            data = r2.json()
            cols = data.get("columns", [])
            rows = data.get("rows", [])
        else:
            seleccion = None  # Evita render de tabla si hay error

    # Render HTML
    html_out = '''
    <style>
      body{display:flex;margin:0;padding:0;font-family:system-ui,Arial,sans-serif;}
      nav{flex:1;background:indigo;color:white;padding:20px;min-height:100vh;box-sizing:border-box;}
      main{flex:5;padding:20px;box-sizing:border-box;}
      nav a{text-decoration:none;color:indigo;display:block;background:white;padding:10px;margin:10px 0;border-radius:8px;}
      nav a.active{background:#fff2; color:white; border:1px solid #fff8;}
      table{width:100%;border-collapse:collapse;}
      th,td{padding:8px 10px;text-align:left;}
      tr{border-bottom:1px solid indigo;}
      h1{margin-top:0}
      .muted{opacity:.7}
    </style>
    <body>
      <nav>
        <h3>Tablas</h3>
    '''
    # Enlaces de tablas
    for t in tablas:
        active = "active" if t == seleccion else ""
        html_out += f'<a class="{active}" href="/?table={html.escape(t)}">{html.escape(t)}</a>'

    html_out += '</nav><main>'

    if not tablas:
        html_out += "<h1>Sin tablas</h1><p class='muted'>La base de datos no contiene tablas.</p>"
    elif not seleccion:
        html_out += "<h1>Selecciona una tabla</h1>"
    else:
        html_out += f"<h1>{html.escape(seleccion)}</h1>"
        if cols:
            html_out += "<table><tr>"
            for c in cols:
                html_out += f"<th>{html.escape(str(c))}</th>"
            html_out += "</tr>"
            for row in rows:
                html_out += "<tr>"
                for cell in row:
                    html_out += f"<td>{html.escape(str(cell))}</td>"
                html_out += "</tr>"
            html_out += "</table>"
        else:
            html_out += "<p class='muted'>No hay columnas o datos para esta tabla.</p>"

    html_out += "</main></body>"
    return html_out

if __name__ == "__main__":
    # threaded=True para permitir que 'requests' llame a nuestra propia app sin bloquear
    app.run(debug=True, threaded=True)

