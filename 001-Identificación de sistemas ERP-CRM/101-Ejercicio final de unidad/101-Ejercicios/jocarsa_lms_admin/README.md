# LMS Admin (CRM/ERP-style) — Flask + SQLite

Panel de administración para un LMS sencillo (estilo Moodle) con stack:
- Backend: Python + Flask
- DB: SQLite
- Front: HTML + CSS + JS vanilla

## Características
- Login con contraseñas *hasheadas* (`werkzeug.security`).
- Usuario inicial: **jocarsa / jocarsa**
- Entidades: Usuarios, Alumnos, Profesores, Cursos, Asignaturas, Materiales.
- Relaciones: cursos_asignaturas, matrículas (alumno↔curso), imparticiones (profesor↔asignatura↔curso).
- CRUD básico desde panel de admin.

## Puesta en marcha
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 1) Crear/Resetear la base de datos (ejecutar una vez o cuando quieras reiniciar)
python configurar.py

# 2) Ejecutar la aplicación
python app.py
# Visita: http://127.0.0.1:5000
```

> **Notas**
> - La base de datos se crea en `lms.db` en el directorio del proyecto.
> - Cambia `SECRET_KEY` en `app.py` para producción.
> - Este proyecto es educativo: no incluye CSRF, RBAC granular ni paginación.
