// Funciones para la gestión de productos
document.addEventListener('DOMContentLoaded', function() {
    console.log('Módulo de productos cargado');
    cargarProductos();
    
    // Configurar el formulario de producto
    const formProducto = document.getElementById('form-producto');
    if (formProducto) {
        formProducto.addEventListener('submit', function(event) {
            event.preventDefault();
            console.log('Formulario de producto enviado');
            guardarProducto();
        });
    }
});

// Cargar lista de productos
function cargarProductos() {
    console.log('Iniciando carga de productos...');
    
    fetch('/api/productos')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor: ' + response.status);
            }
            return response.json();
        })
        .then(function(productos) {
            console.log('Productos cargados:', productos);
            const cuerpoTabla = document.getElementById('cuerpo-tabla');
            
            if (!cuerpoTabla) {
                console.error('No se encontró el elemento cuerpo-tabla');
                return;
            }
            
            cuerpoTabla.innerHTML = '';
            
            if (productos.length === 0) {
                const fila = document.createElement('tr');
                fila.innerHTML = '<td colspan="7" style="text-align: center; padding: 2rem;">No hay productos registrados</td>';
                cuerpoTabla.appendChild(fila);
                return;
            }
            
            productos.forEach(function(producto) {
                const fila = document.createElement('tr');
                fila.innerHTML = `
                    <td>${escapeHtml(producto.codigo)}</td>
                    <td>${escapeHtml(producto.nombre)}</td>
                    <td>€${parseFloat(producto.precio).toFixed(2)}</td>
                    <td>${producto.stock}</td>
                    <td>${producto.categoria ? escapeHtml(producto.categoria) : '-'}</td>
                    <td>
                        <span class="estado-badge ${producto.activo ? 'activo' : 'inactivo'}">
                            ${producto.activo ? 'Activo' : 'Inactivo'}
                        </span>
                    </td>
                    <td>
                        <div class="btn-actions">
                            <button class="btn-edit" onclick="editarProducto(${producto.id})">Editar</button>
                            <button class="btn-delete" onclick="eliminarProducto(${producto.id})">Eliminar</button>
                        </div>
                    </td>
                `;
                cuerpoTabla.appendChild(fila);
            });
        })
        .catch(function(error) {
            console.error('Error al cargar productos:', error);
            alert('Error al cargar la lista de productos: ' + error.message);
        });
}

// Abrir modal para crear producto
function abrirModalCrear() {
    console.log('Abriendo modal para crear producto');
    
    const modal = document.getElementById('modal-producto');
    const modalTitulo = document.getElementById('modal-titulo');
    const form = document.getElementById('form-producto');
    
    if (!modal || !modalTitulo || !form) {
        console.error('Elementos del modal no encontrados');
        return;
    }
    
    modalTitulo.textContent = 'Nuevo Producto';
    form.reset();
    document.getElementById('producto-id').value = '';
    modal.style.display = 'block';
    
    // Enfocar el primer campo
    setTimeout(function() {
        const codigoInput = document.getElementById('codigo');
        if (codigoInput) {
            codigoInput.focus();
        }
    }, 100);
}

// Abrir modal para editar producto
function editarProducto(id) {
    console.log('Editando producto ID:', id);
    
    fetch('/api/productos')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor: ' + response.status);
            }
            return response.json();
        })
        .then(function(productos) {
            const producto = productos.find(function(p) {
                return p.id === id;
            });
            
            if (producto) {
                const modal = document.getElementById('modal-producto');
                const modalTitulo = document.getElementById('modal-titulo');
                
                if (!modal || !modalTitulo) {
                    console.error('Elementos del modal no encontrados');
                    return;
                }
                
                modalTitulo.textContent = 'Editar Producto';
                document.getElementById('producto-id').value = producto.id;
                document.getElementById('codigo').value = producto.codigo || '';
                document.getElementById('nombre').value = producto.nombre || '';
                document.getElementById('descripcion').value = producto.descripcion || '';
                document.getElementById('precio').value = parseFloat(producto.precio).toFixed(2) || '';
                document.getElementById('stock').value = producto.stock || 0;
                document.getElementById('categoria').value = producto.categoria || '';
                
                modal.style.display = 'block';
                
                // Enfocar el primer campo
                setTimeout(function() {
                    const codigoInput = document.getElementById('codigo');
                    if (codigoInput) {
                        codigoInput.focus();
                    }
                }, 100);
            } else {
                alert('Producto no encontrado');
            }
        })
        .catch(function(error) {
            console.error('Error al cargar producto:', error);
            alert('Error al cargar los datos del producto: ' + error.message);
        });
}

// Cerrar modal
function cerrarModal() {
    console.log('Cerrando modal de productos');
    
    const modal = document.getElementById('modal-producto');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Guardar producto (crear o actualizar)
function guardarProducto() {
    console.log('Guardando producto...');
    
    const id = document.getElementById('producto-id').value;
    const codigo = document.getElementById('codigo').value;
    const nombre = document.getElementById('nombre').value;
    const precio = document.getElementById('precio').value;
    
    // Validaciones básicas
    if (!codigo || codigo.trim() === '') {
        alert('El código es obligatorio');
        document.getElementById('codigo').focus();
        return;
    }
    
    if (!nombre || nombre.trim() === '') {
        alert('El nombre es obligatorio');
        document.getElementById('nombre').focus();
        return;
    }
    
    if (!precio || parseFloat(precio) <= 0) {
        alert('El precio debe ser mayor a 0');
        document.getElementById('precio').focus();
        return;
    }
    
    const producto = {
        codigo: codigo.trim(),
        nombre: nombre.trim(),
        descripcion: document.getElementById('descripcion').value.trim(),
        precio: parseFloat(precio),
        stock: parseInt(document.getElementById('stock').value) || 0,
        categoria: document.getElementById('categoria').value.trim()
    };
    
    console.log('Datos del producto:', producto);
    
    let url = '/api/productos';
    let method = 'POST';
    
    if (id) {
        url = '/api/productos/' + id;
        method = 'PUT';
        console.log('Actualizando producto existente ID:', id);
    } else {
        console.log('Creando nuevo producto');
    }
    
    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(producto)
    })
    .then(function(response) {
        if (!response.ok) {
            return response.json().then(function(errorData) {
                throw new Error(errorData.error || 'Error del servidor: ' + response.status);
            });
        }
        return response.json();
    })
    .then(function(result) {
        console.log('Respuesta del servidor:', result);
        
        if (result.error) {
            alert('Error: ' + result.error);
        } else {
            cerrarModal();
            cargarProductos();
            alert(result.message || (id ? 'Producto actualizado exitosamente' : 'Producto creado exitosamente'));
        }
    })
    .catch(function(error) {
        console.error('Error al guardar producto:', error);
        alert('Error al guardar el producto: ' + error.message);
    });
}

// Eliminar producto
function eliminarProducto(id) {
    console.log('Solicitando eliminar producto ID:', id);
    
    if (!confirm('¿Estás seguro de que quieres eliminar este producto? Esta acción no se puede deshacer.')) {
        return;
    }
    
    fetch('/api/productos/' + id, {
        method: 'DELETE'
    })
    .then(function(response) {
        if (!response.ok) {
            return response.json().then(function(errorData) {
                throw new Error(errorData.error || 'Error del servidor: ' + response.status);
            });
        }
        return response.json();
    })
    .then(function(result) {
        console.log('Respuesta de eliminación:', result);
        
        if (result.error) {
            alert('Error: ' + result.error);
        } else {
            cargarProductos();
            alert(result.message || 'Producto eliminado exitosamente');
        }
    })
    .catch(function(error) {
        console.error('Error al eliminar producto:', error);
        alert('Error al eliminar el producto: ' + error.message);
    });
}

// Función para escapar HTML (prevenir XSS)
function escapeHtml(text) {
    if (!text) return '';
    
    const map = {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#039;'
    };
    
    return text.toString().replace(/[&<>"']/g, function(m) {
        return map[m];
    });
}

// Cerrar modal al hacer clic fuera de él
window.addEventListener('click', function(event) {
    const modal = document.getElementById('modal-producto');
    if (modal && event.target === modal) {
        cerrarModal();
    }
});

// Cerrar modal con tecla ESC
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const modal = document.getElementById('modal-producto');
        if (modal && modal.style.display === 'block') {
            cerrarModal();
        }
    }
});

// Hacer las funciones disponibles globalmente
window.abrirModalCrear = abrirModalCrear;
window.editarProducto = editarProducto;
window.eliminarProducto = eliminarProducto;
window.cerrarModal = cerrarModal;
window.cargarProductos = cargarProductos;
window.guardarProducto = guardarProducto;

console.log('Script de gestión de productos cargado correctamente');
