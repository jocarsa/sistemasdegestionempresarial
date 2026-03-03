BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "usuarios" (
	"id"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	"usuario"	TEXT,
	"contrasena"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "clientes" (
	"id"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	"telefono"	TEXT,
	"direccion"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "usuarios" VALUES (1,'Jose Vicente','Carratalá Sanchis','info@jocarsa.com','jocarsa','jocarsa');
INSERT INTO "clientes" VALUES (1,'Carlos','Martinez Lopez','carlos.martinez@example.com','612345001','Calle Mayor 12, Madrid');
INSERT INTO "clientes" VALUES (2,'Laura','Sanchez Ruiz','laura.sanchez@example.com','612345002','Avenida del Puerto 45, Valencia');
INSERT INTO "clientes" VALUES (3,'Miguel','Gomez Perez','miguel.gomez@example.com','612345003','Calle Colon 8, Valencia');
INSERT INTO "clientes" VALUES (4,'Ana','Fernandez Torres','ana.fernandez@example.com','612345004','Plaza Espana 3, Sevilla');
INSERT INTO "clientes" VALUES (5,'David','Hernandez Molina','david.hernandez@example.com','612345005','Calle Gran Via 102, Madrid');
INSERT INTO "clientes" VALUES (6,'Maria','Lopez Navarro','maria.lopez@example.com','612345006','Calle Serreria 21, Valencia');
INSERT INTO "clientes" VALUES (7,'Javier','Ruiz Castillo','javier.ruiz@example.com','612345007','Avenida Andalucia 14, Malaga');
INSERT INTO "clientes" VALUES (8,'Elena','Perez Romero','elena.perez@example.com','612345008','Calle Alfonso X 6, Murcia');
INSERT INTO "clientes" VALUES (9,'Pablo','Moreno Diaz','pablo.moreno@example.com','612345009','Calle Real 19, Granada');
INSERT INTO "clientes" VALUES (10,'Cristina','Vidal Ortega','cristina.vidal@example.com','612345010','Avenida Blasco Ibanez 55, Valencia');
INSERT INTO "clientes" VALUES (11,'Sergio','Iglesias Soto','sergio.iglesias@example.com','612345011','Calle Larios 7, Malaga');
INSERT INTO "clientes" VALUES (12,'Raquel','Cano Flores','raquel.cano@example.com','612345012','Plaza del Ayuntamiento 1, Valencia');
INSERT INTO "clientes" VALUES (13,'Alberto','Mendez Cruz','alberto.mendez@example.com','612345013','Calle San Vicente 30, Alicante');
INSERT INTO "clientes" VALUES (14,'Isabel','Ramos Gil','isabel.ramos@example.com','612345014','Calle Huertas 18, Madrid');
INSERT INTO "clientes" VALUES (15,'Antonio','Vazquez Leon','antonio.vazquez@example.com','612345015','Avenida Europa 9, Toledo');
INSERT INTO "clientes" VALUES (16,'Natalia','Prieto Marcos','natalia.prieto@example.com','612345016','Calle Doctor Fleming 22, Castellon');
INSERT INTO "clientes" VALUES (17,'Francisco','Dominguez Pardo','francisco.dominguez@example.com','612345017','Calle Nueva 5, Salamanca');
INSERT INTO "clientes" VALUES (18,'Beatriz','Nieto Campos','beatriz.nieto@example.com','612345018','Avenida de la Paz 33, Logrono');
INSERT INTO "clientes" VALUES (19,'Ruben','Calvo Herrera','ruben.calvo@example.com','612345019','Calle Mayor 44, Zaragoza');
INSERT INTO "clientes" VALUES (20,'Silvia','Morales Peiro','silvia.morales@example.com','612345020','Calle San Juan 10, Elche');
COMMIT;
