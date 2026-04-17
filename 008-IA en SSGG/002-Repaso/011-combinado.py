import os
import sys
import requests

def build_tree_text(path, prefix=""):
    lines = []

    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        lines.append(prefix + "[Permiso denegado]")
        return lines

    for i, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_last = i == len(items) - 1

        connector = "└── " if is_last else "├── "
        lines.append(prefix + connector + item)

        if os.path.isdir(full_path):
            extension = "    " if is_last else "│   "
            lines.extend(build_tree_text(full_path, prefix + extension))

    return lines

def summarize_folder_with_ollama(folder_path):
    tree_lines = [folder_path]
    tree_lines.extend(build_tree_text(folder_path))
    tree_text = "\n".join(tree_lines)

    prompt = f"""
Eres un asistente que analiza estructuras de carpetas.

Te voy a pasar el árbol de archivos y carpetas de un proyecto.
Quiero que me respondas en español con un resumen claro y breve de lo que contiene.
Indica:
- Qué tipo de proyecto parece ser
- Qué carpetas o archivos importantes detectas
- Una descripción general de la organización

Árbol del proyecto:

{tree_text}
"""

    url = "http://localhost:11434/api/generate"
    data = {
        "model": "phi4-mini:latest",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=data)
    response.raise_for_status()

    result = response.json()
    return result.get("response", "No se recibió respuesta del modelo.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python resumen_proyecto.py <carpeta>")
        sys.exit(1)

    root = sys.argv[1]

    if not os.path.isdir(root):
        print("Carpeta no válida")
        sys.exit(1)

    try:
        resumen = summarize_folder_with_ollama(root)
        print("\nResumen del contenido:\n")
        print(resumen)
    except Exception as e:
        print(f"Error: {e}")