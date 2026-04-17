PRAGMA foreign_keys = ON;

-- =========================================================
-- 1) PRODUCTOS
-- =========================================================
CREATE TABLE IF NOT EXISTS productos (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre      TEXT    NOT NULL,
  descripcion TEXT,
  precio      REAL    NOT NULL CHECK(precio >= 0),
  iva         REAL    NOT NULL DEFAULT 0.21 CHECK(iva >= 0),
  activo      INTEGER NOT NULL DEFAULT 1 CHECK(activo IN (0,1))
);

INSERT INTO productos (id, nombre, descripcion, precio, iva, activo) VALUES
(1,  'Cuaderno A5',        'Cuaderno de tapa dura A5, 120 páginas',          4.90, 0.21, 1),
(2,  'Bolígrafo gel',      'Bolígrafo tinta gel azul 0.5mm',                 1.50, 0.21, 1),
(3,  'Pendrive 32GB',      'Memoria USB 3.0 32GB',                           9.95, 0.21, 1),
(4,  'Ratón inalámbrico',  'Ratón óptico 2.4GHz',                           14.90, 0.21, 1),
(5,  'Teclado compacto',   'Teclado USB compacto español',                  19.90, 0.21, 1),
(6,  'Auriculares',        'Auriculares con micrófono',                     12.50, 0.21, 1),
(7,  'Cable HDMI 2m',      'Cable HDMI alta velocidad 2 metros',             6.80, 0.21, 1),
(8,  'Soporte portátil',   'Soporte plegable para portátil',                17.90, 0.21, 1),
(9,  'Mochila',            'Mochila urbana 15.6"',                          29.00, 0.21, 1),
(10, 'Agenda semanal',     'Agenda 2026 semanal, tamaño A5',                11.90, 0.21, 1);

-- =========================================================
-- 2) PEDIDOS
--    (referencia a clientes.id de tu exportación)
-- =========================================================
CREATE TABLE IF NOT EXISTS pedidos (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  cliente_id INTEGER NOT NULL,
  fecha      TEXT    NOT NULL, -- 'YYYY-MM-DD'
  estado     TEXT    NOT NULL DEFAULT 'pendiente'
             CHECK(estado IN ('pendiente','pagado','enviado','cancelado')),
  subtotal   REAL    NOT NULL DEFAULT 0 CHECK(subtotal >= 0),
  iva_total  REAL    NOT NULL DEFAULT 0 CHECK(iva_total >= 0),
  total      REAL    NOT NULL DEFAULT 0 CHECK(total >= 0),
  FOREIGN KEY (cliente_id) REFERENCES clientes(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

INSERT INTO pedidos (id, cliente_id, fecha, estado, subtotal, iva_total, total) VALUES
(1,  2,  '2026-02-10', 'pendiente', 34.10, 7.16, 41.26),
(2,  5,  '2026-02-12', 'pagado',    33.50, 7.04, 40.54),
(3,  10, '2026-02-14', 'enviado',   47.30, 9.93, 57.23),
(4,  1,  '2026-02-18', 'pagado',    46.90, 9.85, 56.75),
(5,  14, '2026-02-20', 'cancelado', 17.85, 3.75, 21.60);

-- =========================================================
-- 3) LINEAS DE PEDIDO
-- =========================================================
CREATE TABLE IF NOT EXISTS lineas_pedido (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  pedido_id      INTEGER NOT NULL,
  producto_id    INTEGER NOT NULL,
  cantidad       INTEGER NOT NULL CHECK(cantidad > 0),
  precio_unitario REAL   NOT NULL CHECK(precio_unitario >= 0),
  descuento      REAL    NOT NULL DEFAULT 0 CHECK(descuento >= 0), -- importe (no %)
  total_linea    REAL    NOT NULL CHECK(total_linea >= 0),
  FOREIGN KEY (pedido_id)   REFERENCES pedidos(id)   ON UPDATE CASCADE ON DELETE CASCADE,
  FOREIGN KEY (producto_id) REFERENCES productos(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

INSERT INTO lineas_pedido (id, pedido_id, producto_id, cantidad, precio_unitario, descuento, total_linea) VALUES
(1,  1,  1,  3,  4.90, 0.00, 14.70),
(2,  1,  2,  5,  1.50, 0.00,  7.50),
(3,  1, 10,  1, 11.90, 0.00, 11.90),

(4,  2,  3,  2,  9.95, 0.00, 19.90),
(5,  2,  7,  2,  6.80, 0.00, 13.60),

(6,  3,  4,  1, 14.90, 0.00, 14.90),
(7,  3,  5,  1, 19.90, 0.00, 19.90),
(8,  3,  6,  1, 12.50, 0.00, 12.50),

(9,  4,  9,  1, 29.00, 0.00, 29.00),
(10, 4,  8,  1, 17.90, 0.00, 17.90),

(11, 5,  1,  1,  4.90, 0.00,  4.90),
(12, 5,  2,  2,  1.50, 0.00,  3.00),
(13, 5,  3,  1,  9.95, 0.00,  9.95);

-- =========================================================
-- 4) FACTURAS
--    (1 factura por pedido; pedido_id UNIQUE)
-- =========================================================
CREATE TABLE IF NOT EXISTS facturas (
  id             INTEGER PRIMARY KEY AUTOINCREMENT,
  pedido_id      INTEGER NOT NULL UNIQUE,
  numero         TEXT    NOT NULL UNIQUE,
  fecha_emision  TEXT    NOT NULL, -- 'YYYY-MM-DD'
  base_imponible REAL    NOT NULL CHECK(base_imponible >= 0),
  iva_total      REAL    NOT NULL CHECK(iva_total >= 0),
  total          REAL    NOT NULL CHECK(total >= 0),
  pagada         INTEGER NOT NULL DEFAULT 0 CHECK(pagada IN (0,1)),
  FOREIGN KEY (pedido_id) REFERENCES pedidos(id) ON UPDATE CASCADE ON DELETE RESTRICT
);

INSERT INTO facturas (id, pedido_id, numero, fecha_emision, base_imponible, iva_total, total, pagada) VALUES
(1, 2, 'F-2026-0001', '2026-02-13', 33.50, 7.04, 40.54, 1),
(2, 3, 'F-2026-0002', '2026-02-15', 47.30, 9.93, 57.23, 1),
(3, 4, 'F-2026-0003', '2026-02-25', 46.90, 9.85, 56.75, 1);