
import sqlite3, datetime
from werkzeug.security import generate_password_hash

DB="lms.db"
USERNAME="alumno1"
PASSWORD="alumno1"

con = sqlite3.connect(DB)
con.row_factory = sqlite3.Row
cur = con.cursor()

# Asegura que exista un alumno para vincular
al = cur.execute("SELECT id FROM alumnos ORDER BY id LIMIT 1").fetchone()
if not al:
    # crea un alumno dummy si no hay
    cur.execute("INSERT INTO alumnos (nombre, apellidos, email) VALUES (?,?,?)",
                ("Alumno","Uno","alumno.uno@example.com"))
    con.commit()
    al = cur.execute("SELECT id FROM alumnos ORDER BY id LIMIT 1").fetchone()

alumno_id = al["id"]
hashval = generate_password_hash(PASSWORD, method="pbkdf2:sha256")

# upsert en alumno_users
row = cur.execute("SELECT id FROM alumno_users WHERE username=?", (USERNAME,)).fetchone()
if row:
    cur.execute("UPDATE alumno_users SET password_hash=?, alumno_id=? WHERE id=?",
                (hashval, alumno_id, row["id"]))
else:
    cur.execute("""INSERT INTO alumno_users (alumno_id, username, password_hash, created_at)
                   VALUES (?,?,?,?)""",
                (alumno_id, USERNAME, hashval, datetime.datetime.utcnow().isoformat()))
con.commit()

# Mostrar resultado
row = cur.execute("SELECT id, alumno_id, username, password_hash FROM alumno_users WHERE username=?",(USERNAME,)).fetchone()
print("OK ->", dict(row))
con.close()


