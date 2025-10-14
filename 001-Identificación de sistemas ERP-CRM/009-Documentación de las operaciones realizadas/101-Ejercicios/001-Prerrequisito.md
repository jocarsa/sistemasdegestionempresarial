1.-Instalar DBBrowser:
https://sqlitebrowser.org/ (Windows)
O bien desde la tienda de aplicaciones (sqlitebrowser) (Linux)

2.-Crear nueva base de datos

3.-La  guardais como empresa.db

4.-CREATE TABLE "clientes" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);

5.-CREATE TABLE "productos" (
	"Identificador"	INTEGER,
	"nombre"	TEXT,
	"descripcion"	TEXT,
	"precio"	TEXT,
	PRIMARY KEY("Identificador" AUTOINCREMENT)
);

