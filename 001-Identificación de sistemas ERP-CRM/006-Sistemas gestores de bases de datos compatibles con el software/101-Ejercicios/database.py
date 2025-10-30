import sqlite3
from flask import g
import hashlib
import secrets

DATABASE = 'clientes.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def hash_password(password):
    """Encripta la contraseña usando SHA-256 con salt"""
    salt = secrets.token_hex(16)
    return hashlib.sha256((password + salt).encode()).hexdigest() + ':' + salt

def verify_password(stored_password, provided_password):
    """Verifica si la contraseña proporcionada coincide con la almacenada"""
    if ':' not in stored_password:
        return False
    hashed, salt = stored_password.split(':')
    return hashed == hashlib.sha256((provided_password + salt).encode()).hexdigest()

def init_db():
    db = get_db()
    
    # Crear tabla de usuarios si no existe
    db.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            nombre TEXT,
            email TEXT,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Crear tabla de clientes si no existe
    db.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            telefono TEXT,
            empresa TEXT,
            direccion TEXT,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Crear tabla de productos si no existe
    db.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT UNIQUE NOT NULL,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio DECIMAL(10,2) NOT NULL,
            stock INTEGER DEFAULT 0,
            categoria TEXT,
            activo BOOLEAN DEFAULT 1,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Crear tabla de pedidos si no existe
    db.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER NOT NULL,
            numero_pedido TEXT UNIQUE NOT NULL,
            fecha_pedido DATE NOT NULL,
            estado TEXT DEFAULT 'pendiente',
            total DECIMAL(10,2) DEFAULT 0,
            notas TEXT,
            fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cliente_id) REFERENCES clientes (id)
        )
    ''')
    
    # Crear tabla de lineas_pedido si no existe
    db.execute('''
        CREATE TABLE IF NOT EXISTS lineas_pedido (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pedido_id INTEGER NOT NULL,
            producto_id INTEGER NOT NULL,
            cantidad INTEGER NOT NULL,
            precio_unitario DECIMAL(10,2) NOT NULL,
            subtotal DECIMAL(10,2) NOT NULL,
            FOREIGN KEY (pedido_id) REFERENCES pedidos (id),
            FOREIGN KEY (producto_id) REFERENCES productos (id)
        )
    ''')
    
    # Insertar usuario por defecto si no existe
    cursor = db.execute('SELECT id FROM usuarios WHERE username = ?', ('jocarsa',))
    if cursor.fetchone() is None:
        hashed_password = hash_password('jocarsa')
        db.execute(
            'INSERT INTO usuarios (username, password, nombre, email) VALUES (?, ?, ?, ?)',
            ('jocarsa', hashed_password, 'Usuario Administrador', 'admin@sistema.com')
        )
    
    # Insertar algunos productos de ejemplo si no existen
    cursor = db.execute('SELECT id FROM productos WHERE codigo = ?', ('PROD001',))
    if cursor.fetchone() is None:
        productos_ejemplo = [
            ('PROD001', 'Laptop Gaming', 'Laptop para gaming de alta gama', 1200.00, 10, 'Tecnología'),
            ('PROD002', 'Mouse Inalámbrico', 'Mouse ergonómico inalámbrico', 45.50, 25, 'Tecnología'),
            ('PROD003', 'Teclado Mecánico', 'Teclado mecánico RGB', 89.99, 15, 'Tecnología'),
            ('PROD004', 'Monitor 24"', 'Monitor Full HD 24 pulgadas', 199.99, 8, 'Tecnología'),
            ('PROD005', 'Silla Oficina', 'Silla ergonómica para oficina', 299.00, 5, 'Mobiliario')
        ]
        
        for producto in productos_ejemplo:
            db.execute(
                'INSERT INTO productos (codigo, nombre, descripcion, precio, stock, categoria) VALUES (?, ?, ?, ?, ?, ?)',
                producto
            )
    
    db.commit()

def close_db(e=None):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
