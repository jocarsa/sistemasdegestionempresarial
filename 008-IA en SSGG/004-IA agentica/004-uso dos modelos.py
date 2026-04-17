import requests

archivo = open("tareas2.txt","r")

lineas = archivo.readlines()

for linea in lineas:
  print(linea)
  response = requests.post(
      "http://localhost:11434/api/generate",
      json={
          "model": "qwen2.5:3b-instruct",
          "prompt": "Dime que es: "+linea,
          "stream": False
      }
  )
  print(response.json()["response"])
  response = requests.post(
      "http://localhost:11434/api/generate",
      json={
          "model": "qwen2.5-coder:7b",
          "prompt": "Ponme un ejemplo de código de: "+linea,
          "stream": False
      }
  )
  print(response.json()["response"])
  
archivo.close()