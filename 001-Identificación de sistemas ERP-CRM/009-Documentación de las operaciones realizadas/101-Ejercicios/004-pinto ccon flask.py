from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  return "Hola mundo desde Flask"

con = sqlite3.connect('empresa.db')
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())
con.close()

if __name__ == "__main__":
    app.run(debug=True)
