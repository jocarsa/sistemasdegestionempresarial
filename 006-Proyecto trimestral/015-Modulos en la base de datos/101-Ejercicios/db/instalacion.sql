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

CREATE TABLE "clientes" (
	"id"	INTEGER,
	"nombre"	TEXT,
	"apellidos"	TEXT,
	"email"	TEXT,
	"telefono"	TEXT,
	"direccion"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);

INSERT INTO clientes (nombre, apellidos, email, telefono, direccion) VALUES
('Carlos', 'Martinez Lopez', 'carlos.martinez@example.com', '612345001', 'Calle Mayor 12, Madrid'),
('Laura', 'Sanchez Ruiz', 'laura.sanchez@example.com', '612345002', 'Avenida del Puerto 45, Valencia'),
('Miguel', 'Gomez Perez', 'miguel.gomez@example.com', '612345003', 'Calle Colon 8, Valencia'),
('Ana', 'Fernandez Torres', 'ana.fernandez@example.com', '612345004', 'Plaza Espana 3, Sevilla'),
('David', 'Hernandez Molina', 'david.hernandez@example.com', '612345005', 'Calle Gran Via 102, Madrid'),
('Maria', 'Lopez Navarro', 'maria.lopez@example.com', '612345006', 'Calle Serreria 21, Valencia'),
('Javier', 'Ruiz Castillo', 'javier.ruiz@example.com', '612345007', 'Avenida Andalucia 14, Malaga'),
('Elena', 'Perez Romero', 'elena.perez@example.com', '612345008', 'Calle Alfonso X 6, Murcia'),
('Pablo', 'Moreno Diaz', 'pablo.moreno@example.com', '612345009', 'Calle Real 19, Granada'),
('Cristina', 'Vidal Ortega', 'cristina.vidal@example.com', '612345010', 'Avenida Blasco Ibanez 55, Valencia'),
('Sergio', 'Iglesias Soto', 'sergio.iglesias@example.com', '612345011', 'Calle Larios 7, Malaga'),
('Raquel', 'Cano Flores', 'raquel.cano@example.com', '612345012', 'Plaza del Ayuntamiento 1, Valencia'),
('Alberto', 'Mendez Cruz', 'alberto.mendez@example.com', '612345013', 'Calle San Vicente 30, Alicante'),
('Isabel', 'Ramos Gil', 'isabel.ramos@example.com', '612345014', 'Calle Huertas 18, Madrid'),
('Antonio', 'Vazquez Leon', 'antonio.vazquez@example.com', '612345015', 'Avenida Europa 9, Toledo'),
('Natalia', 'Prieto Marcos', 'natalia.prieto@example.com', '612345016', 'Calle Doctor Fleming 22, Castellon'),
('Francisco', 'Dominguez Pardo', 'francisco.dominguez@example.com', '612345017', 'Calle Nueva 5, Salamanca'),
('Beatriz', 'Nieto Campos', 'beatriz.nieto@example.com', '612345018', 'Avenida de la Paz 33, Logrono'),
('Ruben', 'Calvo Herrera', 'ruben.calvo@example.com', '612345019', 'Calle Mayor 44, Zaragoza'),
('Silvia', 'Morales Peiro', 'silvia.morales@example.com', '612345020', 'Calle San Juan 10, Elche');
