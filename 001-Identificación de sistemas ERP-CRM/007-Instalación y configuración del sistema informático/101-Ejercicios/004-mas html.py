from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return '''
    <!doctype html>
    <html>
      <head>
        <title>Flask</title>
      </head>
      <body>
        <h1>Hola desde Python</h1>
      </body>
    </html>
  '''
  
  
if __name__ == "__main__":
  aplicacion.run(debug=True)
