// Funciones para la gestión de clientes
document.addEventListener('DOMContentLoaded', function() {
    console.log('Sistema de Gestión cargado');
    
    // Cargar clientes si estamos en la página de clientes
    if (document.getElementById('tabla-clientes')) {
        console.log('Cargando lista de clientes...');
        cargarClientes();
    }
    
    // Cargar estadísticas si estamos en el dashboard
    if (document.getElementById('total-clientes')) {
        console.log('Cargando estadísticas...');
        cargarEstadisticas();
    }
    
    // Configurar el formulario de cliente
    const formCliente = document.getElementById('form-cliente');
    if (formCliente) {
        formCliente.addEventListener('submit', function(event) {
            event.preventDefault();
            console.log('Formulario de cliente enviado');
            guardarCliente();
        });
    }
    
    // Configurar cierre del modal
    const closeButton = document.querySelector('.close');
    if (closeButton) {
        closeButton.addEventListener('click', cerrarModal);
    }
});

// Cargar lista de clientes
function cargarClientes() {
    console.log('Iniciando carga de clientes...');
    
    fetch('/api/clientes')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor: ' + response.status);
            }
            return response.json();
        })
        .then(function(clientes) {
            console.log('Clientes cargados:', clientes);
            const cuerpoTabla = document.getElementById('cuerpo-tabla');
            
            if (!cuerpoTabla) {
                console.error('No se encontró el elemento cuerpo-tabla');
                return;
            }
            
            cuerpoTabla.innerHTML = '';
            
            if (clientes.length === 0) {
                const fila = document.createElement('tr');
                fila.innerHTML = '<td colspan="6" style="text-align: center; padding: 2rem;">No hay clientes registrados</td>';
                cuerpoTabla.appendChild(fila);
                return;
            }
            
            clientes.forEach(function(cliente) {
                const fila = document.createElement('tr');
                fila.innerHTML = `
                    <td>${escapeHtml(cliente.nombre)}</td>
                    <td>${escapeHtml(cliente.email)}</td>
                    <td>${cliente.telefono ? escapeHtml(cliente.telefono) : '-'}</td>
                    <td>${cliente.empresa ? escapeHtml(cliente.empresa) : '-'}</td>
                    <td>${cliente.direccion ? escapeHtml(cliente.direccion) : '-'}</td>
                    <td>
                        <div class="btn-actions">
                            <button class="btn-edit" onclick="editarCliente(${cliente.id})">Editar</button>
                            <button class="btn-delete" onclick="eliminarCliente(${cliente.id})">Eliminar</button>
                        </div>
                    </td>
                `;
                cuerpoTabla.appendChild(fila);
            });
        })
        .catch(function(error) {
            console.error('Error al cargar clientes:', error);
            alert('Error al cargar la lista de clientes: ' + error.message);
        });
}

// Cargar estadísticas del dashboard
function cargarEstadisticas() {
    console.log('Cargando estadísticas...');
    
    fetch('/api/clientes')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor: ' + response.status);
            }
            return response.json();
        })
        .then(function(clientes) {
            const totalClientes = document.getElementById('total-clientes');
            const totalEmpresas = document.getElementById('total-empresas');
            
            if (totalClientes) {
                totalClientes.textContent = clientes.length;
            }
            
            // Contar empresas únicas
            const empresas = [];
            clientes.forEach(function(cliente) {
                if (cliente.empresa && cliente.empresa.trim() !== '' && !empresas.includes(cliente.empresa)) {
                    empresas.push(cliente.empresa);
                }
            });
            
            if (totalEmpresas) {
                totalEmpresas.textContent = empresas.length;
            }
        })
        .catch(function(error) {
            console.error('Error al cargar estadísticas:', error);
            // No mostrar alerta para no molestar al usuario
        });
}

// Abrir modal para crear cliente
function abrirModalCrear() {
    console.log('Abriendo modal para crear cliente');
    
    const modal = document.getElementById('modal-cliente');
    const modalTitulo = document.getElementById('modal-titulo');
    const form = document.getElementById('form-cliente');
    
    if (!modal || !modalTitulo || !form) {
        console.error('Elementos del modal no encontrados');
        return;
    }
    
    modalTitulo.textContent = 'Nuevo Cliente';
    form.reset();
    document.getElementById('cliente-id').value = '';
    modal.style.display = 'block';
    
    // Enfocar el primer campo
    setTimeout(function() {
        const nombreInput = document.getElementById('nombre');
        if (nombreInput) {
            nombreInput.focus();
        }
    }, 100);
}

// Abrir modal para editar cliente
function editarCliente(id) {
    console.log('Editando cliente ID:', id);
    
    fetch('/api/clientes')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error en la respuesta del servidor: ' + response.status);
            }
            return response.json();
        })
        .then(function(clientes) {
            const cliente = clientes.find(function(c) {
                return c.id === id;
            });
            
            if (cliente) {
                const modal = document.getElementById('modal-cliente');
                const modalTitulo = document.getElementById('modal-titulo');
                
                if (!modal || !modalTitulo) {
                    console.error('Elementos del modal no encontrados');
                    return;
                }
                
                modalTitulo.textContent = 'Editar Cliente';
                document.getElementById('cliente-id').value = cliente.id;
                document.getElementById('nombre').value = cliente.nombre || '';
                document.getElementById('email').value = cliente.email || '';
                document.getElementById('telefono').value = cliente.telefono || '';
                document.getElementById('empresa').value = cliente.empresa || '';
                document.getElementById('direccion').value = cliente.direccion || '';
                
                modal.style.display = 'block';
                
                // Enfocar el primer campo
                setTimeout(function() {
                    const nombreInput = document.getElementById('nombre');
                    if (nombreInput) {
                        nombreInput.focus();
                    }
                }, 100);
            } else {
                alert('Cliente no encontrado');
            }
        })
        .catch(function(error) {
            console.error('Error al cargar cliente:', error);
            alert('Error al cargar los datos del cliente: ' + error.message);
        });
}

// Cerrar modal
function cerrarModal() {
    console.log('Cerrando modal');
    
    const modal = document.getElementById('modal-cliente');
    if (modal) {
        modal.style.display = 'none';
    }
}

// Guardar cliente (crear o actualizar)
function guardarCliente() {
    console.log('Guardando cliente...');
    
    const id = document.getElementById('cliente-id').value;
    const nombre = document.getElementById('nombre').value;
    const email = document.getElementById('email').value;
    
    // Validaciones básicas
    if (!nombre || nombre.trim() === '') {
        alert('El nombre es obligatorio');
        document.getElementById('nombre').focus();
        return;
    }
    
    if (!email || email.trim() === '') {
        alert('El email es obligatorio');
        document.getElementById('email').focus();
        return;
    }
    
    if (!isValidEmail(email)) {
        alert('Por favor ingresa un email válido');
        document.getElementById('email').focus();
        return;
    }
    
    const cliente = {
        nombre: nombre.trim(),
        email: email.trim(),
        telefono: document.getElementById('telefono').value.trim(),
        empresa: document.getElementById('empresa').value.trim(),
        direccion: document.getElementById('direccion').value.trim()
    };
    
    console.log('Datos del cliente:', cliente);
    
    let url = '/api/clientes';
    let method = 'POST';
    
    if (id) {
        url = '/api/clientes/' + id;
        method = 'PUT';
        console.log('Actualizando cliente existente ID:', id);
    } else {
        console.log('Creando nuevo cliente');
    }
    
    fetch(url, {
        method: method,
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(cliente)
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
            cargarClientes();
            
            // Recargar estadísticas si estamos en el dashboard
            if (document.getElementById('total-clientes')) {
                cargarEstadisticas();
            }
            
            alert(result.message || (id ? 'Cliente actualizado exitosamente' : 'Cliente creado exitosamente'));
        }
    })
    .catch(function(error) {
        console.error('Error al guardar cliente:', error);
        alert('Error al guardar el cliente: ' + error.message);
    });
}

// Eliminar cliente
function eliminarCliente(id) {
    console.log('Solicitando eliminar cliente ID:', id);
    
    if (!confirm('¿Estás seguro de que quieres eliminar este cliente? Esta acción no se puede deshacer.')) {
        return;
    }
    
    fetch('/api/clientes/' + id, {
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
            cargarClientes();
            
            // Recargar estadísticas si estamos en el dashboard
            if (document.getElementById('total-clientes')) {
                cargarEstadisticas();
            }
            
            alert(result.message || 'Cliente eliminado exitosamente');
        }
    })
    .catch(function(error) {
        console.error('Error al eliminar cliente:', error);
        alert('Error al eliminar el cliente: ' + error.message);
    });
}

// Función para validar email
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
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
    const modal = document.getElementById('modal-cliente');
    if (modal && event.target === modal) {
        cerrarModal();
    }
});

// Cerrar modal con tecla ESC
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        const modal = document.getElementById('modal-cliente');
        if (modal && modal.style.display === 'block') {
            cerrarModal();
        }
    }
});

// Hacer las funciones disponibles globalmente
window.abrirModalCrear = abrirModalCrear;
window.editarCliente = editarCliente;
window.eliminarCliente = eliminarCliente;
window.cerrarModal = cerrarModal;
window.cargarClientes = cargarClientes;
window.guardarCliente = guardarCliente;

console.log('Script de gestión de clientes cargado correctamente');
