import requests

archivo = open("tareas.txt","r")

lineas = archivo.readlines()

for linea in lineas:
  print(linea)
  response = requests.post(
      "http://localhost:11434/api/generate",
      json={
          "model": "qwen2.5:3b-instruct",
          "prompt": linea,
          "stream": False
      }
  )
  print(response.json()["response"])
  
archivo.close()