Navegamos hasta la carpeta del proyecto
Abrimos terminal
Y ponemos los siguientes comandos:

// Creamos un entorno virtual de python
python3 -m venv .venv
// Activamos el entorno virtual
source .venv/bin/activate
// Actualizamos lista de paquetes
pip install --upgrade pip
// Instalamos estos paquetes necesarios
pip install torch transformers datasets peft trl accelerate bitsandbytes sentencepiece
