from flask import Flask, render_template, request, jsonify, redirect, url_for, session, g
import sqlite3
import os
from database import init_db, get_db, close_db, verify_password, hash_password
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui_muy_segura_y_larga'
app.config['DATABASE'] = 'clientes.db'

# Inicializar base de datos
with app.app_context():
    init_db()

@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM usuarios WHERE id = ?', (user_id,)
        ).fetchone()

@app.route('/')
def index():
    if g.user:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        
        user = db.execute(
            'SELECT * FROM usuarios WHERE username = ?', (username,)
        ).fetchone()
        
        if user is None or not verify_password(user['password'], password):
            error = 'Usuario o contraseña incorrectos'
        
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))
        
        return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# CRUD de Clientes
@app.route('/clientes')
def clientes():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('clientes.html')

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    db = get_db()
    clientes = db.execute(
        'SELECT * FROM clientes ORDER BY fecha_creacion DESC'
    ).fetchall()
    
    return jsonify([dict(cliente) for cliente in clientes])

@app.route('/api/clientes', methods=['POST'])
def crear_cliente():
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    data = request.get_json()
    
    # Validaciones básicas
    if not data.get('nombre') or not data.get('email'):
        return jsonify({'error': 'Nombre y email son obligatorios'}), 400
    
    db = get_db()
    
    try:
        cursor = db.execute(
            'INSERT INTO clientes (nombre, email, telefono, empresa, direccion) VALUES (?, ?, ?, ?, ?)',
            (data['nombre'], data['email'], data.get('telefono', ''), data.get('empresa', ''), data.get('direccion', ''))
        )
        db.commit()
        return jsonify({'id': cursor.lastrowid, 'message': 'Cliente creado exitosamente'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El email ya existe'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clientes/<int:id>', methods=['PUT'])
def actualizar_cliente(id):
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    data = request.get_json()
    
    # Validaciones básicas
    if not data.get('nombre') or not data.get('email'):
        return jsonify({'error': 'Nombre y email son obligatorios'}), 400
    
    db = get_db()
    
    try:
        db.execute(
            'UPDATE clientes SET nombre = ?, email = ?, telefono = ?, empresa = ?, direccion = ? WHERE id = ?',
            (data['nombre'], data['email'], data.get('telefono', ''), data.get('empresa', ''), data.get('direccion', ''), id)
        )
        db.commit()
        return jsonify({'message': 'Cliente actualizado exitosamente'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El email ya existe'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/clientes/<int:id>', methods=['DELETE'])
def eliminar_cliente(id):
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    db = get_db()
    db.execute('DELETE FROM clientes WHERE id = ?', (id,))
    db.commit()
    return jsonify({'message': 'Cliente eliminado exitosamente'})

# CRUD de Productos
@app.route('/productos')
def productos():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('productos.html')

@app.route('/api/productos', methods=['GET'])
def get_productos():
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    db = get_db()
    productos = db.execute(
        'SELECT * FROM productos ORDER BY fecha_creacion DESC'
    ).fetchall()
    
    return jsonify([dict(producto) for producto in productos])

@app.route('/api/productos', methods=['POST'])
def crear_producto():
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    data = request.get_json()
    
    # Validaciones básicas
    if not data.get('codigo') or not data.get('nombre') or not data.get('precio'):
        return jsonify({'error': 'Código, nombre y precio son obligatorios'}), 400
    
    db = get_db()
    
    try:
        cursor = db.execute(
            'INSERT INTO productos (codigo, nombre, descripcion, precio, stock, categoria) VALUES (?, ?, ?, ?, ?, ?)',
            (data['codigo'], data['nombre'], data.get('descripcion', ''), 
             float(data['precio']), int(data.get('stock', 0)), data.get('categoria', ''))
        )
        db.commit()
        return jsonify({'id': cursor.lastrowid, 'message': 'Producto creado exitosamente'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El código ya existe'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    data = request.get_json()
    
    # Validaciones básicas
    if not data.get('codigo') or not data.get('nombre') or not data.get('precio'):
        return jsonify({'error': 'Código, nombre y precio son obligatorios'}), 400
    
    db = get_db()
    
    try:
        db.execute(
            'UPDATE productos SET codigo = ?, nombre = ?, descripcion = ?, precio = ?, stock = ?, categoria = ? WHERE id = ?',
            (data['codigo'], data['nombre'], data.get('descripcion', ''), 
             float(data['precio']), int(data.get('stock', 0)), data.get('categoria', ''), id)
        )
        db.commit()
        return jsonify({'message': 'Producto actualizado exitosamente'})
    except sqlite3.IntegrityError:
        return jsonify({'error': 'El código ya existe'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    db = get_db()
    db.execute('DELETE FROM productos WHERE id = ?', (id,))
    db.commit()
    return jsonify({'message': 'Producto eliminado exitosamente'})

# CRUD de Pedidos
@app.route('/pedidos')
def pedidos():
    if not g.user:
        return redirect(url_for('login'))
    return render_template('pedidos.html')

@app.route('/api/pedidos', methods=['GET'])
def get_pedidos():
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    db = get_db()
    pedidos = db.execute('''
        SELECT p.*, c.nombre as cliente_nombre 
        FROM pedidos p 
        LEFT JOIN clientes c ON p.cliente_id = c.id 
        ORDER BY p.fecha_creacion DESC
    ''').fetchall()
    
    return jsonify([dict(pedido) for pedido in pedidos])

@app.route('/api/pedidos/<int:id>', methods=['GET'])
def get_pedido(id):
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    db = get_db()
    
    # Obtener pedido
    pedido = db.execute('''
        SELECT p.*, c.nombre as cliente_nombre, c.email as cliente_email 
        FROM pedidos p 
        LEFT JOIN clientes c ON p.cliente_id = c.id 
        WHERE p.id = ?
    ''', (id,)).fetchone()
    
    if not pedido:
        return jsonify({'error': 'Pedido no encontrado'}), 404
    
    # Obtener líneas del pedido
    lineas = db.execute('''
        SELECT lp.*, pr.nombre as producto_nombre, pr.codigo as producto_codigo
        FROM lineas_pedido lp 
        LEFT JOIN productos pr ON lp.producto_id = pr.id 
        WHERE lp.pedido_id = ?
    ''', (id,)).fetchall()
    
    return jsonify({
        'pedido': dict(pedido),
        'lineas': [dict(linea) for linea in lineas]
    })

@app.route('/api/pedidos', methods=['POST'])
def crear_pedido():
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    data = request.get_json()
    
    # Validaciones básicas
    if not data.get('cliente_id') or not data.get('lineas') or len(data.get('lineas', [])) == 0:
        return jsonify({'error': 'Cliente y al menos una línea de pedido son obligatorios'}), 400
    
    db = get_db()
    
    try:
        # Generar número de pedido único
        from datetime import datetime
        numero_pedido = f"PED-{datetime.now().strftime('%Y%m%d')}-{secrets.token_hex(4).upper()}"
        
        # Crear pedido
        cursor = db.execute(
            'INSERT INTO pedidos (cliente_id, numero_pedido, fecha_pedido, estado, notas) VALUES (?, ?, ?, ?, ?)',
            (data['cliente_id'], numero_pedido, data.get('fecha_pedido', datetime.now().date().isoformat()), 
             data.get('estado', 'pendiente'), data.get('notas', ''))
        )
        pedido_id = cursor.lastrowid
        
        # Crear líneas de pedido y calcular total
        total_pedido = 0
        for linea in data['lineas']:
            producto = db.execute('SELECT precio, stock FROM productos WHERE id = ?', (linea['producto_id'],)).fetchone()
            if not producto:
                raise Exception(f"Producto con ID {linea['producto_id']} no encontrado")
            
            subtotal = float(producto['precio']) * int(linea['cantidad'])
            total_pedido += subtotal
            
            db.execute(
                'INSERT INTO lineas_pedido (pedido_id, producto_id, cantidad, precio_unitario, subtotal) VALUES (?, ?, ?, ?, ?)',
                (pedido_id, linea['producto_id'], linea['cantidad'], float(producto['precio']), subtotal)
            )
            
            # Actualizar stock
            nuevo_stock = producto['stock'] - linea['cantidad']
            db.execute('UPDATE productos SET stock = ? WHERE id = ?', (nuevo_stock, linea['producto_id']))
        
        # Actualizar total del pedido
        db.execute('UPDATE pedidos SET total = ? WHERE id = ?', (total_pedido, pedido_id))
        
        db.commit()
        return jsonify({'id': pedido_id, 'numero_pedido': numero_pedido, 'message': 'Pedido creado exitosamente'})
    
    except Exception as e:
        db.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/pedidos/<int:id>/estado', methods=['PUT'])
def actualizar_estado_pedido(id):
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    data = request.get_json()
    
    if not data.get('estado'):
        return jsonify({'error': 'Estado es obligatorio'}), 400
    
    db = get_db()
    
    try:
        db.execute(
            'UPDATE pedidos SET estado = ? WHERE id = ?',
            (data['estado'], id)
        )
        db.commit()
        return jsonify({'message': 'Estado del pedido actualizado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/pedidos/<int:id>', methods=['DELETE'])
def eliminar_pedido(id):
    if not g.user:
        return jsonify({'error': 'No autorizado'}), 401
    
    db = get_db()
    
    try:
        # Primero eliminar las líneas del pedido
        db.execute('DELETE FROM lineas_pedido WHERE pedido_id = ?', (id,))
        # Luego eliminar el pedido
        db.execute('DELETE FROM pedidos WHERE id = ?', (id,))
        db.commit()
        return jsonify({'message': 'Pedido eliminado exitosamente'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
