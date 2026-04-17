CREATE DATABASE pruebamysqlphp;
USE pruebamysqlphp;

CREATE TABLE clientes (
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    apellidos VARCHAR(255),
    email VARCHAR(255),
    direccion VARCHAR(255)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;