
## Objetivo

Construir una **página HTML** con **JavaScript puro** que permita **añadir** clientes a un array, **listar** la tabla en el DOM y **eliminar** un cliente por **índice**. Debe evidenciar: uso de **variables/constantes**, **operadores**, **arrays**, **if/else**, **for/forEach**, **funciones**, **eventos** y **manipulación del DOM** con `querySelector` y `innerHTML`.

> Sin librerías externas. Un único archivo `.html`.

## Requisitos funcionales

1. **Interfaz mínima**

   * Campo de texto **Nombre** (`#nombre`) y **Email** (`#email`).
   * Botón **Añadir**.
   * **Tabla** vacía con cabecera `Nombre | Email | Acciones` para mostrar los clientes.
   * Campo de texto **ID a eliminar** (`#ideliminar`) y botón **Eliminar**.

2. **Datos en memoria**

   * Declarar `let clientes = [];` (array de objetos con propiedades `nombre` y `email`).
   * No usar `fetch` ni archivos externos.

3. **Operaciones**

   * **CREATE**: al pulsar **Añadir**, leer `#nombre` y `#email`, **validar**:

     * Si algún campo está vacío → usar `console.warn()` y mostrar un mensaje visible (sin `alert()`), **no** añadir.
     * En caso correcto, **push** al array y **limpiar** los inputs.
   * **READ**: tras cada cambio, **re-renderizar** la tabla completa desde el array.
   * **DELETE**: introducir un **índice** en `#ideliminar` y pulsar **Eliminar**:

     * Si el índice **no existe** (menor que 0 o mayor que el último) → `console.error()` y mensaje visible.
     * Si es válido → `splice(indice, 1)` y re-render.

4. **DOM y eventos**

   * Asignar manejadores con `onclick` (o `addEventListener`) a los botones.
   * Usar `document.querySelector(...)` para seleccionar elementos.
   * Prohibido recargar la página para ver cambios.

5. **Funciones (mínimo)**

   * `anadirCliente()`: valida, inserta en el array y llama a `pintarTabla()`.
   * `pintarTabla()`: reconstruye el HTML de la tabla a partir de `clientes`.
   * `eliminarClientePorIndice()`: valida el índice y elimina con `splice`.
   * (Sugerido) `mostrarMensaje(texto, tipo)` para info/advertencia/error en la página.

6. **Salidas y comentarios**

   * **Encabezado de 3 líneas** (nombre del programa, autor/a, año) insertado en el documento (con `document.write` en una sola sección o mediante DOM).
   * Usar `console.log()` en pasos clave (añadido, listado).
   * Comentar: validación, inserción, borrado y render.

7. **Restricciones**

   * Un único archivo `.html`.
   * Sin `localStorage` (opcional como **extra**).
   * Sin clases ni `fetch` (POO no requerida en este ejercicio).

---

## Casos de prueba (verificación del alumnado)

1. **Alta válida**: completar nombre y email → aparece una nueva fila en la tabla.
2. **Alta inválida**: dejar un campo vacío → `console.warn()` + mensaje visible, **no** se añade.
3. **Eliminar válido**: indicar un índice existente (p. ej., `0`) → desaparece esa fila.
4. **Eliminar inválido**: índice fuera de rango → `console.error()` + mensaje visible.
5. **Re-listado**: tras varias altas y una baja, la tabla refleja el estado actual del array.


> **Extra opcional (no puntúa extra, solo práctica):** persistir `clientes` en `localStorage` al renderizar y cargar al iniciar.

