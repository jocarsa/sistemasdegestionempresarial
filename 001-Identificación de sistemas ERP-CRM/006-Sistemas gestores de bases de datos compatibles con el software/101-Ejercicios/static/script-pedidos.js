// Funciones para la gestión de pedidos
let productosDisponibles = [];
let clientesDisponibles = [];
let contadorLineas = 0;

document.addEventListener('DOMContentLoaded', function() {
    console.log('Módulo de pedidos cargado');
    cargarPedidos();
    cargarClientesYProductos();
    
    // Configurar el formulario de pedido
    const formPedido = document.getElementById('form-pedido');
    if (formPedido) {
        formPedido.addEventListener('submit', function(event) {
            event.preventDefault();
            console.log('Formulario de pedido enviado');
            guardarPedido();
        });
    }
    
    // Establecer fecha actual por defecto
    const fechaInput = document.getElementById('fecha_pedido');
    if (fechaInput) {
        const today = new Date().toISOString().split('T')[0];
        fechaInput.value = today;
    }
});

// Cargar lista de pedidos
function cargarPedidos() {
    console.log('Iniciando carga de pedidos...');
    
    fetch('/api/pedidos')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor: ' + response.status);
            }
            return response.json();
        })
        .then(function(pedidos) {
            console.log('Pedidos cargados:', pedidos);
            const cuerpoTabla = document.getElementById('cuerpo-tabla');
            
            if (!cuerpoTabla) {
                console.error('No se encontró el elemento cuerpo-tabla');
                return;
            }
            
            cuerpoTabla.innerHTML = '';
            
            if (pedidos.length === 0) {
                const fila = document.createElement('tr');
                fila.innerHTML = '<td colspan="6" style="text-align: center; padding: 2rem;">No hay pedidos registrados</td>';
                cuerpoTabla.appendChild(fila);
                return;
            }
            
            pedidos.forEach(function(pedido) {
                const fila = document.createElement('tr');
                fila.innerHTML = `
                    <td>${escapeHtml(pedido.numero_pedido)}</td>
                    <td>${escapeHtml(pedido.cliente_nombre)}</td>
                    <td>${new Date(pedido.fecha_pedido).toLocaleDateString()}</td>
                    <td>€${parseFloat(pedido.total).toFixed(2)}</td>
                    <td>
                        <span class="estado-badge ${pedido.estado}">
                            ${pedido.estado.charAt(0).toUpperCase() + pedido.estado.slice(1)}
                        </span>
                    </td>
                    <td>
                        <div class="btn-actions">
                            <button class="btn-edit" onclick="verPedido(${pedido.id})">Ver</button>
                            <button class="btn-delete" onclick="eliminarPedido(${pedido.id})">Eliminar</button>
                        </div>
                    </td>
                `;
                cuerpoTabla.appendChild(fila);
            });
        })
        .catch(function(error) {
            console.error('Error al cargar pedidos:', error);
            alert('Error al cargar la lista de pedidos: ' + error.message);
        });
}

// Cargar clientes y productos para los selects
function cargarClientesYProductos() {
    console.log('Cargando clientes y productos...');
    
    // Cargar clientes
    fetch('/api/clientes')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error al cargar clientes: ' + response.status);
            }
            return response.json();
        })
        .then(function(clientes) {
            clientesDisponibles = clientes;
            const selectCliente = document.getElementById('cliente_id');
            
            if (selectCliente) {
                selectCliente.innerHTML = '<option value="">Seleccionar cliente</option>';
                clientes.forEach(function(cliente) {
                    const option = document.createElement('option');
                    option.value = cliente.id;
                    option.textContent = cliente.nombre + ' (' + cliente.email + ')';
                    selectCliente.appendChild(option);
                });
            }
        })
        .catch(function(error) {
            console.error('Error al cargar clientes:', error);
        });
    
    // Cargar productos
    fetch('/api/productos')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error al cargar productos: ' + response.status);
            }
            return response.json();
        })
        .then(function(productos) {
            productosDisponibles = productos.filter(function(p) { return p.activo; });
            console.log('Productos disponibles:', productosDisponibles);
        })
        .catch(function(error) {
            console.error('Error al cargar productos:', error);
        });
}

// Abrir modal para crear pedido
function abrirModalCrear() {
    console.log('Abriendo modal para crear pedido');
    
    const modal = document.getElementById('modal-pedido');
    const modalTitulo = document.getElementById('modal-titulo');
    const form = document.getElementById('form-pedido');
    
    if (!modal || !modalTitulo || !form) {
        console.error('Elementos del modal no encontrados');
        return;
    }
    
    modalTitulo.textContent = 'Nuevo Pedido';
    form.reset();
    document.getElementById('pedido-id').value = '';
    
    // Establecer fecha actual por defecto
    const fechaInput = document.getElementById('fecha_pedido');
    if (fechaInput) {
        const today = new Date().toISOString().split('T')[0];
        fechaInput.value = today;
    }
    
    // Limpiar líneas
    const lineasContainer = document.getElementById('lineas-pedido');
    if (lineasContainer) {
        lineasContainer.innerHTML = '';
        contadorLineas = 0;
    }
    
    // Agregar primera línea
    agregarLinea();
    
    modal.style.display = 'block';
    
    // Enfocar el primer campo
    setTimeout(function() {
        const clienteSelect = document.getElementById('cliente_id');
        if (clienteSelect) {
            clienteSelect.focus();
        }
    }, 100);
}

// Agregar nueva línea al pedido
function agregarLinea() {
    console.log('Agregando nueva línea de pedido');
    
    const lineasContainer = document.getElementById('lineas-pedido');
    if (!lineasContainer) return;
    
    const lineaId = 'linea-' + contadorLineas;
    const nuevaLinea = document.createElement('div');
    nuevaLinea.className = 'linea-pedido';
    nuevaLinea.id = lineaId;
    
    nuevaLinea.innerHTML = `
        <div class="linea-header">
            <strong>Línea ${contadorLineas + 1}</strong>
            <button type="button" class="btn-eliminar-linea" onclick="eliminarLinea('${lineaId}')">×</button>
        </div>
        <div class="linea-content">
            <div class="form-group">
                <label>Producto *</label>
                <select class="producto-select" onchange="actualizarPrecio('${lineaId}')" required>
                    <option value="">Seleccionar producto</option>
                    ${productosDisponibles.map(function(producto) {
                        return `<option value="${producto.id}" data-precio="${producto.precio}">${producto.nombre} - €${parseFloat(producto.precio).toFixed(2)} (Stock: ${producto.stock})</option>`;
                    }).join('')}
                </select>
            </div>
            <div class="form-group">
                <label>Precio Unitario</label>
                <input type="number" class="precio-unitario" step="0.01" min="0" readonly>
            </div>
            <div class="form-group">
                <label>Cantidad *</label>
                <input type="number" class="cantidad" min="1" value="1" onchange="calcularSubtotal('${lineaId}')" required>
            </div>
            <div class="form-group">
                <label>Subtotal</label>
                <input type="number" class="subtotal" step="0.01" min="0" readonly>
            </div>
        </div>
    `;
    
    lineasContainer.appendChild(nuevaLinea);
    contadorLineas++;
    
    // Recalcular total
    calcularTotal();
}

// Eliminar línea del pedido
function eliminarLinea(lineaId) {
    console.log('Eliminando línea:', lineaId);
    
    const linea = document.getElementById(lineaId);
    if (linea) {
        linea.remove();
        calcularTotal();
    }
}

// Actualizar precio cuando se selecciona un producto
function actualizarPrecio(lineaId) {
    const linea = document.getElementById(lineaId);
    if (!linea) return;
    
    const productoSelect = linea.querySelector('.producto-select');
    const precioInput = linea.querySelector('.precio-unitario');
    const cantidadInput = linea.querySelector('.cantidad');
    
    if (productoSelect && precioInput && cantidadInput) {
        const selectedOption = productoSelect.options[productoSelect.selectedIndex];
        if (selectedOption && selectedOption.value) {
            const precio = selectedOption.getAttribute('data-precio');
            precioInput.value = parseFloat(precio).toFixed(2);
            
            // Calcular subtotal
            calcularSubtotal(lineaId);
        } else {
            precioInput.value = '';
            linea.querySelector('.subtotal').value = '';
        }
    }
}

// Calcular subtotal de una línea
function calcularSubtotal(lineaId) {
    const linea = document.getElementById(lineaId);
    if (!linea) return;
    
    const precioInput = linea.querySelector('.precio-unitario');
    const cantidadInput = linea.querySelector('.cantidad');
    const subtotalInput = linea.querySelector('.subtotal');
    
    if (precioInput && cantidadInput && subtotalInput) {
        const precio = parseFloat(precioInput.value) || 0;
        const cantidad = parseInt(cantidadInput.value) || 0;
        const subtotal = precio * cantidad;
        
        subtotalInput.value = subtotal.toFixed(2);
        
        // Recalcular total
        calcularTotal();
    }
}

// Calcular total del pedido
function calcularTotal() {
    const lineas = document.querySelectorAll('.linea-pedido');
    let total = 0;
    
    lineas.forEach(function(linea) {
        const subtotalInput = linea.querySelector('.subtotal');
        if (subtotalInput && subtotalInput.value) {
            total += parseFloat(subtotalInput.value);
        }
    });
    
    const totalElement = document.getElementById('total-pedido');
    if (totalElement) {
        totalElement.textContent = total.toFixed(2);
    }
}

// Cerrar modal
function cerrarModal() {
    console.log('Cerrando modal de pedidos');
    
    const modal = document.getElementById('modal-pedido');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Guardar pedido
function guardarPedido() {
    console.log('Guardando pedido...');
    
    const clienteId = document.getElementById('cliente_id').value;
    const lineas = document.querySelectorAll('.linea-pedido');
    
    // Validaciones básicas
    if (!clienteId) {
        alert('Debe seleccionar un cliente');
        document.getElementById('cliente_id').focus();
        return;
    }
    
    if (lineas.length === 0) {
        alert('Debe agregar al menos una línea de pedido');
        return;
    }
    
    // Validar que todas las líneas tengan producto y cantidad
    let lineasValidas = true;
    const lineasData = [];
    
    lineas.forEach(function(linea) {
        const productoSelect = linea.querySelector('.producto-select');
        const cantidadInput = linea.querySelector('.cantidad');
        
        if (!productoSelect.value || !cantidadInput.value || parseInt(cantidadInput.value) <= 0) {
            lineasValidas = false;
        } else {
            lineasData.push({
                producto_id: parseInt(productoSelect.value),
                cantidad: parseInt(cantidadInput.value)
            });
        }
    });
    
    if (!lineasValidas) {
        alert('Todas las líneas deben tener un producto seleccionado y una cantidad válida');
        return;
    }
    
    const pedido = {
        cliente_id: parseInt(clienteId),
        fecha_pedido: document.getElementById('fecha_pedido').value,
        estado: 'pendiente',
        notas: document.getElementById('notas').value,
        lineas: lineasData
    };
    
    console.log('Datos del pedido:', pedido);
    
    fetch('/api/pedidos', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(pedido)
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
            cargarPedidos();
            alert(result.message || 'Pedido creado exitosamente. Número: ' + result.numero_pedido);
        }
    })
    .catch(function(error) {
        console.error('Error al guardar pedido:', error);
        alert('Error al guardar el pedido: ' + error.message);
    });
}

// Ver detalles del pedido
function verPedido(id) {
    console.log('Viendo pedido ID:', id);
    
    fetch('/api/pedidos/' + id)
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor: ' + response.status);
            }
            return response.json();
        })
        .then(function(data) {
            const pedido = data.pedido;
            const lineas = data.lineas;
            
            let mensaje = `Pedido: ${pedido.numero_pedido}\n` +
                         `Cliente: ${pedido.cliente_nombre}\n` +
                         `Fecha: ${new Date(pedido.fecha_pedido).toLocaleDateString()}\n` +
                         `Estado: ${pedido.estado}\n` +
                         `Total: €${parseFloat(pedido.total).toFixed(2)}\n\n` +
                         `Líneas del pedido:\n`;
            
            lineas.forEach(function(linea, index) {
                mensaje += `${index + 1}. ${linea.producto_nombre} - ${linea.cantidad} x €${parseFloat(linea.precio_unitario).toFixed(2)} = €${parseFloat(linea.subtotal).toFixed(2)}\n`;
            });
            
            if (pedido.notas) {
                mensaje += `\nNotas: ${pedido.notas}`;
            }
            
            alert(mensaje);
        })
        .catch(function(error) {
            console.error('Error al cargar pedido:', error);
            alert('Error al cargar los detalles del pedido: ' + error.message);
        });
}

// Eliminar pedido
function eliminarPedido(id) {
    console.log('Solicitando eliminar pedido ID:', id);
    
    if (!confirm('¿Estás seguro de que quieres eliminar este pedido? Esta acción no se puede deshacer.')) {
        return;
    }
    
    fetch('/api/pedidos/' + id, {
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
            cargarPedidos();
            alert(result.message || 'Pedido eliminado exitosamente');
        }
    })
    .catch(function(error) {
        console.error('Error al eliminar pedido:', error);
        alert('Error al eliminar el pedido: ' + error.message);
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
    const modal = document.getElementById('modal-pedido');
    if (modal && event.target === modal) {
        cerrarModal();
    }
});

// Cerrar modal con tecla ESC
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const modal = document.getElementById('modal-pedido');
        if (modal && modal.style.display === 'block') {
            cerrarModal();
        }
    }
});

// Hacer las funciones disponibles globalmente
window.abrirModalCrear = abrirModalCrear;
window.agregarLinea = agregarLinea;
window.eliminarLinea = eliminarLinea;
window.actualizarPrecio = actualizarPrecio;
window.calcularSubtotal = calcularSubtotal;
window.verPedido = verPedido;
window.eliminarPedido = eliminarPedido;
window.cerrarModal = cerrarModal;
window.cargarPedidos = cargarPedidos;
window.guardarPedido = guardarPedido;

console.log('Script de gestión de pedidos cargado correctamente');
