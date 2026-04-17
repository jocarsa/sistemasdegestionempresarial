CREATE TABLE "usuarios" (
	"id"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	"usuario"	TEXT,
	"contrasena"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO usuarios VALUES(
	NULL,
	'Jose Vicente',
	'Carratalá Sanchis',
	'info@jocarsa.com',
	'jocarsa',
	'jocarsa'
);
