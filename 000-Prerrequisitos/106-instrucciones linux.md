# Instalar apache2

```
sudo apt install apache2
```

# Carpeta de publicación

```
/var/www/html
```

# La carpeta de publicación está protegida contra escritura

Cambia de directorio a la carpeta /var/www/html

```
cd /var/www/html
```

# Te creas una carpeta para ti

```
sudo mkdir dam
```
sudo = el super usuario hace algo
mkdir = make directory = crear directorio
dam = el nombre del directorio

# Ahora le tienes que dar permisos

```
sudo chmod 777 -R dam
```
sudo = el superusuario hace algo
chmod = cambia los permisos
777 = codigo de los permisos otorgados (muy permisivo)
-R = recursivo a todas las carpetas contenidas
da = la carpeta afectada

# Y ahora ya puedes poner lo que quieras

Pon tu proyecto dentro de la carpeta

# En el navegador

http://localhost/dam
