Primero descargamos desde la web

https://www.odoo.com/es_ES/page/download

Comprobamos si el servicio está operativo:

sudo systemctl status odoo


Arrancar el el servicio

sudo systemctl start odoo // Ponemos esto para comprobar si arranca

Si falla un paquete de XML (y no arranca o no se instala):

sudo apt update
sudo apt install -y python3-lxml python3-lxml-html-clean
sudo systemctl restart odoo
sudo systemctl status odoo


