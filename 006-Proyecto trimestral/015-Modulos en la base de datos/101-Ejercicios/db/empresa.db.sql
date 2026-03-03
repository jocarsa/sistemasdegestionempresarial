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
CREATE TABLE IF NOT EXISTS "productos" (
	"id"	INTEGER,
	"nombre"	TEXT NOT NULL,
	"descripcion"	TEXT,
	"precio"	REAL NOT NULL CHECK("precio" >= 0),
	"iva"	REAL NOT NULL DEFAULT 0.21 CHECK("iva" >= 0),
	"activo"	INTEGER NOT NULL DEFAULT 1 CHECK("activo" IN (0, 1)),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "pedidos" (
	"id"	INTEGER,
	"cliente_id"	INTEGER NOT NULL,
	"fecha"	TEXT NOT NULL,
	"estado"	TEXT NOT NULL DEFAULT 'pendiente' CHECK("estado" IN ('pendiente', 'pagado', 'enviado', 'cancelado')),
	"subtotal"	REAL NOT NULL DEFAULT 0 CHECK("subtotal" >= 0),
	"iva_total"	REAL NOT NULL DEFAULT 0 CHECK("iva_total" >= 0),
	"total"	REAL NOT NULL DEFAULT 0 CHECK("total" >= 0),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("cliente_id") REFERENCES "clientes"("id") ON UPDATE CASCADE ON DELETE RESTRICT
);
CREATE TABLE IF NOT EXISTS "lineas_pedido" (
	"id"	INTEGER,
	"pedido_id"	INTEGER NOT NULL,
	"producto_id"	INTEGER NOT NULL,
	"cantidad"	INTEGER NOT NULL CHECK("cantidad" > 0),
	"precio_unitario"	REAL NOT NULL CHECK("precio_unitario" >= 0),
	"descuento"	REAL NOT NULL DEFAULT 0 CHECK("descuento" >= 0),
	"total_linea"	REAL NOT NULL CHECK("total_linea" >= 0),
	FOREIGN KEY("producto_id") REFERENCES "productos"("id") ON UPDATE CASCADE ON DELETE RESTRICT,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("pedido_id") REFERENCES "pedidos"("id") ON UPDATE CASCADE ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "facturas" (
	"id"	INTEGER,
	"pedido_id"	INTEGER NOT NULL UNIQUE,
	"numero"	TEXT NOT NULL UNIQUE,
	"fecha_emision"	TEXT NOT NULL,
	"base_imponible"	REAL NOT NULL CHECK("base_imponible" >= 0),
	"iva_total"	REAL NOT NULL CHECK("iva_total" >= 0),
	"total"	REAL NOT NULL CHECK("total" >= 0),
	"pagada"	INTEGER NOT NULL DEFAULT 0 CHECK("pagada" IN (0, 1)),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("pedido_id") REFERENCES "pedidos"("id") ON UPDATE CASCADE ON DELETE RESTRICT
);
CREATE TABLE IF NOT EXISTS "modulos" (
	"id"	INTEGER,
	"slug"	TEXT NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"orden"	INTEGER NOT NULL DEFAULT 0,
	"activo"	INTEGER NOT NULL DEFAULT 1 CHECK("activo" IN (0, 1)),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "modulo_entidades" (
	"id"	INTEGER,
	"modulo_id"	INTEGER NOT NULL,
	"entidad"	TEXT NOT NULL,
	"orden"	INTEGER NOT NULL DEFAULT 0,
	UNIQUE("modulo_id","entidad"),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("modulo_id") REFERENCES "modulos"("id") ON DELETE CASCADE
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
INSERT INTO "productos" VALUES (1,'Cuaderno A5','Cuaderno de tapa dura A5, 120 páginas',4.9,0.21,1);
INSERT INTO "productos" VALUES (2,'Bolígrafo gel','Bolígrafo tinta gel azul 0.5mm',1.5,0.21,1);
INSERT INTO "productos" VALUES (3,'Pendrive 32GB','Memoria USB 3.0 32GB',9.95,0.21,1);
INSERT INTO "productos" VALUES (4,'Ratón inalámbrico','Ratón óptico 2.4GHz',14.9,0.21,1);
INSERT INTO "productos" VALUES (5,'Teclado compacto','Teclado USB compacto español',19.9,0.21,1);
INSERT INTO "productos" VALUES (6,'Auriculares','Auriculares con micrófono',12.5,0.21,1);
INSERT INTO "productos" VALUES (7,'Cable HDMI 2m','Cable HDMI alta velocidad 2 metros',6.8,0.21,1);
INSERT INTO "productos" VALUES (8,'Soporte portátil','Soporte plegable para portátil',17.9,0.21,1);
INSERT INTO "productos" VALUES (9,'Mochila','Mochila urbana 15.6"',29.0,0.21,1);
INSERT INTO "productos" VALUES (10,'Agenda semanal','Agenda 2026 semanal, tamaño A5',11.9,0.21,1);
INSERT INTO "pedidos" VALUES (1,2,'2026-02-10','pendiente',34.1,7.16,41.26);
INSERT INTO "pedidos" VALUES (2,5,'2026-02-12','pagado',33.5,7.04,40.54);
INSERT INTO "pedidos" VALUES (3,10,'2026-02-14','enviado',47.3,9.93,57.23);
INSERT INTO "pedidos" VALUES (4,1,'2026-02-18','pagado',46.9,9.85,56.75);
INSERT INTO "pedidos" VALUES (5,14,'2026-02-20','cancelado',17.85,3.75,21.6);
INSERT INTO "lineas_pedido" VALUES (1,1,1,3,4.9,0.0,14.7);
INSERT INTO "lineas_pedido" VALUES (2,1,2,5,1.5,0.0,7.5);
INSERT INTO "lineas_pedido" VALUES (3,1,10,1,11.9,0.0,11.9);
INSERT INTO "lineas_pedido" VALUES (4,2,3,2,9.95,0.0,19.9);
INSERT INTO "lineas_pedido" VALUES (5,2,7,2,6.8,0.0,13.6);
INSERT INTO "lineas_pedido" VALUES (6,3,4,1,14.9,0.0,14.9);
INSERT INTO "lineas_pedido" VALUES (7,3,5,1,19.9,0.0,19.9);
INSERT INTO "lineas_pedido" VALUES (8,3,6,1,12.5,0.0,12.5);
INSERT INTO "lineas_pedido" VALUES (9,4,9,1,29.0,0.0,29.0);
INSERT INTO "lineas_pedido" VALUES (10,4,8,1,17.9,0.0,17.9);
INSERT INTO "lineas_pedido" VALUES (11,5,1,1,4.9,0.0,4.9);
INSERT INTO "lineas_pedido" VALUES (12,5,2,2,1.5,0.0,3.0);
INSERT INTO "lineas_pedido" VALUES (13,5,3,1,9.95,0.0,9.95);
INSERT INTO "facturas" VALUES (1,2,'F-2026-0001','2026-02-13',33.5,7.04,40.54,1);
INSERT INTO "facturas" VALUES (2,3,'F-2026-0002','2026-02-15',47.3,9.93,57.23,1);
INSERT INTO "facturas" VALUES (3,4,'F-2026-0003','2026-02-25',46.9,9.85,56.75,1);
INSERT INTO "modulos" VALUES (1,'ventas','Ventas',10,1);
INSERT INTO "modulos" VALUES (2,'produccion','Producción',20,1);
INSERT INTO "modulos" VALUES (3,'facturacion','Facturación',30,1);
INSERT INTO "modulo_entidades" VALUES (1,1,'clientes',10);
INSERT INTO "modulo_entidades" VALUES (2,1,'productos',20);
INSERT INTO "modulo_entidades" VALUES (3,1,'pedidos',30);
INSERT INTO "modulo_entidades" VALUES (4,2,'productos',10);
INSERT INTO "modulo_entidades" VALUES (5,3,'clientes',10);
INSERT INTO "modulo_entidades" VALUES (6,3,'facturas',20);
INSERT INTO "modulo_entidades" VALUES (7,3,'pedidos',30);
COMMIT;
