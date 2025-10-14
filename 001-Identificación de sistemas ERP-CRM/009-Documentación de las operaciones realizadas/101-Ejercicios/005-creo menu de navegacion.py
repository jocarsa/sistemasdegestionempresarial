from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  html = '''
    <style>
      body{display:flex;margin:0px;padding:0px;}
      nav{flex:1;background:indigo;color:white;padding:20px;}
      main{flex:5;}
      nav a{text-decoration:none;color:inherit;display:block;background:white;color:indigo;padding:10px;margin:20px;}
    </style>
    <body>
      <nav>'''
  con = sqlite3.connect('empresa.db')
  cur = con.cursor()
  cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
  lineas = cur.fetchall()
  for linea in lineas:
    html += '<a href="">'+linea[0]+'</a>'
  con.close()    
  html += '''</nav>
      <main></main>
    </body>
  '''
  return html

if __name__ == "__main__":
    app.run(debug=True)
