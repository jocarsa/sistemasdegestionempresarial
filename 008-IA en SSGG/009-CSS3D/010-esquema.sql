-- ============================================
-- Crear base de datos SQLite: empresa.db
-- ============================================

-- En SQLite no se usa CREATE DATABASE
-- Basta con abrir el archivo:
-- sqlite3 empresa.db

-- ============================================
-- Crear tabla clientes
-- ============================================

CREATE TABLE clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellidos TEXT NOT NULL,
    empresa TEXT,
    telefono TEXT,
    email TEXT,
    direccion TEXT,
    ciudad TEXT,
    provincia TEXT,
    codigo_postal TEXT,
    fecha_alta DATE,
    saldo REAL
);

-- ============================================
-- Insertar clientes ficticios
-- ============================================

INSERT INTO clientes (
    nombre,
    apellidos,
    empresa,
    telefono,
    email,
    direccion,
    ciudad,
    provincia,
    codigo_postal,
    fecha_alta,
    saldo
) VALUES
('Carlos', 'Martínez López', 'Tecnologías Levante SL', '612345678', 'carlos.martinez@example.com', 'Calle Mayor 12', 'Valencia', 'Valencia', '46001', '2025-01-15', 1250.50),

('Laura', 'García Sánchez', 'Distribuciones Mediterráneo', '623456789', 'laura.garcia@example.com', 'Avenida del Puerto 45', 'Valencia', 'Valencia', '46011', '2025-02-03', 890.00),

('Miguel', 'Fernández Ruiz', 'Construcciones Ruiz', '634567890', 'miguel.fernandez@example.com', 'Calle San Vicente 88', 'Alicante', 'Alicante', '03002', '2025-02-10', 2450.75),

('Ana', 'Torres Gómez', 'Eventos Torres', '645678901', 'ana.torres@example.com', 'Plaza España 3', 'Castellón', 'Castellón', '12001', '2025-02-18', 340.20),

('Javier', 'Navarro Pérez', 'Navarro Informática', '656789012', 'javier.navarro@example.com', 'Calle Colón 21', 'Madrid', 'Madrid', '28001', '2025-03-01', 5100.00),

('Marta', 'Romero Díaz', 'Romero Diseño', '667890123', 'marta.romero@example.com', 'Calle Luna 7', 'Sevilla', 'Sevilla', '41001', '2025-03-08', 760.40),

('Sergio', 'Ortega Molina', 'Ortega Consulting', '678901234', 'sergio.ortega@example.com', 'Avenida Andalucía 55', 'Málaga', 'Málaga', '29003', '2025-03-12', 1320.90),

('Elena', 'Castro Vidal', 'Castro Arquitectura', '689012345', 'elena.castro@example.com', 'Calle del Mar 14', 'Barcelona', 'Barcelona', '08002', '2025-03-20', 2890.00),

('Raúl', 'Jiménez Herrera', 'Jiménez Logistics', '690123456', 'raul.jimenez@example.com', 'Camino Real 19', 'Bilbao', 'Vizcaya', '48001', '2025-04-02', 980.60),

('Patricia', 'Santos Gil', 'Santos Marketing', '601234567', 'patricia.santos@example.com', 'Paseo Central 101', 'Zaragoza', 'Zaragoza', '50004', '2025-04-10', 4500.30),

('David', 'Mendoza Cano', 'Mendoza Solutions', '602345678', 'david.mendoza@example.com', 'Calle Jardines 8', 'Murcia', 'Murcia', '30001', '2025-04-14', 670.00),

('Lucía', 'Vega Moreno', 'Vega Publicidad', '603456789', 'lucia.vega@example.com', 'Avenida Libertad 33', 'Granada', 'Granada', '18005', '2025-04-20', 1540.80),

('Andrés', 'Peña Rubio', 'Peña Automoción', '604567890', 'andres.pena@example.com', 'Calle Cervantes 44', 'Toledo', 'Toledo', '45003', '2025-04-25', 3750.10),

('Cristina', 'Lorenzo Serra', 'Lorenzo Moda', '605678901', 'cristina.lorenzo@example.com', 'Calle Pintor Sorolla 6', 'Valencia', 'Valencia', '46002', '2025-05-01', 2100.00),

('Fernando', 'Ibáñez Soler', 'Ibáñez Industrial', '606789012', 'fernando.ibanez@example.com', 'Polígono Norte 18', 'Valladolid', 'Valladolid', '47001', '2025-05-08', 8120.45);

-- ============================================
-- Consultar clientes
-- ============================================

SELECT * FROM clientes;