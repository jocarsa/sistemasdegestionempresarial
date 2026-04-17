import os
import re
import json
import time
import textwrap
import requests
from PIL import Image, ImageDraw, ImageFont

# ==============================
# CONFIGURACIÓN
# ==============================

ARCHIVO_ENTRADA = "programacion.txt"
ARCHIVO_SALIDA = "resultado.md"
CARPETA_IMAGENES = "imagenes_codigo"

URL_OLLAMA = "http://localhost:11434/api/generate"

MODELO_EXPLICACION = "qwen2.5:3b-instruct"
MODELO_CODIGO = "qwen2.5-coder:7b"
MODELO_DESGLOSE = "qwen2.5:3b-instruct"

PAUSA_ENTRE_PETICIONES = 1

POSIBLES_FUENTES_MONO = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",
    "/usr/share/fonts/truetype/freefont/FreeMono.ttf",
    "C:/Windows/Fonts/consola.ttf",
    "C:/Windows/Fonts/cour.ttf",
    "/System/Library/Fonts/Menlo.ttc",
]

POSIBLES_FUENTES_UI = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
    "C:/Windows/Fonts/arial.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
]

# ==============================
# UTILIDADES
# ==============================

def buscar_fuente(lista_rutas, tam):
    for ruta in lista_rutas:
        if os.path.exists(ruta):
            try:
                return ImageFont.truetype(ruta, tam)
            except Exception:
                pass
    return ImageFont.load_default()

def limpiar_nombre_archivo(texto):
    texto = texto.strip().lower()
    texto = texto.replace("−", "")
    texto = re.sub(r"[^\w\s-]", "", texto, flags=re.UNICODE)
    texto = re.sub(r"\s+", "_", texto)
    return texto[:80] if texto else "bloque"

def es_titulo(linea):
    return linea.endswith(":")

def normalizar_linea(linea):
    return linea.strip().lstrip("−").strip()

def extraer_codigo(texto):
    bloques = re.findall(r"```(?:cpp|c\+\+)?\s*(.*?)```", texto, flags=re.DOTALL | re.IGNORECASE)
    if bloques:
        return "\n\n".join(b.strip() for b in bloques if b.strip())
    return texto.strip()

def extraer_json(texto):
    texto = texto.strip()

    try:
        return json.loads(texto)
    except Exception:
        pass

    m = re.search(r"```json\s*(.*?)```", texto, flags=re.DOTALL | re.IGNORECASE)
    if m:
        try:
            return json.loads(m.group(1).strip())
        except Exception:
            pass

    m = re.search(r"(\{.*\}|\[.*\])", texto, flags=re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1).strip())
        except Exception:
            pass

    raise ValueError("No se pudo extraer un JSON válido de la respuesta.")

def llamada_ollama(modelo, prompt, timeout=300):
    response = requests.post(
        URL_OLLAMA,
        json={
            "model": modelo,
            "prompt": prompt,
            "stream": False
        },
        timeout=timeout
    )
    response.raise_for_status()
    data = response.json()
    return data.get("response", "").strip()

def escapar_markdown_texto_plano(texto):
    """
    Evita que Google Drive o Markdown interpreten ciertos símbolos.
    No usa bloques ```code```.
    """
    texto = texto.replace("\\", "\\\\")
    texto = texto.replace("*", "\\*")
    texto = texto.replace("_", "\\_")
    texto = texto.replace("#", "\\#")
    texto = texto.replace("`", "'")
    return texto

def formatear_fragmento_plano(lineas_codigo, inicio, fin):
    """
    Devuelve un fragmento textual con numeración real.
    """
    partes = []
    for numero in range(inicio, fin + 1):
        contenido = lineas_codigo[numero - 1]
        partes.append(f"{numero:>3}: {contenido}")
    return "\n".join(partes)

def normalizar_pasos(datos, total_lineas):
    pasos = datos.get("pasos", [])
    pasos_validos = []

    for i, paso in enumerate(pasos, start=1):
        try:
            titulo = str(paso.get("titulo", f"Paso {i}")).strip()
            linea_inicio = int(paso.get("linea_inicio", 1))
            linea_fin = int(paso.get("linea_fin", 1))
            explicacion = str(paso.get("explicacion", "")).strip()

            if linea_inicio < 1:
                linea_inicio = 1
            if linea_fin < 1:
                linea_fin = 1
            if linea_inicio > total_lineas:
                linea_inicio = total_lineas
            if linea_fin > total_lineas:
                linea_fin = total_lineas
            if linea_fin < linea_inicio:
                linea_fin = linea_inicio

            pasos_validos.append({
                "titulo": titulo,
                "linea_inicio": linea_inicio,
                "linea_fin": linea_fin,
                "explicacion": explicacion
            })
        except Exception:
            continue

    if not pasos_validos:
        pasos_validos = [{
            "titulo": "Paso 1",
            "linea_inicio": 1,
            "linea_fin": total_lineas,
            "explicacion": "Explicación general del ejemplo completo."
        }]

    pasos_validos.sort(key=lambda x: (x["linea_fin"], x["linea_inicio"]))

    return pasos_validos

# ==============================
# RENDER A PNG
# ==============================

def medir_texto(draw, texto, font):
    bbox = draw.textbbox((0, 0), texto, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]

def partir_lineas_largas(lineas, ancho_max_caracteres=90):
    nuevas = []
    for linea in lineas:
        if not linea.strip():
            nuevas.append("")
            continue

        indent = re.match(r"^\s*", linea).group(0)
        contenido = linea[len(indent):]

        if len(linea) <= ancho_max_caracteres:
            nuevas.append(linea)
        else:
            trozos = textwrap.wrap(
                contenido,
                width=max(20, ancho_max_caracteres - len(indent)),
                replace_whitespace=False,
                drop_whitespace=False
            )
            if not trozos:
                nuevas.append(linea)
            else:
                for trozo in trozos:
                    nuevas.append(indent + trozo)
    return nuevas

def render_codigo_a_png(codigo, ruta_salida, titulo="main.cpp"):
    os.makedirs(os.path.dirname(ruta_salida), exist_ok=True)

    fuente_codigo = buscar_fuente(POSIBLES_FUENTES_MONO, 22)
    fuente_ui = buscar_fuente(POSIBLES_FUENTES_UI, 18)
    fuente_num = buscar_fuente(POSIBLES_FUENTES_MONO, 20)

    codigo = codigo.replace("\t", "    ").rstrip() + "\n"
    lineas = partir_lineas_largas(codigo.splitlines(), ancho_max_caracteres=88)

    color_fondo = (245, 246, 248)
    color_ventana = (255, 255, 255)
    color_barra = (235, 236, 240)
    color_borde = (210, 214, 220)
    color_texto = (35, 39, 47)
    color_num_linea = (130, 138, 150)
    color_sombra = (0, 0, 0, 20)

    rojo = (255, 95, 86)
    amarillo = (255, 189, 46)
    verde = (39, 201, 63)

    padding_externo = 30
    padding_interno_x = 24
    padding_interno_y = 20
    ancho_numeracion = 60
    alto_barra = 42
    radio = 18
    interlineado_extra = 10

    imagen_aux = Image.new("RGBA", (10, 10), color_fondo)
    draw_aux = ImageDraw.Draw(imagen_aux)

    ancho_texto_max = 0
    alto_linea_max = 0

    for linea in lineas:
        w, h = medir_texto(draw_aux, linea if linea else " ", fuente_codigo)
        ancho_texto_max = max(ancho_texto_max, w)
        alto_linea_max = max(alto_linea_max, h)

    _, alto_num = medir_texto(draw_aux, "999", fuente_num)
    alto_linea = max(alto_linea_max, alto_num) + interlineado_extra

    ancho_ventana = padding_interno_x + ancho_numeracion + 20 + ancho_texto_max + padding_interno_x
    alto_contenido = padding_interno_y * 2 + len(lineas) * alto_linea
    alto_ventana = alto_barra + alto_contenido

    ancho_total = ancho_ventana + padding_externo * 2
    alto_total = alto_ventana + padding_externo * 2

    img = Image.new("RGBA", (ancho_total, alto_total), color_fondo)
    draw = ImageDraw.Draw(img)

    sombra_offset = 8
    draw.rounded_rectangle(
        (
            padding_externo + sombra_offset,
            padding_externo + sombra_offset,
            padding_externo + ancho_ventana + sombra_offset,
            padding_externo + alto_ventana + sombra_offset
        ),
        radius=radio,
        fill=color_sombra
    )

    x0 = padding_externo
    y0 = padding_externo
    x1 = x0 + ancho_ventana
    y1 = y0 + alto_ventana

    draw.rounded_rectangle((x0, y0, x1, y1), radius=radio, fill=color_ventana, outline=color_borde, width=1)
    draw.rounded_rectangle((x0, y0, x1, y0 + alto_barra), radius=radio, fill=color_barra, outline=color_borde, width=1)
    draw.rectangle((x0, y0 + alto_barra - radio, x1, y0 + alto_barra), fill=color_barra)

    bx = x0 + 18
    by = y0 + alto_barra // 2
    r = 6
    draw.ellipse((bx - r, by - r, bx + r, by + r), fill=rojo)
    draw.ellipse((bx + 20 - r, by - r, bx + 20 + r, by + r), fill=amarillo)
    draw.ellipse((bx + 40 - r, by - r, bx + 40 + r, by + r), fill=verde)

    titulo_w, titulo_h = medir_texto(draw, titulo, fuente_ui)
    draw.text(
        (x0 + (ancho_ventana - titulo_w) / 2, y0 + (alto_barra - titulo_h) / 2 - 1),
        titulo,
        font=fuente_ui,
        fill=(80, 86, 96)
    )

    inicio_x_num = x0 + padding_interno_x
    inicio_x_codigo = inicio_x_num + ancho_numeracion + 20
    inicio_y = y0 + alto_barra + padding_interno_y

    for i, linea in enumerate(lineas, start=1):
        y = inicio_y + (i - 1) * alto_linea
        draw.text((inicio_x_num, y), str(i), font=fuente_num, fill=color_num_linea)
        draw.text((inicio_x_codigo, y), linea if linea else " ", font=fuente_codigo, fill=color_texto)

    img.save(ruta_salida)

# ==============================
# PROMPTS
# ==============================

def prompt_explicacion(contexto, linea):
    return f"""
Tienes el siguiente temario completo como contexto:

{contexto}

Ahora explica únicamente este punto del temario:

{linea}

Instrucciones:
- Responde en español.
- El lenguaje de referencia es C++.
- Da una explicación teórica y didáctica.
- No pongas ejemplos de código.
- No pongas pseudocódigo.
- No pongas bloques de código.
- Devuelve únicamente la explicación final.
""".strip()

def prompt_codigo(contexto, linea):
    return f"""
Tienes el siguiente temario completo como contexto:

{contexto}

Ahora genera un ejemplo completo en C++ para este punto del temario:

{linea}

Instrucciones:
- Responde en español.
- El ejemplo debe estar en C++.
- Debe ser completo, claro y didáctico.
- Devuelve primero una línea con un título breve.
- Después devuelve únicamente un bloque de código en C++.
- No expliques el código.
- No añadas teoría.
- No añadas texto después del bloque de código.
""".strip()

def prompt_desglose_lineas(contexto, linea, codigo):
    return f"""
Tienes el siguiente temario completo como contexto:

{contexto}

El punto concreto del temario es:

{linea}

Este es el ejemplo principal en C++:

{codigo}

Ahora divide este ejemplo en pasos didácticos basados en rangos de líneas del código.

Devuelve exclusivamente un JSON válido con este formato:

{{
  "pasos": [
    {{
      "titulo": "Paso 1",
      "linea_inicio": 1,
      "linea_fin": 3,
      "explicacion": "Explicación en español de lo que hacen esas líneas."
    }},
    {{
      "titulo": "Paso 2",
      "linea_inicio": 4,
      "linea_fin": 7,
      "explicacion": "Explicación en español de lo que hacen esas líneas."
    }}
  ]
}}

Reglas:
- Usa números de línea reales del código dado.
- Cubre todo el ejemplo.
- Los pasos deben seguir un orden lógico.
- No repitas código dentro de la explicación.
- No escribas nada fuera del JSON.
- No uses markdown.
""".strip()

# ==============================
# PRINCIPAL
# ==============================

def main():
    os.makedirs(CARPETA_IMAGENES, exist_ok=True)

    with open(ARCHIVO_ENTRADA, "r", encoding="utf-8") as f:
        contexto_completo = f.read()

    lineas = [linea.strip() for linea in contexto_completo.splitlines() if linea.strip()]

    with open(ARCHIVO_SALIDA, "a", encoding="utf-8") as salida:
        salida.write("\n# Temario explicado en C++\n\n")
        salida.flush()

        for indice, linea_original in enumerate(lineas, start=1):
            linea = normalizar_linea(linea_original)

            if not linea:
                continue

            print(f"[{indice}/{len(lineas)}] Procesando: {linea}")

            if es_titulo(linea):
                salida.write(f"\n# {linea[:-1].strip()}\n\n")
                salida.flush()
                continue

            # 1. Explicación teórica
            try:
                explicacion = llamada_ollama(
                    MODELO_EXPLICACION,
                    prompt_explicacion(contexto_completo, linea)
                )
            except Exception as e:
                explicacion = f"Error al generar la explicación: {e}"

            time.sleep(PAUSA_ENTRE_PETICIONES)

            # 2. Código principal
            try:
                respuesta_codigo = llamada_ollama(
                    MODELO_CODIGO,
                    prompt_codigo(contexto_completo, linea)
                )
                codigo_principal = extraer_codigo(respuesta_codigo)
            except Exception as e:
                codigo_principal = f"// Error al generar el código: {e}"

            lineas_codigo = codigo_principal.splitlines()
            total_lineas = max(1, len(lineas_codigo))

            time.sleep(PAUSA_ENTRE_PETICIONES)

            # 3. Imagen del código completo
            nombre_base = f"{indice:03d}_{limpiar_nombre_archivo(linea)}"
            ruta_png_principal = os.path.join(CARPETA_IMAGENES, f"{nombre_base}_principal.png")

            try:
                render_codigo_a_png(codigo_principal, ruta_png_principal, titulo="ejemplo.cpp")
                md_codigo_principal = f"![Código principal de {linea}]({ruta_png_principal})"
            except Exception as e:
                md_codigo_principal = f"**Error al generar la imagen principal:** {e}"

            # 4. Desglose por líneas
            try:
                respuesta_desglose = llamada_ollama(
                    MODELO_DESGLOSE,
                    prompt_desglose_lineas(contexto_completo, linea, codigo_principal)
                )
                datos_desglose = extraer_json(respuesta_desglose)
                pasos = normalizar_pasos(datos_desglose, total_lineas)
            except Exception as e:
                pasos = [{
                    "titulo": "Paso 1",
                    "linea_inicio": 1,
                    "linea_fin": total_lineas,
                    "explicacion": f"No se pudo generar el desglose automáticamente: {e}"
                }]

            time.sleep(PAUSA_ENTRE_PETICIONES)

            # 5. Escribir markdown
            salida.write(f"## {linea}\n\n")
            salida.write("### Explicación\n\n")
            salida.write(explicacion + "\n\n")

            salida.write("### Ejemplo completo en C++\n\n")
            salida.write(md_codigo_principal + "\n\n")

            salida.write("### Explicación paso a paso\n\n")

            for j, paso in enumerate(pasos, start=1):
                titulo_paso = paso["titulo"]
                linea_inicio = paso["linea_inicio"]
                linea_fin = paso["linea_fin"]
                explicacion_paso = paso["explicacion"]

                # Texto plano del bloque citado
                fragmento = formatear_fragmento_plano(lineas_codigo, linea_inicio, linea_fin)
                fragmento = escapar_markdown_texto_plano(fragmento)

                # Código acumulado hasta este paso
                codigo_acumulado = "\n".join(lineas_codigo[:linea_fin]).strip()
                if not codigo_acumulado:
                    codigo_acumulado = "// vacío"

                ruta_png_paso = os.path.join(
                    CARPETA_IMAGENES,
                    f"{nombre_base}_paso_{j:02d}.png"
                )

                try:
                    render_codigo_a_png(codigo_acumulado, ruta_png_paso, titulo=f"paso_{j}.cpp")
                    md_codigo_paso = f"![{titulo_paso}]({ruta_png_paso})"
                except Exception as e:
                    md_codigo_paso = f"**Error al generar la imagen del paso {j}:** {e}"

                salida.write(f"#### {titulo_paso}\n\n")
                salida.write(f"Líneas {linea_inicio} a {linea_fin}:\n\n")
                salida.write(fragmento + "\n\n")
                salida.write(md_codigo_paso + "\n\n")
                salida.write(explicacion_paso + "\n\n")

            salida.write("---\n\n")
            salida.flush()

            print(f"  -> Guardado: {linea}")

    print("Proceso completado correctamente.")

if __name__ == "__main__":
    main()