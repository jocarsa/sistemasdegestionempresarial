from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  html = '''
    <style>
      body{display:flex;margin:0px;padding:0px;}
      nav{flex:1;background:indigo;color:white;padding:20px;}
      main{flex:5;padding:20px;}
      nav a{text-decoration:none;color:inherit;display:block;background:white;color:indigo;padding:10px;margin:20px;}
      table{width:100%;}
      table tr{border-bottom:1px solid indigo;}
    </style>
    <body>
      <nav>'''
  con = sqlite3.connect('empresa.db')
  cur = con.cursor()
  cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
  lineas = cur.fetchall()
  for linea in lineas:
    if linea[0] != "sqlite_sequence":
      html += '<a href="">'+linea[0]+'</a>'
    
  html += '''</nav>
      <main>
      <table>
      <tr>

      '''
  cur.execute("PRAGMA table_info(clientes);")    
  lineas = cur.fetchall()
  for linea in lineas:
    html += '<th>'+str(linea[1])+'</th>'
  html += '''
  </tr>'''
  cur.execute("SELECT * FROM clientes;")
  lineas = cur.fetchall()  
  for linea in lineas:
    html += '<tr>'
    for campo in linea:
      html += '<td>' + str(campo) + '</td>'
    html += '</tr>'
  html += '''
  </table>
  </main>
    </body>
  '''
  con.close()  
  return html

if __name__ == "__main__":
    app.run(debug=True)
