// Funciones para el dashboard
document.addEventListener('DOMContentLoaded', function() {
    console.log('Dashboard cargado');
    cargarEstadisticas();
});

// Cargar estadísticas del dashboard
function cargarEstadisticas() {
    console.log('Cargando estadísticas del dashboard...');
    
    // Cargar clientes
    fetch('/api/clientes')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error al cargar clientes: ' + response.status);
            }
            return response.json();
        })
        .then(function(clientes) {
            document.getElementById('total-clientes').textContent = clientes.length;
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
            document.getElementById('total-productos').textContent = productos.length;
        })
        .catch(function(error) {
            console.error('Error al cargar productos:', error);
        });
    
    // Cargar pedidos y calcular total de ventas
    fetch('/api/pedidos')
        .then(function(response) {
            if (!response.ok) {
                throw new Error('Error al cargar pedidos: ' + response.status);
            }
            return response.json();
        })
        .then(function(pedidos) {
            document.getElementById('total-pedidos').textContent = pedidos.length;
            
            // Calcular total de ventas
            let totalVentas = 0;
            pedidos.forEach(function(pedido) {
                totalVentas += parseFloat(pedido.total) || 0;
            });
            
            document.getElementById('total-ventas').textContent = '€' + totalVentas.toFixed(2);
        })
        .catch(function(error) {
            console.error('Error al cargar pedidos:', error);
        });
}

// Hacer funciones disponibles globalmente
window.cargarEstadisticas = cargarEstadisticas;
