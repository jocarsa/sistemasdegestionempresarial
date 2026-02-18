# sistemasdegestionempresarial

**Author:** Jose Vicente Carratala Sanchis

## Table of contents

- [Prerrequisitos](#prerrequisitos)
  - [salidas](#salidas)
  - [variables y constantes](#variables-y-constantes)
  - [operadores](#operadores)
  - [estructuras de datos](#estructuras-de-datos)
  - [estructuras de control](#estructuras-de-control)
  - [funciones](#funciones)
  - [programacion orientada a objetos](#programacion-orientada-a-objetos)
  - [DOM](#dom)
  - [Ejercicio CRUD 1](#ejercicio-crud-1)
  - [Ejercicio CRUD 2](#ejercicio-crud-2)
  - [Ejercicio final de unidad](#ejercicio-final-de-unidad)
- [Identificación de sistemas ERP-CRM](#identificacion-de-sistemas-erp-crm)
  - [Concepto de ERP](#concepto-de-erp)
  - [Revisión de los ERP actuales](#revision-de-los-erp-actuales)
  - [Concepto de CRM](#concepto-de-crm)
  - [Revisión de los CRM actuales](#revision-de-los-crm-actuales)
  - [Tipos de licencias de los ERP-CRM](#tipos-de-licencias-de-los-erp-crm)
  - [Sistemas gestores de bases de datos compatibles con el software](#sistemas-gestores-de-bases-de-datos-compatibles-con-el-software)
  - [Instalación y configuración del sistema informático](#instalacion-y-configuracion-del-sistema-informatico)
  - [Verificación de la instalación y configuración](#verificacion-de-la-instalacion-y-configuracion)
  - [Documentación de las operaciones realizadas](#documentacion-de-las-operaciones-realizadas)
  - [Simulacro de examen](#simulacro-de-examen)
  - [Simulacro de examen 2](#simulacro-de-examen-2)
  - [Ejercicio final de unidad](#ejercicio-final-de-unidad-1)
  - [Examen final](#examen-final)
- [Instalación y configuración de sistemas ERP-CRM](#instalacion-y-configuracion-de-sistemas-erp-crm)
  - [Tipos de instalación.](#tipos-de-instalacion)
  - [Módulos de un sistema ERP-CRM](#modulos-de-un-sistema-erp-crm)
  - [Procesos de instalación del sistema ERP-CRM](#procesos-de-instalacion-del-sistema-erp-crm)
  - [Parámetros de configuración del sistema ERP-CRM](#parametros-de-configuracion-del-sistema-erp-crm)
  - [Actualización del sistema ERP-CRM y aplicación de actualizaciones](#actualizacion-del-sistema-erp-crm-y-aplicacion-de-actualizaciones)
  - [Servicios de acceso al sistema ERP-CRM](#servicios-de-acceso-al-sistema-erp-crm)
  - [Entornos de desarrollo, pruebas y explotación](#entornos-de-desarrollo-pruebas-y-explotacion)
- [Organización y consulta de la información](#organizacion-y-consulta-de-la-informacion)
  - [Definición de campos](#definicion-de-campos)
  - [Consultas de acceso a datos](#consultas-de-acceso-a-datos)
  - [Interfaces de entrada de datos y de procesos.](#interfaces-de-entrada-de-datos-y-de-procesos)
  - [Informes y listados de la aplicación](#informes-y-listados-de-la-aplicacion)
  - [Gestión de pedidos](#gestion-de-pedidos)
  - [Gráficos](#graficos)
  - [Herramientas de monitorización y de evaluación del rendimiento](#herramientas-de-monitorizacion-y-de-evaluacion-del-rendimiento)
  - [Incidencias identificación y resolución](#incidencias-identificacion-y-resolucion)
  - [Procesos de extracción de datos en sistemas de ERP-CRM y almacenes de datos](#procesos-de-extraccion-de-datos-en-sistemas-de-erp-crm-y-almacenes-de-datos)
  - [Inteligencia de negocio (Business Intelligence)](#inteligencia-de-negocio-business-intelligence)
- [Implantación de sistemas ERP-CRM en una empresa](#implantacion-de-sistemas-erp-crm-en-una-empresa)
  - [Tipos de empresa. Necesidades de la empresa](#tipos-de-empresa-necesidades-de-la-empresa)
  - [Selección de los módulos del sistema ERP-CRM](#seleccion-de-los-modulos-del-sistema-erp-crm)
  - [Tablas y vistas que es preciso adaptar](#tablas-y-vistas-que-es-preciso-adaptar)
  - [Consultas necesarias para obtener información](#consultas-necesarias-para-obtener-informacion)
  - [Creación de formularios personalizados](#creacion-de-formularios-personalizados)
  - [Creación de informes personalizados](#creacion-de-informes-personalizados)
  - [Paneles de control (Dashboards)](#paneles-de-control-dashboards)
  - [Integración con otros sistemas de gestión](#integracion-con-otros-sistemas-de-gestion)
- [Desarrollo de componentes](#desarrollo-de-componentes)
  - [Arquitectura del ERP-CRM](#arquitectura-del-erp-crm)
  - [Lenguaje proporcionado](#lenguaje-proporcionado)
  - [Entornos de desarrollo y herramientas del sistema ERP y CRM](#entornos-de-desarrollo-y-herramientas-del-sistema-erp-y-crm)
  - [Inserción, modificación y eliminación de datos en los objetos](#insercion-modificacion-y-eliminacion-de-datos-en-los-objetos)
  - [Operaciones de consulta. Herramientas](#operaciones-de-consulta-herramientas)
  - [Formularios e informes](#formularios-e-informes)
  - [Procesamiento de datos y obtención de la información](#procesamiento-de-datos-y-obtencion-de-la-informacion)
  - [Llamadas a funciones, librerías de funciones (APIs)](#llamadas-a-funciones-librerias-de-funciones-apis)
  - [Depuración y tratamiento de errores](#depuracion-y-tratamiento-de-errores)
- [Proyecto trimestral](#proyecto-trimestral)
  - [Inicio](#inicio)
  - [Login](#login)
  - [selector de modulos](#selector-de-modulos)
  - [seguridad basica](#seguridad-basica)
- [Repaso PHP](#repaso-php)
  - [Repaso inicial](#repaso-inicial)
- [.git](#git)
  - [branches](#branches)
  - [hooks](#hooks)
  - [info](#info)
  - [logs](#logs)
  - [objects](#objects)
  - [refs](#refs)

---

<a id="prerrequisitos"></a>
# Prerrequisitos

<a id="salidas"></a>
## salidas

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/001-salidas)

### salidas
<small>Creado: 2025-09-28 22:27</small>

`002-salidas.html`

```html
<script>
  console.log("Hola mundo desde Javascript");
</script>
```

### adevertencias y errores
<small>Creado: 2025-09-28 22:27</small>

`003-adevertencias y errores.html`

```html
<script>
  console.log("Hola mundo desde Javascript");
  console.warn("Esto parece una advertencia");
  console.error("Esto parece un error");
</script>
```

### document write
<small>Creado: 2025-09-28 22:27</small>

`004-document write.html`

```html
<script>
  document.write("hola mundo para el mundo");
</script>
```

### comentarios
<small>Creado: 2025-09-28 22:27</small>

`005-comentarios.html`

```html
<script>
  // Esto es un comentario de una línea
  /*
    Esto es un comentario
    y tiene varias lineas
  */
</script>
```


<a id="variables-y-constantes"></a>
## variables y constantes

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/002-variables%20y%20constantes)

### variables
<small>Creado: 2025-09-28 22:28</small>

`006-variables.html`

```html
<script>
  var edad = 47;
  var nombre = "Jose Vicente";
</script>
```

### variar el valor de la variable
<small>Creado: 2025-09-28 22:28</small>

`007-variar el valor de la variable.html`

```html
<script>
  var edad = 47;
  console.log("Mi edad es de",edad,"años");
  edad = edad + 1;
  console.log("Mi edad es de",edad,"años");
</script>
```

### constantes
<small>Creado: 2025-09-28 22:28</small>

`008-constantes.html`

```html
<script>
  const PI = 3.1415;
  console.log("El valor de PI es ",PI);
  PI = 4;
</script>
```


<a id="operadores"></a>
## operadores

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/003-operadores)

### Operadores artimeticos
<small>Creado: 2025-09-28 22:27</small>

`009-Operadores artimeticos.html`

```html
<script>
  console.log(4+3);
  console.log(4-3);
  console.log(4*3);
  console.log(4/3);
  console.log(4%3);
</script>
```

### Operadores
<small>Creado: 2025-09-28 22:27</small>

`009-Operadores.html`

```html
<script>
  const PI = 3.1415;
  console.log("El valor de PI es ",PI);
  PI = 4;
</script>
```

### operadores de comparacion
<small>Creado: 2025-09-28 22:27</small>

`010-operadores de comparacion.html`

```html
<script>
  console.log(4 < 3);
  console.log(4 <= 3);
  console.log(4 > 3);
  console.log(4 >= 3);
  console.log(4 == 3);
  console.log(4 != 3);
</script>
```

### operadores matematicos
<small>Creado: 2025-09-28 22:27</small>

`011-operadores matematicos.html`

```html
<script>
  var edad = 47;
  
  edad += 5;
  edad -= 5;
  edad *= 5;
  edad /= 5;
</script>
```


<a id="estructuras-de-datos"></a>
## estructuras de datos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/004-estructuras%20de%20datos)

### arrays
<small>Creado: 2025-09-28 22:27</small>

`012-arrays.html`

```html
<script>
  var clientes = [];
  
  clientes[0] = "Juan";
  clientes[1] = "Jorge";
  clientes[2] = "Jaime";
  clientes[3] = "Jose";
  
  console.table(clientes);
</script>
```

### arrays indices
<small>Creado: 2025-09-28 22:27</small>

`013-arrays indices.html`

```html
<script>
  var clientes = [];
  
  clientes['nombre'] = "Juan";
  clientes['email'] = "juan@juan.com";
  clientes['direccion'] = "Calle de Juan";
  clientes['telefono'] = "6453564";
  
  console.log(clientes);
</script>
```

### operaciones con arrays
<small>Creado: 2025-09-28 22:27</small>

`014-operaciones con arrays.html`

```html
<script>
  var clientes = [];
  
  clientes.push("Juan");
  clientes.push("Jorge");
  clientes.push("Jaime");
  clientes.push("Jose");
  
  console.log(clientes);
  
  clientes.pop(1);
  console.log(clientes);
  
  clientes.splice(1,1);
  
  console.log(clientes);
  
</script>
```


<a id="estructuras-de-control"></a>
## estructuras de control

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/005-estructuras%20de%20control)

### estructura for
<small>Creado: 2025-09-28 22:27</small>

`015-estructura for.html`

```html
<script>
  var dia;
  for(dia = 1;dia<31;dia++){
    document.write("Hoy es el dia ",dia," del mes<br>");
  }
</script>
```

### estructura while
<small>Creado: 2025-09-28 22:27</small>

`016-estructura while.html`

```html
<script>
  var dia = 1;
  while(dia < 31){
    document.write("Hoy es el dia ",dia," del mes<br>");
  }
</script>
```

### Estructura while pero bien
<small>Creado: 2025-09-28 22:27</small>

`017-Estructura while pero bien.html`

```html
<script>
  var dia = 1;
  while(dia < 31){
    document.write("Hoy es el dia ",dia," del mes<br>");
    dia++;
  }
</script>
```

### estructura if
<small>Creado: 2025-09-28 22:27</small>

`018-estructura if.html`

```html
<script>
  var edad = 47;
  if(edad < 30){
    console.log("Eres un joven");
  }
</script>
```

### clausula else
<small>Creado: 2025-09-28 22:27</small>

`019-clausula else.html`

```html
<script>
  var edad = 47;
  if(edad < 30){
    console.log("Eres un joven");
  }else{
    console.log("Ya no eres un joven");
  }
</script>
```

### else if
<small>Creado: 2025-09-28 22:27</small>

`020-else if.html`

```html
<script>
  var edad = 47;
  if(edad < 10){
    console.log("Eres un niño");
  }else if(edad >=10 and edad < 20){
    console.log("Eres un adolescente");
  }else if(edad >=20 and edad < 30){
    console.log("Eres un joven");
  }else{
    console.log("Ya no eres un joven");
  }
</script>
```

### switch
<small>Creado: 2025-09-28 22:27</small>

`021-switch.html`

```html
<script>
  var dia = "lunes";
  switch(dia){
    case "lunes":
      console.log("Hoy es el peor día de la semana");
      break;
    case "martes":
      console.log("Hoy es el segundo peor día de la semana");
      break;
    case "miercoles":
      console.log("Ya estamos a mitad de semana");
      break;
    case "jueves":
      console.log("YA es casi viernes");
      break;
    case "viernes":
      console.log("Por fin es viernes");
      break;
    case "sabado":
      console.log("Hoy es el mejor día de la semana");
      break;
    case "domingo":
      console.log("Parece mentira que mañana ya es lunes");
      break;
  }
</script>
```


<a id="funciones"></a>
## funciones

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/006-funciones)

### funciones.
<small>Creado: 2025-09-28 22:27</small>

`022-funciones..html`

```html
<script>
  function diHola(){
    console.log("Hola");
  }
</script>
```

### llamada a la funcion
<small>Creado: 2025-09-28 22:27</small>

`023-llamada a la funcion.html`

```html
<script>
  function diHola(){
    console.log("Hola");
  }
  
  diHola();
</script>
```


<a id="programacion-orientada-a-objetos"></a>
## programacion orientada a objetos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/007-programacion%20orientada%20a%20objetos)

### parametro
<small>Creado: 2025-09-28 22:27</small>

`024-parametro.html`

```html
<script>
  function diHola(nombre){
    console.log("Hola ",nombre);
  }
  
  diHola();
</script>
```

### funcion con parametro correcto
<small>Creado: 2025-09-28 22:27</small>

`025-funcion con parametro correcto.html`

```html
<script>
  function diHola(nombre){
    console.log("Hola ",nombre);
  }
  
  diHola("Jose Vicente");
</script>
```

### varios parametros
<small>Creado: 2025-09-28 22:27</small>

`026-varios parametros.html`

```html
<script>
  function diHola(nombre,edad){
    return "Hola "+nombre+"tienes"+edad+"años";
  }
  
  console.log(diHola("Jose Vicente",47));
</script>
```

### clases
<small>Creado: 2025-09-28 22:27</small>

`027-clases.html`

```html
<script>
  class Gato{
    constructor(){
      
    }
  }
  
</script>
```

### constructor
<small>Creado: 2025-09-28 22:27</small>

`028-constructor.html`

```html
<script>
  class Gato{
    constructor(){
      this.color = ""
      this.nombre = ""
      this.colorojos = ""
    }
    
  }
  
</script>
```

### metodos
<small>Creado: 2025-09-28 22:27</small>

`029-metodos.html`

```html
<script>
  class Gato{
    constructor(){
      this.color = ""
      this.nombre = ""
      this.colorojos = ""
    }
    maulla(){
      return "miau";
    }
    aranya(){
      return "te araño";
    }
  }
  
</script>
```

### instanciar un gato
<small>Creado: 2025-09-28 22:27</small>

`030-instanciar un gato.html`

```html
<script>
  class Gato{
    constructor(){
      this.color = ""
      this.nombre = ""
      this.colorojos = ""
    }
    maulla(){
      return "miau";
    }
    aranya(){
      return "te araño";
    }
  }
  
  var micifu = new Gato();
  console.log(micifu)
</script>
```

### valores
<small>Creado: 2025-09-28 22:27</small>

`031-valores.html`

```html
<script>
  class Gato{
    constructor(){
      this.color = ""
      this.nombre = ""
      this.colorojos = ""
    }
    maulla(){
      return "miau";
    }
    aranya(){
      return "te araño";
    }
  }
  
  var micifu = new Gato();
  console.log(micifu)
  micifu.color = "naranja"
  micifu.nombre = "Micifu"
  micifu.colorojos = "verde"
  console.log(micifu)
</script>
```

### constructor con parametros
<small>Creado: 2025-09-28 22:27</small>

`032-constructor con parametros.html`

```html
<script>
  class Gato{
    constructor(gatocolor,gatonombre,gatocolorojos){
      this.color = gatocolor
      this.nombre = gatonombre
      this.colorojos = gatocolorojos
    }
    maulla(){
      return "miau";
    }
    aranya(){
      return "te araño";
    }
  }
  
  var micifu = new Gato("naranja","Micifu","verdes");
  console.log(micifu)
  micifu.color = "verde"
  console.log(micifu)

</script>
```

### set y get
<small>Creado: 2025-09-28 22:27</small>

`033-set y get.html`

```html
<script>
  class Gato{
    constructor(gatocolor,gatonombre,gatocolorojos){
      this.color = gatocolor
      this.nombre = gatonombre
      this.colorojos = gatocolorojos
    }
    maulla(){
      return "miau";
    }
    aranya(){
      return "te araño";
    }
    getColor(){
      return this.color;
    }
    setColor(nuevocolor){
      this.color = nuevocolor;
    }
  }
  
  var micifu = new Gato("naranja","Micifu","verdes");
  console.log(micifu)
  micifu.setColor("verde")
  console.log(micifu)

</script>
```


<a id="dom"></a>
## DOM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/008-DOM)

### escribir
<small>Creado: 2025-09-28 22:28</small>

`101-escribir.html`

```html
<html>
  <body>
    <div id="contenedor">
    </div>
  </body>
  <script>
    document.querySelector("#contenedor").innerHTML = "Hola desde Javascript";
  </script>
</html>
```

### leer
<small>Creado: 2025-09-28 22:28</small>

`102-leer.html`

```html
<html>
  <body>
    <div id="contenedor">
      Esto es un texto estático
    </div>
  </body>
  <script>
    var texto = document.querySelector("#contenedor").innerHTML;
    console.log(texto);
  </script>
</html>
```

### eventos
<small>Creado: 2025-09-28 22:28</small>

`103-eventos.html`

```html
<html>
  <body>
    <button>Pulsame</button>
  </body>
  <script>
    document.querySelector("button").onclick = function(){
      console.log("Me has pulsado");
    }
    document.querySelector("button").ondblclick = function(){
      console.log("Me has pulsado pero dos veces");
    }
    document.querySelector("button").oncontextmenu = function(){
      console.log("Me has pulsado pero con el boton derecho");
    }
  </script>
</html>
```

### calculadora
<small>Creado: 2025-09-28 22:28</small>

`104-calculadora.html`

```html
<html>
  <body>
    <input type="text" id="operando1">
    <input type="text" id="operando2">
    <button>Calcula</button>
    <input type="text" id="resultado">
  </body>
  <script>
    // Cuando pulse el boton
    // Primero selecciono el boton y lo meto en una variable
    var boton = document.querySelector("button");
    // Cuando pulse el botón
    boton.onclick = function(){
      // Cogeré el valor de operando 1
         var operando1 = document.querySelector("#operando1").value 
      // Cogeré el valor de operando 2
         var operando2 = document.querySelector("#operando2").value 
      // Realizaré un cálculo
         var resultado = operando1*1 + operando2*1
      // Mostraré el cálculo en el resultado
        document.querySelector("#resultado").value = resultado;
    }
    
  </script>
</html>
```

### clientes
<small>Creado: 2025-09-28 22:28</small>

`105-clientes.html`

```html
<html>
  <head> 
    <style>
  
  body {
        background: radial-gradient(circle at center, #0a0f1e, #05070d);
        font-family: "Segoe UI", Roboto, sans-serif;
        color: #cce7ff;
        margin: 0;
        padding: 20px;
      }

      table {
        width: 80%;
        margin: 40px auto;
        border-collapse: collapse;
        background: rgba(10, 20, 40, 0.8);
        box-shadow: 0 0 20px rgba(0, 150, 255, 0.5);
        border: 1px solid #0ff;
        border-radius: 12px;
        overflow: hidden;
      }

      th, td {
        padding: 14px 20px;
        text-align: left;
      }

      th {
        background: linear-gradient(90deg, #003366, #0055aa);
        color: #00e5ff;
        font-weight: bold;
        letter-spacing: 1px;
        text-transform: uppercase;
        border-bottom: 2px solid #00c3ff;
      }

      tr {
        transition: all 0.3s ease;
      }

      tr:nth-child(even) {
        background: rgba(255, 255, 255, 0.05);
      }

      td {
        border-bottom: 1px solid rgba(0, 150, 255, 0.3);
      }

      tr:hover {
        background: rgba(0, 200, 255, 0.2);
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(0, 200, 255, 0.7);
      }
    </style>

   
  </head>
  <body>
    <table>
      
    </table>
  </body>
  <script>
    fetch("clientes.json")      // Me traigo el json a Javascript
    .then(function(respuesta){  // Y una vez que venga
      return respuesta.json()   // Intepretalo como JSON
    })
    .then(function(datos){      // Y entonces
      console.log(datos)        // Lanzalo a la consola
      
      // Ahora voy a recorrer uno a uno los elementos del array
      // Primero selecciono la tabla desde el HTML
      var tabla = document.querySelector("table")
      // Ahora inicializo un contenido (de momento no vale nada)
      // La estreategia consiste en inicializar una cadena, e ir sumando elementos a la cadena
      var contenido = "<tr><th>Nombre</th><th>Apellido</th><th>Email</th></tr>";
      // Para cada uno de los clientes que han venido del json
      datos.forEach(function(cliente){
        // Arranco una fila HTML
        contenido += "<tr>";
        // Para cada propiedad del objeto
        for (let propiedad in cliente) {
          // Pinto la propiedad en una celda
          contenido += "<td>"+cliente[propiedad]+"</td>";
        }
        // Cierro una fila HTML
        contenido += "</tr>";
      })
      // Esta linea selecciona la tabla y realmente le mete el contenido que hemos ido tejiendo
      tabla.innerHTML = contenido;
    })
  </script>
</html>
```

### Insertar
<small>Creado: 2025-09-28 22:28</small>

`108-Insertar.html`

```html
<html>
  <head> 
    <style>
  
  body {
        background: radial-gradient(circle at center, #0a0f1e, #05070d);
        font-family: "Segoe UI", Roboto, sans-serif;
        color: #cce7ff;
        margin: 0;
        padding: 20px;
      }

      table {
        width: 80%;
        margin: 40px auto;
        border-collapse: collapse;
        background: rgba(10, 20, 40, 0.8);
        box-shadow: 0 0 20px rgba(0, 150, 255, 0.5);
        border: 1px solid #0ff;
        border-radius: 12px;
        overflow: hidden;
      }

      th, td {
        padding: 14px 20px;
        text-align: left;
      }

      th {
        background: linear-gradient(90deg, #003366, #0055aa);
        color: #00e5ff;
        font-weight: bold;
        letter-spacing: 1px;
        text-transform: uppercase;
        border-bottom: 2px solid #00c3ff;
      }

      tr {
        transition: all 0.3s ease;
      }

      tr:nth-child(even) {
        background: rgba(255, 255, 255, 0.05);
      }

      td {
        border-bottom: 1px solid rgba(0, 150, 255, 0.3);
      }

      tr:hover {
        background: rgba(0, 200, 255, 0.2);
        transform: scale(1.02);
        box-shadow: 0 0 15px rgba(0, 200, 255, 0.7);
      }
    </style>

   <meta charset="utf-8">
  </head>
  <body>
    <table>
      
    </table>
  </body>
  <script>
    fetch("clientes.json")      // Me traigo el json a Javascript
    .then(function(respuesta){  // Y una vez que venga
      return respuesta.json()   // Intepretalo como JSON
    })
    .then(function(datos){      // Y entonces
      console.log(datos)        // Lanzalo a la consola
      
      // Ahora voy a recorrer uno a uno los elementos del array
      // Primero selecciono la tabla desde el HTML
      var tabla = document.querySelector("table")
      // Ahora inicializo un contenido (de momento no vale nada)
      // La estreategia consiste en inicializar una cadena, e ir sumando elementos a la cadena
      var contenido = "<tr><th>Nombre</th><th>Apellido</th><th>Email</th></tr>";
      // Para cada uno de los clientes que han venido del json
      datos.forEach(function(cliente){
        // Arranco una fila HTML
        contenido += "<tr>";
        // Para cada propiedad del objeto
        for (let propiedad in cliente) {
          // Pinto la propiedad en una celda
          contenido += "<td>"+cliente[propiedad]+"</td>";
        }
        // Cierro una fila HTML
        contenido += '<td>🖍 ❌ </td>'
        contenido += "</tr>";
      })
      contenido += `
         <tr>
          <td><input type="text" placeholder="Nombre del cliente"></td>
          <td><input type="text" placeholder="Apellidos del cliente"></td>
          <td><input type="text" placeholder="Email del cliente"></td>
          <td><button>Crear</button></td>
         </tr>
      `
      // Esta linea selecciona la tabla y realmente le mete el contenido que hemos ido tejiendo
      tabla.innerHTML = contenido;
    })
  </script>
</html>
```


<a id="ejercicio-crud-1"></a>
## Ejercicio CRUD 1

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/009-Ejercicio%20CRUD%201)

### ejemplo clientes
<small>Creado: 2025-09-28 22:28</small>

`301-ejemplo clientes.html`

```html
<html>
  <head>
  </head>
  <body>
    <p>Nombre del cliente</p>
    <input type="text" id="nombre">
    <p>Email del cliente</p>
    <input type="email" id="nombre">
    <p>Teléfono del cliente</p>
    <input type="text" id="nombre">
    <button>Enviar</button>
  </body>
</html>
```

### ejemplo con estilo
<small>Creado: 2025-09-28 22:28</small>

`302-ejemplo con estilo.html`

```html
<html>
  <head>
    <style>
      *{padding:0px;margin:0px;}
      html{background:grey;}
      body{background:white;padding:20px;margin:auto;width:50%;}
      input,button{width:100%;}
    </style>
  </head>
  <body>
    <p>Nombre del cliente</p>
    <input type="text" id="nombre">
    <p>Email del cliente</p>
    <input type="email" id="nombre">
    <p>Teléfono del cliente</p>
    <input type="text" id="nombre">
    <button>Enviar</button>
  </body>
</html>
```

### javascript muy sencillo
<small>Creado: 2025-09-28 22:28</small>

`303-javascript muy sencillo.html`

```html
<html>
  <head>
    <style>
      *{padding:0px;margin:0px;}
      html{background:grey;}
      body{background:white;padding:20px;margin:auto;width:50%;}
      input,button{width:100%;}
    </style>
  </head>
  <body>
    <p>Nombre del cliente</p>
    <input type="text" id="nombre">
    <p>Email del cliente</p>
    <input type="email" id="email">
    <p>Teléfono del cliente</p>
    <input type="text" id="telefono">
    <button>Enviar</button>
  </body>
  <script>
    document.querySelector("button").onclick = function(){
      var cliente = [];
      cliente['nombre'] = document.querySelector("#nombre").value;
      cliente['email'] = document.querySelector("#email").value;
      cliente['telefono'] = document.querySelector("#telefono").value;
      console.log(cliente)
    }
  </script>
</html>
```

### javascript selectores
<small>Creado: 2025-09-28 22:28</small>

`304-javascript selectores.html`

```html
<html>
  <head>
    <style>
      *{padding:0px;margin:0px;}
      html{background:grey;}
      body{background:white;padding:20px;margin:auto;width:50%;}
      input,button{width:100%;}
    </style>
  </head>
  <body>
    <p>Nombre del cliente</p>
    <input type="text" id="nombre">
    <p>Email del cliente</p>
    <input type="email" id="email">
    <p>Teléfono del cliente</p>
    <input type="text" id="telefono">
    <button>Enviar</button>
  </body>
  <script>
    document.querySelector("button").onclick = function(){
      var cliente = [];
      cliente['nombre'] = document.querySelector("#nombre").value;
      cliente['email'] = document.querySelector("#email").value;
      cliente['telefono'] = document.querySelector("#telefono").value;
      console.log(cliente)
    }
  </script>
</html>
```


<a id="ejercicio-crud-2"></a>
## Ejercicio CRUD 2

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/010-Ejercicio%20CRUD%202)

### Ejercicio
<small>Creado: 2025-09-28 22:28</small>

`401-Ejercicio.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button>

    </div>
  </body>
</html>
```

### Ejercicio
<small>Creado: 2025-09-28 22:28</small>

`402-Ejercicio.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button> 
    </div>
    <table>
    </table>
    <script>
        // Creo un array vacio
        let clientes = [];
        /////////////////// CREATE ///////////////////////////
        
        // Selecciono el boton
        let boton = document.querySelector("button")
        // Accion de pulsar en el boton
        boton.onclick = function(){
          // Atrapo el nombre
          let nombre = document.querySelector("#nombre").value
          // Atrapo el email
          let email = document.querySelector("#email").value
          // Añado el cliente actual al array
          clientes.push({"nombre":nombre,"email":email})
          // Lo saco por consola
          console.log(clientes)
          // Borramos los campos
          document.querySelector("#nombre").value = ""
          document.querySelector("#email").value = ""
        }
        
        /////////////////// READ ///////////////////////////
        
        
        
    </script>
  </body>
</html>
```

### leer
<small>Creado: 2025-09-28 22:28</small>

`403-leer.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button> 
    </div>
    <table>
    </table>
    <script>
        // Creo un array vacio
        let clientes = [];
        /////////////////// CREATE ///////////////////////////
        
        // Selecciono el boton
        let boton = document.querySelector("button")
        // Accion de pulsar en el boton
        boton.onclick = function(){
          // Atrapo el nombre
          let nombre = document.querySelector("#nombre").value
          // Atrapo el email
          let email = document.querySelector("#email").value
          // Añado el cliente actual al array
          clientes.push({"nombre":nombre,"email":email})
          // Lo saco por consola
          console.log(clientes)
          // Borramos los campos
          document.querySelector("#nombre").value = ""
          document.querySelector("#email").value = ""
          // Re-renderizo la tabla
          pueblaTabla()
        }
        
        /////////////////// READ ///////////////////////////
        
        function pueblaTabla(){
          // Primero creo la cabecera de la tabla
          let cadena = "<tr><th>Nombre</th><th>Email</th></tr>";
          // Repaso uno a uno los clientes
          clientes.forEach(function(cliente){
             cadena += "<tr><td>"+cliente.nombre+"</td><td>"+cliente.email+"</td></tr>"
          })
          document.querySelector("table").innerHTML = cadena
        }
        
    </script>
  </body>
</html>
```

### estilo
<small>Creado: 2025-09-28 22:28</small>

`404-estilo.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
    <style>
      /* ===== Design tokens ===== */
      :root{
        --bg: hsl(220 15% 10%);
        --panel: hsl(220 20% 14%);
        --panel-2: hsl(220 18% 16%);
        --text: hsl(210 20% 98%);
        --muted: hsl(220 10% 70%);
        --accent: hsl(199 90% 56%);
        --accent-2: hsl(213 90% 62%);
        --success: hsl(142 60% 45%);
        --danger: hsl(2 85% 62%);
        --ring: hsla(199, 90%, 56%, .35);
        --radius: 14px;
        --shadow: 0 10px 30px rgba(0,0,0,.35);
        --shadow-sm: 0 4px 16px rgba(0,0,0,.25);
        --border: 1px solid hsl(220 18% 22%);
        --font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
                 Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
      }

      /* Light mode tweak if user prefers */
      @media (prefers-color-scheme: light){
        :root{
          --bg: hsl(210 20% 98%);
          --panel: hsl(0 0% 100%);
          --panel-2: hsl(0 0% 100%);
          --text: hsl(222 18% 16%);
          --muted: hsl(222 10% 40%);
          --accent: hsl(210 100% 52%);
          --accent-2: hsl(221 89% 63%);
          --ring: hsla(210, 100%, 52%, .32);
          --border: 1px solid hsl(220 15% 88%);
          --shadow: 0 10px 30px rgba(2,12,27,.08);
          --shadow-sm: 0 4px 16px rgba(2,12,27,.06);
        }
      }

      /* ===== Global ===== */
      *,
      *::before,
      *::after{ box-sizing: border-box; }

      html, body{
        height: 100%;
      }

      body{
        margin: 0;
        font-family: var(--font);
        color: var(--text);
        background:
          radial-gradient(1200px 600px at 10% -10%, rgba(255,255,255,.06), transparent 50%),
          radial-gradient(1200px 600px at 110% 10%, rgba(255,255,255,.05), transparent 50%),
          var(--bg);
        display: grid;
        align-content: start;
        gap: 24px;
        padding: 40px 20px 80px;
      }

      /* Center content and set widths without altering HTML */
      #formulario, table{
        width: min(980px, 100%);
        margin-inline: auto;
      }

      /* ===== Form card ===== */
      #formulario{
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr auto;
        gap: 14px;
        align-items: start;
      }

      #formulario input[type="text"]{
        appearance: none;
        width: 100%;
        padding: 12px 14px;
        border-radius: 10px;
        border: var(--border);
        background: var(--panel-2);
        color: var(--text);
        outline: none;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
        transition: border-color .2s ease, box-shadow .2s ease, transform .04s ease;
      }

      #formulario input::placeholder{
        color: var(--muted);
      }

      #formulario input:focus{
        border-color: var(--accent);
        box-shadow: 0 0 0 6px var(--ring), inset 0 1px 0 rgba(255,255,255,.03);
      }

      #formulario button{
        justify-self: end;
        padding: 12px 18px;
        border: 0;
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: .2px;
        color: white;
        cursor: pointer;
        background: linear-gradient(135deg, var(--accent), var(--accent-2));
        box-shadow: var(--shadow-sm);
        transition: transform .06s ease, filter .2s ease, box-shadow .2s ease;
      }

      #formulario button:hover{
        filter: brightness(1.06) saturate(1.05);
        box-shadow: 0 8px 22px rgba(0,0,0,.25);
      }

      #formulario button:active{
        transform: translateY(1px) scale(.995);
      }

      /* Small screens: stack nicely */
      @media (max-width: 720px){
        #formulario{
          grid-template-columns: 1fr;
        }
        #formulario button{
          justify-self: stretch;
        }
      }

      /* ===== Table styling ===== */
      table{
        border-collapse: separate;
        border-spacing: 0;
        width: min(980px, 100%);
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        overflow: hidden;
        box-shadow: var(--shadow);
      }

      table tr:first-child th{
        position: sticky; /* stays at top if page scrolls */
        top: 0;
        background:
          linear-gradient(0deg, rgba(255,255,255,.02), rgba(255,255,255,.02)),
          var(--panel-2);
        color: var(--text);
        text-align: left;
        font-weight: 800;
        letter-spacing: .3px;
      }

      th, td{
        padding: 14px 16px;
        border-bottom: 1px solid color-mix(in oklab, currentColor 12%, transparent);
      }

      tr:last-child td{
        border-bottom: none;
      }

      /* Zebra stripes & hover */
      table tr:nth-child(odd){
        background: color-mix(in oklab, var(--panel) 92%, black 8%);
      }

      table tr:nth-child(even){
        background: var(--panel);
      }

      table tr:hover td{
        background: color-mix(in oklab, var(--panel) 85%, var(--accent) 5%);
      }

      /* Subtle row entrance animation when table re-renders */
      @keyframes rowIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
      }
      table tr{
        animation: rowIn .25s ease both;
      }

      /* Make columns breathe on small screens */
      @media (max-width: 560px){
        th, td{ padding: 12px 14px; }
      }

      /* ===== Focus visibility for a11y ===== */
      :focus-visible{
        outline: 0;
        box-shadow: 0 0 0 6px var(--ring) !important;
        border-color: var(--accent) !important;
        border-radius: 10px;
      }

      /* ===== Nice scrollbars (where supported) ===== */
      :root{
        scrollbar-color: color-mix(in oklab, var(--panel) 65%, var(--accent) 35%) transparent;
        scrollbar-width: thin;
      }
      ::-webkit-scrollbar{ height: 10px; width: 10px; }
      ::-webkit-scrollbar-track{ background: transparent; }
      ::-webkit-scrollbar-thumb{
        background: color-mix(in oklab, var(--panel) 60%, var(--accent) 40%);
        border-radius: 999px;
        border: 2px solid transparent;
        background-clip: padding-box;
      }

    </style>
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button> 
    </div>
    <table>
    </table>
    <script>
        // Creo un array vacio
        let clientes = [];
        /////////////////// CREATE ///////////////////////////
        
        // Selecciono el boton
        let boton = document.querySelector("button")
        // Accion de pulsar en el boton
        boton.onclick = function(){
          // Atrapo el nombre
          let nombre = document.querySelector("#nombre").value
          // Atrapo el email
          let email = document.querySelector("#email").value
          // Añado el cliente actual al array
          clientes.push({"nombre":nombre,"email":email})
          // Lo saco por consola
          console.log(clientes)
          // Borramos los campos
          document.querySelector("#nombre").value = ""
          document.querySelector("#email").value = ""
          // Re-renderizo la tabla
          pueblaTabla()
        }
        
        /////////////////// READ ///////////////////////////
        
        function pueblaTabla(){
          // Primero creo la cabecera de la tabla
          let cadena = "<tr><th>Nombre</th><th>Email</th></tr>";
          // Repaso uno a uno los clientes
          clientes.forEach(function(cliente){
             cadena += "<tr><td>"+cliente.nombre+"</td><td>"+cliente.email+"</td></tr>"
          })
          document.querySelector("table").innerHTML = cadena
        }
        
    </script>
  </body>
</html>
```

### encapsular
<small>Creado: 2025-09-28 22:28</small>

`405-encapsular.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
    <style>
      /* ===== Design tokens ===== */
      :root{
        --bg: hsl(220 15% 10%);
        --panel: hsl(220 20% 14%);
        --panel-2: hsl(220 18% 16%);
        --text: hsl(210 20% 98%);
        --muted: hsl(220 10% 70%);
        --accent: hsl(199 90% 56%);
        --accent-2: hsl(213 90% 62%);
        --success: hsl(142 60% 45%);
        --danger: hsl(2 85% 62%);
        --ring: hsla(199, 90%, 56%, .35);
        --radius: 14px;
        --shadow: 0 10px 30px rgba(0,0,0,.35);
        --shadow-sm: 0 4px 16px rgba(0,0,0,.25);
        --border: 1px solid hsl(220 18% 22%);
        --font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
                 Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
      }

      /* Light mode tweak if user prefers */
      @media (prefers-color-scheme: light){
        :root{
          --bg: hsl(210 20% 98%);
          --panel: hsl(0 0% 100%);
          --panel-2: hsl(0 0% 100%);
          --text: hsl(222 18% 16%);
          --muted: hsl(222 10% 40%);
          --accent: hsl(210 100% 52%);
          --accent-2: hsl(221 89% 63%);
          --ring: hsla(210, 100%, 52%, .32);
          --border: 1px solid hsl(220 15% 88%);
          --shadow: 0 10px 30px rgba(2,12,27,.08);
          --shadow-sm: 0 4px 16px rgba(2,12,27,.06);
        }
      }

      /* ===== Global ===== */
      *,
      *::before,
      *::after{ box-sizing: border-box; }

      html, body{
        height: 100%;
      }

      body{
        margin: 0;
        font-family: var(--font);
        color: var(--text);
        background:
          radial-gradient(1200px 600px at 10% -10%, rgba(255,255,255,.06), transparent 50%),
          radial-gradient(1200px 600px at 110% 10%, rgba(255,255,255,.05), transparent 50%),
          var(--bg);
        display: grid;
        align-content: start;
        gap: 24px;
        padding: 40px 20px 80px;
      }

      /* Center content and set widths without altering HTML */
      #formulario, table{
        width: min(980px, 100%);
        margin-inline: auto;
      }

      /* ===== Form card ===== */
      #formulario{
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr auto;
        gap: 14px;
        align-items: start;
      }

      #formulario input[type="text"]{
        appearance: none;
        width: 100%;
        padding: 12px 14px;
        border-radius: 10px;
        border: var(--border);
        background: var(--panel-2);
        color: var(--text);
        outline: none;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
        transition: border-color .2s ease, box-shadow .2s ease, transform .04s ease;
      }

      #formulario input::placeholder{
        color: var(--muted);
      }

      #formulario input:focus{
        border-color: var(--accent);
        box-shadow: 0 0 0 6px var(--ring), inset 0 1px 0 rgba(255,255,255,.03);
      }

      #formulario button{
        justify-self: end;
        padding: 12px 18px;
        border: 0;
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: .2px;
        color: white;
        cursor: pointer;
        background: linear-gradient(135deg, var(--accent), var(--accent-2));
        box-shadow: var(--shadow-sm);
        transition: transform .06s ease, filter .2s ease, box-shadow .2s ease;
      }

      #formulario button:hover{
        filter: brightness(1.06) saturate(1.05);
        box-shadow: 0 8px 22px rgba(0,0,0,.25);
      }

      #formulario button:active{
        transform: translateY(1px) scale(.995);
      }

      /* Small screens: stack nicely */
      @media (max-width: 720px){
        #formulario{
          grid-template-columns: 1fr;
        }
        #formulario button{
          justify-self: stretch;
        }
      }

      /* ===== Table styling ===== */
      table{
        border-collapse: separate;
        border-spacing: 0;
        width: min(980px, 100%);
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        overflow: hidden;
        box-shadow: var(--shadow);
      }

      table tr:first-child th{
        position: sticky; /* stays at top if page scrolls */
        top: 0;
        background:
          linear-gradient(0deg, rgba(255,255,255,.02), rgba(255,255,255,.02)),
          var(--panel-2);
        color: var(--text);
        text-align: left;
        font-weight: 800;
        letter-spacing: .3px;
      }

      th, td{
        padding: 14px 16px;
        border-bottom: 1px solid color-mix(in oklab, currentColor 12%, transparent);
      }

      tr:last-child td{
        border-bottom: none;
      }

      /* Zebra stripes & hover */
      table tr:nth-child(odd){
        background: color-mix(in oklab, var(--panel) 92%, black 8%);
      }

      table tr:nth-child(even){
        background: var(--panel);
      }

      table tr:hover td{
        background: color-mix(in oklab, var(--panel) 85%, var(--accent) 5%);
      }

      /* Subtle row entrance animation when table re-renders */
      @keyframes rowIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
      }
      table tr{
        animation: rowIn .25s ease both;
      }

      /* Make columns breathe on small screens */
      @media (max-width: 560px){
        th, td{ padding: 12px 14px; }
      }

      /* ===== Focus visibility for a11y ===== */
      :focus-visible{
        outline: 0;
        box-shadow: 0 0 0 6px var(--ring) !important;
        border-color: var(--accent) !important;
        border-radius: 10px;
      }

      /* ===== Nice scrollbars (where supported) ===== */
      :root{
        scrollbar-color: color-mix(in oklab, var(--panel) 65%, var(--accent) 35%) transparent;
        scrollbar-width: thin;
      }
      ::-webkit-scrollbar{ height: 10px; width: 10px; }
      ::-webkit-scrollbar-track{ background: transparent; }
      ::-webkit-scrollbar-thumb{
        background: color-mix(in oklab, var(--panel) 60%, var(--accent) 40%);
        border-radius: 999px;
        border: 2px solid transparent;
        background-clip: padding-box;
      }

    </style>
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button> 
    </div>
    <table>
    </table>
    <script>
        // Creo un array vacio
        let clientes = [];
        /////////////////// CREATE ///////////////////////////
        
        // Selecciono el boton
        let boton = document.querySelector("button")
        // Si pulso el boton, se añade el registro
        boton.onclick = function(){
          anadeRegistro()
        }
        // Si pulso una tecla
        document.onkeypress = function(event){
          // Y la tecla es la tecla enter
          if(event.key == "Enter"){
            anadeRegistro() // En ese caso se añade el registro
          }
        }
        function anadeRegistro(){
          // Atrapo el nombre
          let nombre = document.querySelector("#nombre").value
          // Atrapo el email
          let email = document.querySelector("#email").value
          // Añado el cliente actual al array
          clientes.push({"nombre":nombre,"email":email})
          // Lo saco por consola
          console.log(clientes)
          // Borramos los campos
          document.querySelector("#nombre").value = ""
          document.querySelector("#email").value = ""
          // Re-renderizo la tabla
          pueblaTabla()
        }
        /////////////////// READ ///////////////////////////
        
        function pueblaTabla(){
          // Primero creo la cabecera de la tabla
          let cadena = "<tr><th>Nombre</th><th>Email</th></tr>";
          // Repaso uno a uno los clientes
          clientes.forEach(function(cliente){
             cadena += "<tr><td>"+cliente.nombre+"</td><td>"+cliente.email+"</td></tr>"
          })
          document.querySelector("table").innerHTML = cadena
        }
        
    </script>
  </body>
</html>
```

### eliminar
<small>Creado: 2025-09-28 22:28</small>

`406-eliminar.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
    <style>
      /* ===== Design tokens ===== */
      :root{
        --bg: hsl(220 15% 10%);
        --panel: hsl(220 20% 14%);
        --panel-2: hsl(220 18% 16%);
        --text: hsl(210 20% 98%);
        --muted: hsl(220 10% 70%);
        --accent: hsl(199 90% 56%);
        --accent-2: hsl(213 90% 62%);
        --success: hsl(142 60% 45%);
        --danger: hsl(2 85% 62%);
        --ring: hsla(199, 90%, 56%, .35);
        --radius: 14px;
        --shadow: 0 10px 30px rgba(0,0,0,.35);
        --shadow-sm: 0 4px 16px rgba(0,0,0,.25);
        --border: 1px solid hsl(220 18% 22%);
        --font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
                 Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
      }

      /* Light mode tweak if user prefers */
      @media (prefers-color-scheme: light){
        :root{
          --bg: hsl(210 20% 98%);
          --panel: hsl(0 0% 100%);
          --panel-2: hsl(0 0% 100%);
          --text: hsl(222 18% 16%);
          --muted: hsl(222 10% 40%);
          --accent: hsl(210 100% 52%);
          --accent-2: hsl(221 89% 63%);
          --ring: hsla(210, 100%, 52%, .32);
          --border: 1px solid hsl(220 15% 88%);
          --shadow: 0 10px 30px rgba(2,12,27,.08);
          --shadow-sm: 0 4px 16px rgba(2,12,27,.06);
        }
      }

      /* ===== Global ===== */
      *,
      *::before,
      *::after{ box-sizing: border-box; }

      html, body{
        height: 100%;
      }

      body{
        margin: 0;
        font-family: var(--font);
        color: var(--text);
        background:
          radial-gradient(1200px 600px at 10% -10%, rgba(255,255,255,.06), transparent 50%),
          radial-gradient(1200px 600px at 110% 10%, rgba(255,255,255,.05), transparent 50%),
          var(--bg);
        display: grid;
        align-content: start;
        gap: 24px;
        padding: 40px 20px 80px;
      }

      /* Center content and set widths without altering HTML */
      #formulario, table{
        width: min(980px, 100%);
        margin-inline: auto;
      }

      /* ===== Form card ===== */
      #formulario{
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr auto;
        gap: 14px;
        align-items: start;
      }

      #formulario input[type="text"]{
        appearance: none;
        width: 100%;
        padding: 12px 14px;
        border-radius: 10px;
        border: var(--border);
        background: var(--panel-2);
        color: var(--text);
        outline: none;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
        transition: border-color .2s ease, box-shadow .2s ease, transform .04s ease;
      }

      #formulario input::placeholder{
        color: var(--muted);
      }

      #formulario input:focus{
        border-color: var(--accent);
        box-shadow: 0 0 0 6px var(--ring), inset 0 1px 0 rgba(255,255,255,.03);
      }

      #formulario button{
        justify-self: end;
        padding: 12px 18px;
        border: 0;
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: .2px;
        color: white;
        cursor: pointer;
        background: linear-gradient(135deg, var(--accent), var(--accent-2));
        box-shadow: var(--shadow-sm);
        transition: transform .06s ease, filter .2s ease, box-shadow .2s ease;
      }

      #formulario button:hover{
        filter: brightness(1.06) saturate(1.05);
        box-shadow: 0 8px 22px rgba(0,0,0,.25);
      }

      #formulario button:active{
        transform: translateY(1px) scale(.995);
      }

      /* Small screens: stack nicely */
      @media (max-width: 720px){
        #formulario{
          grid-template-columns: 1fr;
        }
        #formulario button{
          justify-self: stretch;
        }
      }

      /* ===== Table styling ===== */
      table{
        border-collapse: separate;
        border-spacing: 0;
        width: min(980px, 100%);
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        overflow: hidden;
        box-shadow: var(--shadow);
      }

      table tr:first-child th{
        position: sticky; /* stays at top if page scrolls */
        top: 0;
        background:
          linear-gradient(0deg, rgba(255,255,255,.02), rgba(255,255,255,.02)),
          var(--panel-2);
        color: var(--text);
        text-align: left;
        font-weight: 800;
        letter-spacing: .3px;
      }

      th, td{
        padding: 14px 16px;
        border-bottom: 1px solid color-mix(in oklab, currentColor 12%, transparent);
      }

      tr:last-child td{
        border-bottom: none;
      }

      /* Zebra stripes & hover */
      table tr:nth-child(odd){
        background: color-mix(in oklab, var(--panel) 92%, black 8%);
      }

      table tr:nth-child(even){
        background: var(--panel);
      }

      table tr:hover td{
        background: color-mix(in oklab, var(--panel) 85%, var(--accent) 5%);
      }

      /* Subtle row entrance animation when table re-renders */
      @keyframes rowIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
      }
      table tr{
        animation: rowIn .25s ease both;
      }

      /* Make columns breathe on small screens */
      @media (max-width: 560px){
        th, td{ padding: 12px 14px; }
      }

      /* ===== Focus visibility for a11y ===== */
      :focus-visible{
        outline: 0;
        box-shadow: 0 0 0 6px var(--ring) !important;
        border-color: var(--accent) !important;
        border-radius: 10px;
      }

      /* ===== Nice scrollbars (where supported) ===== */
      :root{
        scrollbar-color: color-mix(in oklab, var(--panel) 65%, var(--accent) 35%) transparent;
        scrollbar-width: thin;
      }
      ::-webkit-scrollbar{ height: 10px; width: 10px; }
      ::-webkit-scrollbar-track{ background: transparent; }
      ::-webkit-scrollbar-thumb{
        background: color-mix(in oklab, var(--panel) 60%, var(--accent) 40%);
        border-radius: 999px;
        border: 2px solid transparent;
        background-clip: padding-box;
      }

    </style>
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button> 
    </div>
    <table>
    </table>
    <div id="formularioeliminar">
      <input type="text" id="ideliminar" placeholder="Introduce el ID para eliminar">
      <button id="procesaeliminar">Eliminar</button>
    </div>
    <script>
        // Creo un array vacio
        let clientes = [];
        /////////////////// CREATE ///////////////////////////
        
        // Selecciono el boton
        let boton = document.querySelector("button")
        // Si pulso el boton, se añade el registro
        boton.onclick = function(){
          anadeRegistro()
        }
        // Si pulso una tecla
        document.onkeypress = function(event){
          // Y la tecla es la tecla enter
          if(event.key == "Enter"){
            anadeRegistro() // En ese caso se añade el registro
          }
        }
        function anadeRegistro(){
          // Atrapo el nombre
          let nombre = document.querySelector("#nombre").value
          // Atrapo el email
          let email = document.querySelector("#email").value
          // Añado el cliente actual al array
          clientes.push({"nombre":nombre,"email":email})
          // Lo saco por consola
          console.log(clientes)
          // Borramos los campos
          document.querySelector("#nombre").value = ""
          document.querySelector("#email").value = ""
          // Re-renderizo la tabla
          pueblaTabla()
        }
        /////////////////// READ ///////////////////////////
        
        function pueblaTabla(){
          // Primero creo la cabecera de la tabla
          let cadena = "<tr><th>Nombre</th><th>Email</th></tr>";
          // Repaso uno a uno los clientes
          clientes.forEach(function(cliente){
             cadena += "<tr><td>"+cliente.nombre+"</td><td>"+cliente.email+"</td></tr>"
          })
          document.querySelector("table").innerHTML = cadena
        }
        
        /////////////////// DELETE ///////////////////////////
        
        
        
    </script>
  </body>
</html>
```

### Tratamiento de arrays
<small>Creado: 2025-09-28 22:28</small>

`407-Tratamiento de arrays.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
    <style>
      /* ===== Design tokens ===== */
      :root{
        --bg: hsl(220 15% 10%);
        --panel: hsl(220 20% 14%);
        --panel-2: hsl(220 18% 16%);
        --text: hsl(210 20% 98%);
        --muted: hsl(220 10% 70%);
        --accent: hsl(199 90% 56%);
        --accent-2: hsl(213 90% 62%);
        --success: hsl(142 60% 45%);
        --danger: hsl(2 85% 62%);
        --ring: hsla(199, 90%, 56%, .35);
        --radius: 14px;
        --shadow: 0 10px 30px rgba(0,0,0,.35);
        --shadow-sm: 0 4px 16px rgba(0,0,0,.25);
        --border: 1px solid hsl(220 18% 22%);
        --font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
                 Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
      }

      /* Light mode tweak if user prefers */
      @media (prefers-color-scheme: light){
        :root{
          --bg: hsl(210 20% 98%);
          --panel: hsl(0 0% 100%);
          --panel-2: hsl(0 0% 100%);
          --text: hsl(222 18% 16%);
          --muted: hsl(222 10% 40%);
          --accent: hsl(210 100% 52%);
          --accent-2: hsl(221 89% 63%);
          --ring: hsla(210, 100%, 52%, .32);
          --border: 1px solid hsl(220 15% 88%);
          --shadow: 0 10px 30px rgba(2,12,27,.08);
          --shadow-sm: 0 4px 16px rgba(2,12,27,.06);
        }
      }

      /* ===== Global ===== */
      *,
      *::before,
      *::after{ box-sizing: border-box; }

      html, body{
        height: 100%;
      }

      body{
        margin: 0;
        font-family: var(--font);
        color: var(--text);
        background:
          radial-gradient(1200px 600px at 10% -10%, rgba(255,255,255,.06), transparent 50%),
          radial-gradient(1200px 600px at 110% 10%, rgba(255,255,255,.05), transparent 50%),
          var(--bg);
        display: grid;
        align-content: start;
        gap: 24px;
        padding: 40px 20px 80px;
      }

      /* Center content and set widths without altering HTML */
      #formulario, table{
        width: min(980px, 100%);
        margin-inline: auto;
      }

      /* ===== Form card ===== */
      #formulario{
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr auto;
        gap: 14px;
        align-items: start;
      }

      #formulario input[type="text"]{
        appearance: none;
        width: 100%;
        padding: 12px 14px;
        border-radius: 10px;
        border: var(--border);
        background: var(--panel-2);
        color: var(--text);
        outline: none;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
        transition: border-color .2s ease, box-shadow .2s ease, transform .04s ease;
      }

      #formulario input::placeholder{
        color: var(--muted);
      }

      #formulario input:focus{
        border-color: var(--accent);
        box-shadow: 0 0 0 6px var(--ring), inset 0 1px 0 rgba(255,255,255,.03);
      }

      #formulario button{
        justify-self: end;
        padding: 12px 18px;
        border: 0;
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: .2px;
        color: white;
        cursor: pointer;
        background: linear-gradient(135deg, var(--accent), var(--accent-2));
        box-shadow: var(--shadow-sm);
        transition: transform .06s ease, filter .2s ease, box-shadow .2s ease;
      }

      #formulario button:hover{
        filter: brightness(1.06) saturate(1.05);
        box-shadow: 0 8px 22px rgba(0,0,0,.25);
      }

      #formulario button:active{
        transform: translateY(1px) scale(.995);
      }

      /* Small screens: stack nicely */
      @media (max-width: 720px){
        #formulario{
          grid-template-columns: 1fr;
        }
        #formulario button{
          justify-self: stretch;
        }
      }

      /* ===== Table styling ===== */
      table{
        border-collapse: separate;
        border-spacing: 0;
        width: min(980px, 100%);
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        overflow: hidden;
        box-shadow: var(--shadow);
      }

      table tr:first-child th{
        position: sticky; /* stays at top if page scrolls */
        top: 0;
        background:
          linear-gradient(0deg, rgba(255,255,255,.02), rgba(255,255,255,.02)),
          var(--panel-2);
        color: var(--text);
        text-align: left;
        font-weight: 800;
        letter-spacing: .3px;
      }

      th, td{
        padding: 14px 16px;
        border-bottom: 1px solid color-mix(in oklab, currentColor 12%, transparent);
      }

      tr:last-child td{
        border-bottom: none;
      }

      /* Zebra stripes & hover */
      table tr:nth-child(odd){
        background: color-mix(in oklab, var(--panel) 92%, black 8%);
      }

      table tr:nth-child(even){
        background: var(--panel);
      }

      table tr:hover td{
        background: color-mix(in oklab, var(--panel) 85%, var(--accent) 5%);
      }

      /* Subtle row entrance animation when table re-renders */
      @keyframes rowIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
      }
      table tr{
        animation: rowIn .25s ease both;
      }

      /* Make columns breathe on small screens */
      @media (max-width: 560px){
        th, td{ padding: 12px 14px; }
      }

      /* ===== Focus visibility for a11y ===== */
      :focus-visible{
        outline: 0;
        box-shadow: 0 0 0 6px var(--ring) !important;
        border-color: var(--accent) !important;
        border-radius: 10px;
      }

      /* ===== Nice scrollbars (where supported) ===== */
      :root{
        scrollbar-color: color-mix(in oklab, var(--panel) 65%, var(--accent) 35%) transparent;
        scrollbar-width: thin;
      }
      ::-webkit-scrollbar{ height: 10px; width: 10px; }
      ::-webkit-scrollbar-track{ background: transparent; }
      ::-webkit-scrollbar-thumb{
        background: color-mix(in oklab, var(--panel) 60%, var(--accent) 40%);
        border-radius: 999px;
        border: 2px solid transparent;
        background-clip: padding-box;
      }

    </style>
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button> 
    </div>
    <table>
    </table>
    <div id="formularioeliminar">
      <input type="text" id="ideliminar" placeholder="Introduce el ID para eliminar">
      <button id="procesaeliminar">Eliminar</button>
    </div>
    <script>
        // Creo un array vacio
        let clientes = [];
        /////////////////// CREATE ///////////////////////////
        
        // Selecciono el boton
        let boton = document.querySelector("button")
        // Si pulso el boton, se añade el registro
        boton.onclick = function(){
          anadeRegistro()
        }
        // Si pulso una tecla
        document.onkeypress = function(event){
          // Y la tecla es la tecla enter
          if(event.key == "Enter"){
            anadeRegistro() // En ese caso se añade el registro
          }
        }
        function anadeRegistro(){
          // Atrapo el nombre
          let nombre = document.querySelector("#nombre").value
          // Atrapo el email
          let email = document.querySelector("#email").value
          // Añado el cliente actual al array
          clientes.push({"nombre":nombre,"email":email})
          // Lo saco por consola
          console.log(clientes)
          // Borramos los campos
          document.querySelector("#nombre").value = ""
          document.querySelector("#email").value = ""
          // Re-renderizo la tabla
          pueblaTabla()
        }
        /////////////////// READ ///////////////////////////
        
        function pueblaTabla(){
          // Primero creo la cabecera de la tabla
          let cadena = "<tr><th>Nombre</th><th>Email</th></tr>";
          // Repaso uno a uno los clientes
          clientes.forEach(function(cliente){
             cadena += "<tr><td>"+cliente.nombre+"</td><td>"+cliente.email+"</td></tr>"
          })
          document.querySelector("table").innerHTML = cadena
        }
        
        /////////////////// DELETE ///////////////////////////
        
        // Primero cojo el botón
        var botoneliminar = document.querySelector("#procesaeliminar");
        // Cuando pulso el botón
        botoneliminar.onclick = function(){
          // Tomo el id a eliminar
          let ideliminar = document.querySelector("#ideliminar").value
          // Y ahora elimino el elemento del array
          clientes.splice(ideliminar,1); /////////////// IMPORTANTE
          // Y ahora re-renderizo la tabla
          pueblaTabla();
        }
        
        
        
    </script>
  </body>
</html>
```

### formulario de actualizacion
<small>Creado: 2025-09-28 22:28</small>

`408-formulario de actualizacion.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
    <style>
      /* ===== Design tokens ===== */
      :root{
        --bg: hsl(220 15% 10%);
        --panel: hsl(220 20% 14%);
        --panel-2: hsl(220 18% 16%);
        --text: hsl(210 20% 98%);
        --muted: hsl(220 10% 70%);
        --accent: hsl(199 90% 56%);
        --accent-2: hsl(213 90% 62%);
        --success: hsl(142 60% 45%);
        --danger: hsl(2 85% 62%);
        --ring: hsla(199, 90%, 56%, .35);
        --radius: 14px;
        --shadow: 0 10px 30px rgba(0,0,0,.35);
        --shadow-sm: 0 4px 16px rgba(0,0,0,.25);
        --border: 1px solid hsl(220 18% 22%);
        --font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
                 Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
      }

      /* Light mode tweak if user prefers */
      @media (prefers-color-scheme: light){
        :root{
          --bg: hsl(210 20% 98%);
          --panel: hsl(0 0% 100%);
          --panel-2: hsl(0 0% 100%);
          --text: hsl(222 18% 16%);
          --muted: hsl(222 10% 40%);
          --accent: hsl(210 100% 52%);
          --accent-2: hsl(221 89% 63%);
          --ring: hsla(210, 100%, 52%, .32);
          --border: 1px solid hsl(220 15% 88%);
          --shadow: 0 10px 30px rgba(2,12,27,.08);
          --shadow-sm: 0 4px 16px rgba(2,12,27,.06);
        }
      }

      /* ===== Global ===== */
      *,
      *::before,
      *::after{ box-sizing: border-box; }

      html, body{
        height: 100%;
      }

      body{
        margin: 0;
        font-family: var(--font);
        color: var(--text);
        background:
          radial-gradient(1200px 600px at 10% -10%, rgba(255,255,255,.06), transparent 50%),
          radial-gradient(1200px 600px at 110% 10%, rgba(255,255,255,.05), transparent 50%),
          var(--bg);
        display: grid;
        align-content: start;
        gap: 24px;
        padding: 40px 20px 80px;
      }

      /* Center content and set widths without altering HTML */
      #formulario, table{
        width: min(980px, 100%);
        margin-inline: auto;
      }

      /* ===== Form card ===== */
      #formulario{
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr auto;
        gap: 14px;
        align-items: start;
      }

      #formulario input[type="text"]{
        appearance: none;
        width: 100%;
        padding: 12px 14px;
        border-radius: 10px;
        border: var(--border);
        background: var(--panel-2);
        color: var(--text);
        outline: none;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
        transition: border-color .2s ease, box-shadow .2s ease, transform .04s ease;
      }

      #formulario input::placeholder{
        color: var(--muted);
      }

      #formulario input:focus{
        border-color: var(--accent);
        box-shadow: 0 0 0 6px var(--ring), inset 0 1px 0 rgba(255,255,255,.03);
      }

      #formulario button{
        justify-self: end;
        padding: 12px 18px;
        border: 0;
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: .2px;
        color: white;
        cursor: pointer;
        background: linear-gradient(135deg, var(--accent), var(--accent-2));
        box-shadow: var(--shadow-sm);
        transition: transform .06s ease, filter .2s ease, box-shadow .2s ease;
      }

      #formulario button:hover{
        filter: brightness(1.06) saturate(1.05);
        box-shadow: 0 8px 22px rgba(0,0,0,.25);
      }

      #formulario button:active{
        transform: translateY(1px) scale(.995);
      }

      /* Small screens: stack nicely */
      @media (max-width: 720px){
        #formulario{
          grid-template-columns: 1fr;
        }
        #formulario button{
          justify-self: stretch;
        }
      }

      /* ===== Table styling ===== */
      table{
        border-collapse: separate;
        border-spacing: 0;
        width: min(980px, 100%);
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        overflow: hidden;
        box-shadow: var(--shadow);
      }

      table tr:first-child th{
        position: sticky; /* stays at top if page scrolls */
        top: 0;
        background:
          linear-gradient(0deg, rgba(255,255,255,.02), rgba(255,255,255,.02)),
          var(--panel-2);
        color: var(--text);
        text-align: left;
        font-weight: 800;
        letter-spacing: .3px;
      }

      th, td{
        padding: 14px 16px;
        border-bottom: 1px solid color-mix(in oklab, currentColor 12%, transparent);
      }

      tr:last-child td{
        border-bottom: none;
      }

      /* Zebra stripes & hover */
      table tr:nth-child(odd){
        background: color-mix(in oklab, var(--panel) 92%, black 8%);
      }

      table tr:nth-child(even){
        background: var(--panel);
      }

      table tr:hover td{
        background: color-mix(in oklab, var(--panel) 85%, var(--accent) 5%);
      }

      /* Subtle row entrance animation when table re-renders */
      @keyframes rowIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
      }
      table tr{
        animation: rowIn .25s ease both;
      }

      /* Make columns breathe on small screens */
      @media (max-width: 560px){
        th, td{ padding: 12px 14px; }
      }

      /* ===== Focus visibility for a11y ===== */
      :focus-visible{
        outline: 0;
        box-shadow: 0 0 0 6px var(--ring) !important;
        border-color: var(--accent) !important;
        border-radius: 10px;
      }

      /* ===== Nice scrollbars (where supported) ===== */
      :root{
        scrollbar-color: color-mix(in oklab, var(--panel) 65%, var(--accent) 35%) transparent;
        scrollbar-width: thin;
      }
      ::-webkit-scrollbar{ height: 10px; width: 10px; }
      ::-webkit-scrollbar-track{ background: transparent; }
      ::-webkit-scrollbar-thumb{
        background: color-mix(in oklab, var(--panel) 60%, var(--accent) 40%);
        border-radius: 999px;
        border: 2px solid transparent;
        background-clip: padding-box;
      }

    </style>
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button> 
    </div>
    <table>
    </table>
    <div id="formularioeliminar">
      <input type="text" id="ideliminar" placeholder="Introduce el ID para eliminar">
      <button id="procesaeliminar">Eliminar</button>
    </div>
    <div id="formularioactualizar">
      <input type="text" id="idactualizar" placeholder="Introduce el ID a actualizar">
      <input type="text" id="nuevonombre" placeholder="Introduce el nuevo nombre">
      <input type="text" id="nuevoemail" placeholder="Introduce el nuevo email">
      <button id="procesaactualizar">Actualizar</button>
    </div>
    <script>
        // Creo un array vacio
        let clientes = [];
        /////////////////// CREATE ///////////////////////////
        
        // Selecciono el boton
        let boton = document.querySelector("button")
        // Si pulso el boton, se añade el registro
        boton.onclick = function(){
          anadeRegistro()
        }
        // Si pulso una tecla
        document.onkeypress = function(event){
          // Y la tecla es la tecla enter
          if(event.key == "Enter"){
            anadeRegistro() // En ese caso se añade el registro
          }
        }
        function anadeRegistro(){
          // Atrapo el nombre
          let nombre = document.querySelector("#nombre").value
          // Atrapo el email
          let email = document.querySelector("#email").value
          // Añado el cliente actual al array
          clientes.push({"nombre":nombre,"email":email})
          // Lo saco por consola
          console.log(clientes)
          // Borramos los campos
          document.querySelector("#nombre").value = ""
          document.querySelector("#email").value = ""
          // Re-renderizo la tabla
          pueblaTabla()
        }
        /////////////////// READ ///////////////////////////
        
        function pueblaTabla(){
          // Primero creo la cabecera de la tabla
          let cadena = "<tr><th>Nombre</th><th>Email</th></tr>";
          // Repaso uno a uno los clientes
          clientes.forEach(function(cliente){
             cadena += "<tr><td>"+cliente.nombre+"</td><td>"+cliente.email+"</td></tr>"
          })
          document.querySelector("table").innerHTML = cadena
        }
        
        /////////////////// DELETE ///////////////////////////
        
        // Primero cojo el botón
        var botoneliminar = document.querySelector("#procesaeliminar");
        // Cuando pulso el botón
        botoneliminar.onclick = function(){
          // Tomo el id a eliminar
          let ideliminar = document.querySelector("#ideliminar").value
          // Y ahora elimino el elemento del array
          clientes.splice(ideliminar,1); /////////////// IMPORTANTE
          // Y ahora re-renderizo la tabla
          pueblaTabla();
        }
        
        /////////////////// UPDATE ///////////////////////////
        
        // Primero cojo el botón
        var botonactualizar = document.querySelector("#procesaactualizar");
        // Cuando pulso el botón
        botonactualizar.onclick = function(){
          // Primer cojo el id a actualizar
          let idactualizar = document.querySelector("#idactualizar").value
          // Ahora atrapo el dato del nuevo nombre
          let nuevonombre = document.querySelector("#nuevonombre").value
          // A continuación atrapo el dato del nuevo email
          let nuevoemail = document.querySelector("#nuevoemail").value
          // Edito el array y construyo un objeto
          clientes[idactualizar] = {"nombre":nuevonombre,"email":nuevoemail}
          // Y ahora re-renderizo la tabla
          pueblaTabla();
        }
    </script>
  </body>
</html>
```

### persisrtencia
<small>Creado: 2025-09-28 22:28</small>

`409-persisrtencia.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
    <style>
      /* ===== Design tokens ===== */
      :root{
        --bg: hsl(220 15% 10%);
        --panel: hsl(220 20% 14%);
        --panel-2: hsl(220 18% 16%);
        --text: hsl(210 20% 98%);
        --muted: hsl(220 10% 70%);
        --accent: hsl(199 90% 56%);
        --accent-2: hsl(213 90% 62%);
        --success: hsl(142 60% 45%);
        --danger: hsl(2 85% 62%);
        --ring: hsla(199, 90%, 56%, .35);
        --radius: 14px;
        --shadow: 0 10px 30px rgba(0,0,0,.35);
        --shadow-sm: 0 4px 16px rgba(0,0,0,.25);
        --border: 1px solid hsl(220 18% 22%);
        --font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
                 Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
      }

      /* Light mode tweak if user prefers */
      @media (prefers-color-scheme: light){
        :root{
          --bg: hsl(210 20% 98%);
          --panel: hsl(0 0% 100%);
          --panel-2: hsl(0 0% 100%);
          --text: hsl(222 18% 16%);
          --muted: hsl(222 10% 40%);
          --accent: hsl(210 100% 52%);
          --accent-2: hsl(221 89% 63%);
          --ring: hsla(210, 100%, 52%, .32);
          --border: 1px solid hsl(220 15% 88%);
          --shadow: 0 10px 30px rgba(2,12,27,.08);
          --shadow-sm: 0 4px 16px rgba(2,12,27,.06);
        }
      }

      /* ===== Global ===== */
      *,
      *::before,
      *::after{ box-sizing: border-box; }

      html, body{
        height: 100%;
      }

      body{
        margin: 0;
        font-family: var(--font);
        color: var(--text);
        background:
          radial-gradient(1200px 600px at 10% -10%, rgba(255,255,255,.06), transparent 50%),
          radial-gradient(1200px 600px at 110% 10%, rgba(255,255,255,.05), transparent 50%),
          var(--bg);
        display: grid;
        align-content: start;
        gap: 24px;
        padding: 40px 20px 80px;
      }

      /* Center content and set widths without altering HTML */
      #formulario, table{
        width: min(980px, 100%);
        margin-inline: auto;
      }

      /* ===== Form card ===== */
      #formulario{
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr auto;
        gap: 14px;
        align-items: start;
      }

      #formulario input[type="text"]{
        appearance: none;
        width: 100%;
        padding: 12px 14px;
        border-radius: 10px;
        border: var(--border);
        background: var(--panel-2);
        color: var(--text);
        outline: none;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
        transition: border-color .2s ease, box-shadow .2s ease, transform .04s ease;
      }

      #formulario input::placeholder{
        color: var(--muted);
      }

      #formulario input:focus{
        border-color: var(--accent);
        box-shadow: 0 0 0 6px var(--ring), inset 0 1px 0 rgba(255,255,255,.03);
      }

      #formulario button{
        justify-self: end;
        padding: 12px 18px;
        border: 0;
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: .2px;
        color: white;
        cursor: pointer;
        background: linear-gradient(135deg, var(--accent), var(--accent-2));
        box-shadow: var(--shadow-sm);
        transition: transform .06s ease, filter .2s ease, box-shadow .2s ease;
      }

      #formulario button:hover{
        filter: brightness(1.06) saturate(1.05);
        box-shadow: 0 8px 22px rgba(0,0,0,.25);
      }

      #formulario button:active{
        transform: translateY(1px) scale(.995);
      }

      /* Small screens: stack nicely */
      @media (max-width: 720px){
        #formulario{
          grid-template-columns: 1fr;
        }
        #formulario button{
          justify-self: stretch;
        }
      }

      /* ===== Table styling ===== */
      table{
        border-collapse: separate;
        border-spacing: 0;
        width: min(980px, 100%);
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        overflow: hidden;
        box-shadow: var(--shadow);
      }

      table tr:first-child th{
        position: sticky; /* stays at top if page scrolls */
        top: 0;
        background:
          linear-gradient(0deg, rgba(255,255,255,.02), rgba(255,255,255,.02)),
          var(--panel-2);
        color: var(--text);
        text-align: left;
        font-weight: 800;
        letter-spacing: .3px;
      }

      th, td{
        padding: 14px 16px;
        border-bottom: 1px solid color-mix(in oklab, currentColor 12%, transparent);
      }

      tr:last-child td{
        border-bottom: none;
      }

      /* Zebra stripes & hover */
      table tr:nth-child(odd){
        background: color-mix(in oklab, var(--panel) 92%, black 8%);
      }

      table tr:nth-child(even){
        background: var(--panel);
      }

      table tr:hover td{
        background: color-mix(in oklab, var(--panel) 85%, var(--accent) 5%);
      }

      /* Subtle row entrance animation when table re-renders */
      @keyframes rowIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
      }
      table tr{
        animation: rowIn .25s ease both;
      }

      /* Make columns breathe on small screens */
      @media (max-width: 560px){
        th, td{ padding: 12px 14px; }
      }

      /* ===== Focus visibility for a11y ===== */
      :focus-visible{
        outline: 0;
        box-shadow: 0 0 0 6px var(--ring) !important;
        border-color: var(--accent) !important;
        border-radius: 10px;
      }

      /* ===== Nice scrollbars (where supported) ===== */
      :root{
        scrollbar-color: color-mix(in oklab, var(--panel) 65%, var(--accent) 35%) transparent;
        scrollbar-width: thin;
      }
      ::-webkit-scrollbar{ height: 10px; width: 10px; }
      ::-webkit-scrollbar-track{ background: transparent; }
      ::-webkit-scrollbar-thumb{
        background: color-mix(in oklab, var(--panel) 60%, var(--accent) 40%);
        border-radius: 999px;
        border: 2px solid transparent;
        background-clip: padding-box;
      }

    </style>
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button> 
    </div>
    <table>
    </table>
    <div id="formularioeliminar">
      <input type="text" id="ideliminar" placeholder="Introduce el ID para eliminar">
      <button id="procesaeliminar">Eliminar</button>
    </div>
    <div id="formularioactualizar">
      <input type="text" id="idactualizar" placeholder="Introduce el ID a actualizar">
      <input type="text" id="nuevonombre" placeholder="Introduce el nuevo nombre">
      <input type="text" id="nuevoemail" placeholder="Introduce el nuevo email">
      <button id="procesaactualizar">Actualizar</button>
    </div>
    <script>
        // Creo un array vacio
        let clientes = [];
        /////////////////// CREATE ///////////////////////////
        
        // Selecciono el boton
        let boton = document.querySelector("button")
        // Si pulso el boton, se añade el registro
        boton.onclick = function(){
          anadeRegistro()
        }
        // Si pulso una tecla
        document.onkeypress = function(event){
          // Y la tecla es la tecla enter
          if(event.key == "Enter"){
            anadeRegistro() // En ese caso se añade el registro
          }
        }
        function anadeRegistro(){
          // Atrapo el nombre
          let nombre = document.querySelector("#nombre").value
          // Atrapo el email
          let email = document.querySelector("#email").value
          // Añado el cliente actual al array
          clientes.push({"nombre":nombre,"email":email})
          // Lo saco por consola
          console.log(clientes)
          // Borramos los campos
          document.querySelector("#nombre").value = ""
          document.querySelector("#email").value = ""
          // Re-renderizo la tabla
          pueblaTabla()
        }
        /////////////////// READ ///////////////////////////
        
        function pueblaTabla(){
          // Primero creo la cabecera de la tabla
          let cadena = "<tr><th>Nombre</th><th>Email</th></tr>";
          // Repaso uno a uno los clientes
          clientes.forEach(function(cliente){
             cadena += "<tr><td>"+cliente.nombre+"</td><td>"+cliente.email+"</td></tr>"
          })
          document.querySelector("table").innerHTML = cadena
          // Persisto los datos en localStorage
          localStorage.setItem("clientes",JSON.stringify(clientes));
        }
        
        /////////////////// DELETE ///////////////////////////
        
        // Primero cojo el botón
        var botoneliminar = document.querySelector("#procesaeliminar");
        // Cuando pulso el botón
        botoneliminar.onclick = function(){
          // Tomo el id a eliminar
          let ideliminar = document.querySelector("#ideliminar").value
          // Y ahora elimino el elemento del array
          clientes.splice(ideliminar,1); /////////////// IMPORTANTE
          // Y ahora re-renderizo la tabla
          pueblaTabla();
        }
        
        /////////////////// UPDATE ///////////////////////////
        
        // Primero cojo el botón
        var botonactualizar = document.querySelector("#procesaactualizar");
        // Cuando pulso el botón
        botonactualizar.onclick = function(){
          // Primer cojo el id a actualizar
          let idactualizar = document.querySelector("#idactualizar").value
          // Ahora atrapo el dato del nuevo nombre
          let nuevonombre = document.querySelector("#nuevonombre").value
          // A continuación atrapo el dato del nuevo email
          let nuevoemail = document.querySelector("#nuevoemail").value
          // Edito el array y construyo un objeto
          clientes[idactualizar] = {"nombre":nuevonombre,"email":nuevoemail}
          // Y ahora re-renderizo la tabla
          pueblaTabla();
        }
    </script>
  </body>
</html>
```

### recuperar memoria
<small>Creado: 2025-09-28 22:28</small>

`410-recuperar memoria.html`

```html
<!doctype html>
<html>
  <head>
    <title></title>
    <meta charset="utf-8">
    <style>
      /* ===== Design tokens ===== */
      :root{
        --bg: hsl(220 15% 10%);
        --panel: hsl(220 20% 14%);
        --panel-2: hsl(220 18% 16%);
        --text: hsl(210 20% 98%);
        --muted: hsl(220 10% 70%);
        --accent: hsl(199 90% 56%);
        --accent-2: hsl(213 90% 62%);
        --success: hsl(142 60% 45%);
        --danger: hsl(2 85% 62%);
        --ring: hsla(199, 90%, 56%, .35);
        --radius: 14px;
        --shadow: 0 10px 30px rgba(0,0,0,.35);
        --shadow-sm: 0 4px 16px rgba(0,0,0,.25);
        --border: 1px solid hsl(220 18% 22%);
        --font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue",
                 Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji";
      }

      /* Light mode tweak if user prefers */
      @media (prefers-color-scheme: light){
        :root{
          --bg: hsl(210 20% 98%);
          --panel: hsl(0 0% 100%);
          --panel-2: hsl(0 0% 100%);
          --text: hsl(222 18% 16%);
          --muted: hsl(222 10% 40%);
          --accent: hsl(210 100% 52%);
          --accent-2: hsl(221 89% 63%);
          --ring: hsla(210, 100%, 52%, .32);
          --border: 1px solid hsl(220 15% 88%);
          --shadow: 0 10px 30px rgba(2,12,27,.08);
          --shadow-sm: 0 4px 16px rgba(2,12,27,.06);
        }
      }

      /* ===== Global ===== */
      *,
      *::before,
      *::after{ box-sizing: border-box; }

      html, body{
        height: 100%;
      }

      body{
        margin: 0;
        font-family: var(--font);
        color: var(--text);
        background:
          radial-gradient(1200px 600px at 10% -10%, rgba(255,255,255,.06), transparent 50%),
          radial-gradient(1200px 600px at 110% 10%, rgba(255,255,255,.05), transparent 50%),
          var(--bg);
        display: grid;
        align-content: start;
        gap: 24px;
        padding: 40px 20px 80px;
      }

      /* Center content and set widths without altering HTML */
      #formulario, table{
        width: min(980px, 100%);
        margin-inline: auto;
      }

      /* ===== Form card ===== */
      #formulario{
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        box-shadow: var(--shadow);
        padding: 20px;
        display: grid;
        grid-template-columns: 1fr 1fr auto;
        gap: 14px;
        align-items: start;
      }

      #formulario input[type="text"]{
        appearance: none;
        width: 100%;
        padding: 12px 14px;
        border-radius: 10px;
        border: var(--border);
        background: var(--panel-2);
        color: var(--text);
        outline: none;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
        transition: border-color .2s ease, box-shadow .2s ease, transform .04s ease;
      }

      #formulario input::placeholder{
        color: var(--muted);
      }

      #formulario input:focus{
        border-color: var(--accent);
        box-shadow: 0 0 0 6px var(--ring), inset 0 1px 0 rgba(255,255,255,.03);
      }

      #formulario button{
        justify-self: end;
        padding: 12px 18px;
        border: 0;
        border-radius: 12px;
        font-weight: 700;
        letter-spacing: .2px;
        color: white;
        cursor: pointer;
        background: linear-gradient(135deg, var(--accent), var(--accent-2));
        box-shadow: var(--shadow-sm);
        transition: transform .06s ease, filter .2s ease, box-shadow .2s ease;
      }

      #formulario button:hover{
        filter: brightness(1.06) saturate(1.05);
        box-shadow: 0 8px 22px rgba(0,0,0,.25);
      }

      #formulario button:active{
        transform: translateY(1px) scale(.995);
      }

      /* Small screens: stack nicely */
      @media (max-width: 720px){
        #formulario{
          grid-template-columns: 1fr;
        }
        #formulario button{
          justify-self: stretch;
        }
      }

      /* ===== Table styling ===== */
      table{
        border-collapse: separate;
        border-spacing: 0;
        width: min(980px, 100%);
        background: var(--panel);
        border: var(--border);
        border-radius: var(--radius);
        overflow: hidden;
        box-shadow: var(--shadow);
      }

      table tr:first-child th{
        position: sticky; /* stays at top if page scrolls */
        top: 0;
        background:
          linear-gradient(0deg, rgba(255,255,255,.02), rgba(255,255,255,.02)),
          var(--panel-2);
        color: var(--text);
        text-align: left;
        font-weight: 800;
        letter-spacing: .3px;
      }

      th, td{
        padding: 14px 16px;
        border-bottom: 1px solid color-mix(in oklab, currentColor 12%, transparent);
      }

      tr:last-child td{
        border-bottom: none;
      }

      /* Zebra stripes & hover */
      table tr:nth-child(odd){
        background: color-mix(in oklab, var(--panel) 92%, black 8%);
      }

      table tr:nth-child(even){
        background: var(--panel);
      }

      table tr:hover td{
        background: color-mix(in oklab, var(--panel) 85%, var(--accent) 5%);
      }

      /* Subtle row entrance animation when table re-renders */
      @keyframes rowIn {
        from { opacity: 0; transform: translateY(6px); }
        to   { opacity: 1; transform: translateY(0); }
      }
      table tr{
        animation: rowIn .25s ease both;
      }

      /* Make columns breathe on small screens */
      @media (max-width: 560px){
        th, td{ padding: 12px 14px; }
      }

      /* ===== Focus visibility for a11y ===== */
      :focus-visible{
        outline: 0;
        box-shadow: 0 0 0 6px var(--ring) !important;
        border-color: var(--accent) !important;
        border-radius: 10px;
      }

      /* ===== Nice scrollbars (where supported) ===== */
      :root{
        scrollbar-color: color-mix(in oklab, var(--panel) 65%, var(--accent) 35%) transparent;
        scrollbar-width: thin;
      }
      ::-webkit-scrollbar{ height: 10px; width: 10px; }
      ::-webkit-scrollbar-track{ background: transparent; }
      ::-webkit-scrollbar-thumb{
        background: color-mix(in oklab, var(--panel) 60%, var(--accent) 40%);
        border-radius: 999px;
        border: 2px solid transparent;
        background-clip: padding-box;
      }

    </style>
  </head>
  <body>
    <div id="formulario">
      <input type="text" id="nombre" placeholder="Introduce el nombre">
      <input type="text" id="email" placeholder="Introduce el email">
      <button>Añadir</button> 
    </div>
    <table>
    </table>
    <div id="formularioeliminar">
      <input type="text" id="ideliminar" placeholder="Introduce el ID para eliminar">
      <button id="procesaeliminar">Eliminar</button>
    </div>
    <div id="formularioactualizar">
      <input type="text" id="idactualizar" placeholder="Introduce el ID a actualizar">
      <input type="text" id="nuevonombre" placeholder="Introduce el nuevo nombre">
      <input type="text" id="nuevoemail" placeholder="Introduce el nuevo email">
      <button id="procesaactualizar">Actualizar</button>
    </div>
    <script>
        // Creo un array vacio
        let clientes = [];
        // Y ahora si acaso hay algo en el localStorage, lo cargo
        clientes = JSON.parse(localStorage.getItem("clientes"))
        // Y redibujo la tabla
        pueblaTabla() 
        
        
        /////////////////// CREATE ///////////////////////////
        
        // Selecciono el boton
        let boton = document.querySelector("button")
        // Si pulso el boton, se añade el registro
        boton.onclick = function(){
          anadeRegistro()
        }
        // Si pulso una tecla
        document.onkeypress = function(event){
          // Y la tecla es la tecla enter
          if(event.key == "Enter"){
            anadeRegistro() // En ese caso se añade el registro
          }
        }
        function anadeRegistro(){
          // Atrapo el nombre
          let nombre = document.querySelector("#nombre").value
          // Atrapo el email
          let email = document.querySelector("#email").value
          // Añado el cliente actual al array
          clientes.push({"nombre":nombre,"email":email})
          // Lo saco por consola
          console.log(clientes)
          // Borramos los campos
          document.querySelector("#nombre").value = ""
          document.querySelector("#email").value = ""
          // Re-renderizo la tabla
          pueblaTabla()
        }
        /////////////////// READ ///////////////////////////
        
        function pueblaTabla(){
          // Primero creo la cabecera de la tabla
          let cadena = "<tr><th>Nombre</th><th>Email</th></tr>";
          // Repaso uno a uno los clientes
          clientes.forEach(function(cliente){
             cadena += "<tr><td>"+cliente.nombre+"</td><td>"+cliente.email+"</td></tr>"
          })
          document.querySelector("table").innerHTML = cadena
          // Persisto los datos en localStorage
          localStorage.setItem("clientes",JSON.stringify(clientes));
        }
        
        /////////////////// DELETE ///////////////////////////
        
        // Primero cojo el botón
        var botoneliminar = document.querySelector("#procesaeliminar");
        // Cuando pulso el botón
        botoneliminar.onclick = function(){
          // Tomo el id a eliminar
          let ideliminar = document.querySelector("#ideliminar").value
          // Y ahora elimino el elemento del array
          clientes.splice(ideliminar,1); /////////////// IMPORTANTE
          // Y ahora re-renderizo la tabla
          pueblaTabla();
        }
        
        /////////////////// UPDATE ///////////////////////////
        
        // Primero cojo el botón
        var botonactualizar = document.querySelector("#procesaactualizar");
        // Cuando pulso el botón
        botonactualizar.onclick = function(){
          // Primer cojo el id a actualizar
          let idactualizar = document.querySelector("#idactualizar").value
          // Ahora atrapo el dato del nuevo nombre
          let nuevonombre = document.querySelector("#nuevonombre").value
          // A continuación atrapo el dato del nuevo email
          let nuevoemail = document.querySelector("#nuevoemail").value
          // Edito el array y construyo un objeto
          clientes[idactualizar] = {"nombre":nuevonombre,"email":nuevoemail}
          // Y ahora re-renderizo la tabla
          pueblaTabla();
        }
    </script>
  </body>
</html>
```

### clientes
<small>Creado: 2025-09-28 22:28</small>

`clientes.json`

```json
[
  {
    "nombre":"Juan",
    "apellidos":"Lopez",
    "email":"info@juan.com"
  },
  {
    "nombre":"Jorge",
    "apellidos":"Lopez",
    "email":"info@jorge.com"
  },
  {
    "nombre":"Jose Luis",
    "apellidos":"Martinez",
    "email":"info@joseluis.com"
  },
  {
    "nombre":"Julia",
    "apellidos":"Garcia",
    "email":"info@julia.com"
  }
]
```


<a id="ejercicio-final-de-unidad"></a>
## Ejercicio final de unidad

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/000-Prerrequisitos/101-Ejercicio%20final%20de%20unidad)



<a id="identificacion-de-sistemas-erp-crm"></a>
# Identificación de sistemas ERP-CRM

<a id="concepto-de-erp"></a>
## Concepto de ERP

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/001-Concepto%20de%20ERP)


<a id="revision-de-los-erp-actuales"></a>
## Revisión de los ERP actuales

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/002-Revisi%C3%B3n%20de%20los%20ERP%20actuales)


<a id="concepto-de-crm"></a>
## Concepto de CRM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/003-Concepto%20de%20CRM)


<a id="revision-de-los-crm-actuales"></a>
## Revisión de los CRM actuales

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/004-Revisi%C3%B3n%20de%20los%20CRM%20actuales)


<a id="tipos-de-licencias-de-los-erp-crm"></a>
## Tipos de licencias de los ERP-CRM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/005-Tipos%20de%20licencias%20de%20los%20ERP-CRM)


<a id="sistemas-gestores-de-bases-de-datos-compatibles-con-el-software"></a>
## Sistemas gestores de bases de datos compatibles con el software

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/006-Sistemas%20gestores%20de%20bases%20de%20datos%20compatibles%20con%20el%20software)

### app
<small>Creado: 2025-10-28 15:48</small>

`app.py`

```python
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
```

### database
<small>Creado: 2025-10-28 15:48</small>

`database.py`

```python
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
```


<a id="instalacion-y-configuracion-del-sistema-informatico"></a>
## Instalación y configuración del sistema informático

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/007-Instalaci%C3%B3n%20y%20configuraci%C3%B3n%20del%20sistema%20inform%C3%A1tico)

### servidor
<small>Creado: 2025-10-01 15:13</small>

`001-servidor.py`

```python
print("Hola mundo")
```

### ahora quiero instalar flask
<small>Creado: 2025-10-01 15:26</small>

`002-ahora quiero instalar flask.py`

```python
# Windows:
# pip install flask

# Linux:
# sudo apt install pip - o esta
# sudo apt install pip3 - o esta


# pip3 install flask --break-system-packages
```

### miniservidor
<small>Creado: 2025-10-01 15:29</small>

`003-miniservidor.py`

```python
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return "Esto es HTML desde Flask"
  
if __name__ == "__main__":
  aplicacion.run(debug=True)
```

### mas html
<small>Creado: 2025-10-01 15:41</small>

`004-mas html.py`

```python
from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route("/")
def raiz():
  return '''
    <!doctype html>
    <html>
      <head>
        <title>Flask</title>
      </head>
      <body>
        <h1>Hola desde Python</h1>
      </body>
    </html>
  '''
  
  
if __name__ == "__main__":
  aplicacion.run(debug=True)
```

### salidas
<small>Creado: 2025-10-01 15:52</small>

`005-salidas.py`

```python
print("Esto es una salida en Python")
```

### entradas
<small>Creado: 2025-10-01 15:55</small>

`006-entradas.py`

```python
input("Introduce tu edad")
```

### podemos entrar cadena
<small>Creado: 2025-10-01 15:56</small>

`007-podemos entrar cadena.py`

```python
input("Introduce tu nombre")
```

### variables
<small>Creado: 2025-10-01 15:57</small>

`008-variables.py`

```python
edad = 47
```

### tipos de datos
<small>Creado: 2025-10-01 15:59</small>

`009-tipos de datos.py`

```python
edad = 47               # Tipo de dato entero
altura = 1.78           # Tipo de datos decimal
nombre = "Jose Vicente" # Tipo de dato cadena
profesor = True         # Tipo de dato booleano
```

### comentarios
<small>Creado: 2025-10-01 16:01</small>

`010-comentarios.py`

```python
# esto es un comentario de una única linea

'''
  Esto es un docstring
  Se puede considerar cadena multilinea
  O se puede considerar comentario multilinea
'''

"""
  También se puede usar con comillas dobles
"""
```

### cambio de tipo de dato
<small>Creado: 2025-10-01 16:04</small>

`011-cambio de tipo de dato.py`

```python
edad = 47
print(edad)
print(type(edad))

edad = str(edad)

print(edad)
print(type(edad))

edad = int(edad)

print(edad)
print(type(edad))

edad = float(edad)

print(edad)
print(type(edad))
```

### operadores aritmeticos
<small>Creado: 2025-10-01 16:06</small>

`012-operadores aritmeticos.py`

```python
print(4+3)
print(4-3)
print(4*3)
print(4/3)
print(4%3)
```

### operadores de comparacion
<small>Creado: 2025-10-01 16:31</small>

`013-operadores de comparacion.py`

```python
print(4 < 3)
print(4 <= 3)
print(4 > 3)
print(4 >= 3)
print(4 == 3)
print(4 != 3)
```

### operadores booleanos
<small>Creado: 2025-10-01 16:33</small>

`014-operadores booleanos.py`

```python
print(4 == 4 and 3 == 3 and 2 == 2)
print(4 == 4 and 3 == 3 and 2 == 1)

print(4 == 4 or 3 == 3 or 2 == 2)
print(4 == 4 or 3 == 3 or 2 == 1)
print(4 == 4 or 3 == 2 or 2 == 1)
print(4 == 3 or 3 == 2 or 2 == 1)
```

### if
<small>Creado: 2025-10-01 16:35</small>

`015-if.py`

```python
edad = 47

if edad < 30:
  print("Eres un joven")
```

### else
<small>Creado: 2025-10-01 16:37</small>

`016-else.py`

```python
edad = 47

if edad < 30:
  print("Eres un joven")
else:
  print("Ya no eres un joven")
```

### elif
<small>Creado: 2025-10-01 16:38</small>

`017-elif.py`

```python
edad = 47

if edad < 10:
  print("Eres un niño")
elif edad >= 10 and edad < 20:
  print("Eres un adolescente")
elif edad >= 20 and edad < 30:
  print("Eres un joven")
else:
  print("Ya no eres un joven")
```

### for
<small>Creado: 2025-10-01 16:41</small>

`018-for.py`

```python
for dia in range(1,31,1):
  print("Hoy es el dia",dia,"del mes")
```

### while
<small>Creado: 2025-10-01 16:42</small>

`019-while.py`

```python
dia = 1
while dia < 31:
  print("Hoy es el dia",dia,"del mes")
  dia += 1
```


<a id="verificacion-de-la-instalacion-y-configuracion"></a>
## Verificación de la instalación y configuración

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/008-Verificaci%C3%B3n%20de%20la%20instalaci%C3%B3n%20y%20configuraci%C3%B3n)

### app
<small>Creado: 2025-10-08 16:05</small>

`app.py`

```python
# Primero importamos la librería de Flask para montar un servidor
from flask import Flask, request, redirect
# Importamos la base de datos y la librería de sistema
import sqlite3, os

# Creamos una instancia del servidor en Python
app = Flask(__name__)
# Y creamos el apunte a una base de datos
DB = "clientes.db"

# Función de manejo de la base de datos
def db(q, args=()):
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    cur = con.execute(q, args); con.commit()
    r = cur.fetchall(); cur.close(); con.close(); return r

# Si no existe la base de datos, creala - ATENCION aqui modificáis el modelo de datos
if not os.path.exists(DB):
    db("""CREATE TABLE clientes(
        id INTEGER PRIMARY KEY,
        nombre TEXT, apellidos TEXT, email TEXT, telefono TEXT,
        dni TEXT, fecha_nacimiento TEXT)""")

# Raiz, acepta recogida de información
@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
      # Si el método es post, inserta nuevo cliente
      # Esta es la estructura que RECIBE los datos
        f = request.form
        db("INSERT INTO clientes(nombre,apellidos,email,telefono,dni,fecha_nacimiento) VALUES(?,?,?,?,?,?)",
           (f["nombre"], f["apellidos"], f["email"], f.get("telefono",""), f["dni"], f.get("fecha_nacimiento","")))
        return redirect("/")
    # en cualquier otro caso, solicita
    filas = db("SELECT * FROM clientes ORDER BY apellidos,nombre")
    # HTML mínimo inline
    
    return """
<!doctype html><meta charset=utf-8>
<title>Clientes</title>
<h3>Nuevo cliente</h3>
<form method=post>
<!-- Este es el formulario que ENVIA los datos -->
  <input name=nombre placeholder=Nombre required>
  <input name=apellidos placeholder=Apellidos required>
  <input name=email type=email placeholder=Email required>
  <input name=telefono placeholder=Teléfono>
  <input name=dni placeholder=DNI required>
  <input name=fecha_nacimiento type=date>
  <button>Guardar</button>
</form>
<h3>Listado</h3>
<table border=1 cellspacing=0 cellpadding=4>
  <tr><th>Nombre</th><th>Apellidos</th><th>Email</th><th>Teléfono</th><th>DNI</th><th>Fecha nac.</th></tr>
  %s
</table>""" % "\n".join(
        f"<tr><td>{r['nombre']}</td><td>{r['apellidos']}</td><td>{r['email']}</td>"
        f"<td>{r['telefono']}</td><td>{r['dni']}</td><td>{r['fecha_nacimiento'] or ''}</td></tr>"
        for r in filas)

if __name__ == "__main__":
    app.run(debug=True)
```

### app2
<small>Creado: 2025-10-08 16:15</small>

`app2.py`

```python
from flask import Flask, request, redirect, render_template
import sqlite3, os

app = Flask(__name__)
DB = "clientes.db"

def db(q, args=()):
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    cur = con.execute(q, args); con.commit()
    r = cur.fetchall(); cur.close(); con.close(); return r

# Crear la tabla si no existe
if not os.path.exists(DB):
    db("""CREATE TABLE clientes(
        id INTEGER PRIMARY KEY,
        nombre TEXT, apellidos TEXT, email TEXT, telefono TEXT,
        dni TEXT, fecha_nacimiento TEXT)""")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        f = request.form
        db("INSERT INTO clientes(nombre,apellidos,email,telefono,dni,fecha_nacimiento) VALUES(?,?,?,?,?,?)",
           (f["nombre"], f["apellidos"], f["email"], f.get("telefono",""), f["dni"], f.get("fecha_nacimiento","")))
        return redirect("/")
    filas = db("SELECT * FROM clientes ORDER BY apellidos,nombre")
    return render_template("index.html", filas=filas)

if __name__ == "__main__":
    app.run(debug=True)
```

### app3
<small>Creado: 2025-10-08 16:24</small>

`app3.py`

```python
from flask import Flask, request, redirect, render_template, url_for, abort
import sqlite3, os

app = Flask(__name__)
DB = "clientes.db"

def db(q, args=(), one=False):
    con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
    cur = con.execute(q, args); con.commit()
    rows = cur.fetchall(); cur.close(); con.close()
    return (rows[0] if rows else None) if one else rows

# Crear tabla si no existe
if not os.path.exists(DB):
    db("""CREATE TABLE clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT, apellidos TEXT, email TEXT, telefono TEXT,
        dni TEXT, fecha_nacimiento TEXT)""")

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == "POST":
        f = request.form
        db("INSERT INTO clientes(nombre,apellidos,email,telefono,dni,fecha_nacimiento) VALUES(?,?,?,?,?,?)",
           (f["nombre"], f["apellidos"], f["email"], f.get("telefono",""), f["dni"], f.get("fecha_nacimiento","")))
        return redirect(url_for("index"))
    filas = db("SELECT * FROM clientes ORDER BY apellidos,nombre")
    return render_template("index.html", filas=filas)

@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id):
    if request.method == "POST":
        f = request.form
        db("""UPDATE clientes SET nombre=?, apellidos=?, email=?, telefono=?, dni=?, fecha_nacimiento=?
              WHERE id=?""",
           (f["nombre"], f["apellidos"], f["email"], f.get("telefono",""),
            f["dni"], f.get("fecha_nacimiento",""), id))
        return redirect(url_for("index"))
    r = db("SELECT * FROM clientes WHERE id=?", (id,), one=True)
    if not r: abort(404)
    return render_template("edit.html", r=r)

@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    db("DELETE FROM clientes WHERE id=?", (id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
```


<a id="documentacion-de-las-operaciones-realizadas"></a>
## Documentación de las operaciones realizadas

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/009-Documentaci%C3%B3n%20de%20las%20operaciones%20realizadas)

### insertar datos
<small>Creado: 2025-10-14 19:36</small>

`002-insertar datos.sql`

```sql
-- clientes
INSERT INTO clientes VALUES(
  NULL,
  'Jose Vicente',
  'Carratalá',
  'info@jocarsa.com'
);

INSERT INTO clientes VALUES(
  NULL,
  'Juan',
  'García Lopez',
  'juan@jocarsa.com'
);

-- productos

INSERT INTO productos VALUES(
  NULL,
  'manzana',
  'Manzana de color rojo',
  '0.3'
);

INSERT INTO productos VALUES(
  NULL,
  'Naranja',
  'Naranja valenciana',
  '0.2'
);
```

### conectar con base de datos
<small>Creado: 2025-10-14 19:41</small>

`003-conectar con base de datos.py`

```python
import sqlite3

con = sqlite3.connect('empresa.db')
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())
con.close()
```

### pinto ccon flask
<small>Creado: 2025-10-14 19:48</small>

`004-pinto ccon flask.py`

```python
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  return "Hola mundo desde Flask"

con = sqlite3.connect('empresa.db')
cur = con.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())
con.close()

if __name__ == "__main__":
    app.run(debug=True)
```

### creo menu de navegacion
<small>Creado: 2025-10-14 20:02</small>

`005-creo menu de navegacion.py`

```python
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  html = '''
    <style>
      body{display:flex;margin:0px;padding:0px;}
      nav{flex:1;background:indigo;color:white;padding:20px;}
      main{flex:5;}
      nav a{text-decoration:none;color:inherit;display:block;background:white;color:indigo;padding:10px;margin:20px;}
    </style>
    <body>
      <nav>'''
  con = sqlite3.connect('empresa.db')
  cur = con.cursor()
  cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
  lineas = cur.fetchall()
  for linea in lineas:
    html += '<a href="">'+linea[0]+'</a>'
  con.close()    
  html += '''</nav>
      <main></main>
    </body>
  '''
  return html

if __name__ == "__main__":
    app.run(debug=True)
```

### tabla
<small>Creado: 2025-10-14 20:21</small>

`006-tabla.py`

```python
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  html = '''
    <style>
      body{display:flex;margin:0px;padding:0px;}
      nav{flex:1;background:indigo;color:white;padding:20px;}
      main{flex:5;padding:20px;}
      nav a{text-decoration:none;color:inherit;display:block;background:white;color:indigo;padding:10px;margin:20px;}
      table{width:100%;}
      table tr{border-bottom:1px solid indigo;}
    </style>
    <body>
      <nav>'''
  con = sqlite3.connect('empresa.db')
  cur = con.cursor()
  cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
  lineas = cur.fetchall()
  for linea in lineas:
    html += '<a href="">'+linea[0]+'</a>'
    
  html += '''</nav>
      <main>
      <table>
      <tr>

      '''
  cur.execute("PRAGMA table_info(clientes);")    
  lineas = cur.fetchall()
  for linea in lineas:
    html += '<th>'+str(linea[1])+'</th>'
  html += '''
  </tr>
  </table>
  </main>
    </body>
  '''
  con.close()  
  return html

if __name__ == "__main__":
    app.run(debug=True)
```

### datos de la tabla
<small>Creado: 2025-10-14 20:24</small>

`007-datos de la tabla.py`

```python
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  html = '''
    <style>
      body{display:flex;margin:0px;padding:0px;}
      nav{flex:1;background:indigo;color:white;padding:20px;}
      main{flex:5;padding:20px;}
      nav a{text-decoration:none;color:inherit;display:block;background:white;color:indigo;padding:10px;margin:20px;}
      table{width:100%;}
      table tr{border-bottom:1px solid indigo;}
    </style>
    <body>
      <nav>'''
  con = sqlite3.connect('empresa.db')
  cur = con.cursor()
  cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
  lineas = cur.fetchall()
  for linea in lineas:
    html += '<a href="">'+linea[0]+'</a>'
    
  html += '''</nav>
      <main>
      <table>
      <tr>

      '''
  cur.execute("PRAGMA table_info(clientes);")    
  lineas = cur.fetchall()
  for linea in lineas:
    html += '<th>'+str(linea[1])+'</th>'
  html += '''
  </tr>'''
  cur.execute("SELECT * FROM clientes;")
  lineas = cur.fetchall()  
  for linea in lineas:
    html += '<tr>'
    for campo in linea:
      html += '<td>' + str(campo) + '</td>'
    html += '</tr>'
  html += '''
  </table>
  </main>
    </body>
  '''
  con.close()  
  return html

if __name__ == "__main__":
    app.run(debug=True)
```

### evitar sqlite sequence
<small>Creado: 2025-10-14 20:38</small>

`008-evitar sqlite sequence.py`

```python
from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
  html = '''
    <style>
      body{display:flex;margin:0px;padding:0px;}
      nav{flex:1;background:indigo;color:white;padding:20px;}
      main{flex:5;padding:20px;}
      nav a{text-decoration:none;color:inherit;display:block;background:white;color:indigo;padding:10px;margin:20px;}
      table{width:100%;}
      table tr{border-bottom:1px solid indigo;}
    </style>
    <body>
      <nav>'''
  con = sqlite3.connect('empresa.db')
  cur = con.cursor()
  cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
  lineas = cur.fetchall()
  for linea in lineas:
    if linea[0] != "sqlite_sequence":
      html += '<a href="">'+linea[0]+'</a>'
    
  html += '''</nav>
      <main>
      <table>
      <tr>

      '''
  cur.execute("PRAGMA table_info(clientes);")    
  lineas = cur.fetchall()
  for linea in lineas:
    html += '<th>'+str(linea[1])+'</th>'
  html += '''
  </tr>'''
  cur.execute("SELECT * FROM clientes;")
  lineas = cur.fetchall()  
  for linea in lineas:
    html += '<tr>'
    for campo in linea:
      html += '<td>' + str(campo) + '</td>'
    html += '</tr>'
  html += '''
  </table>
  </main>
    </body>
  '''
  con.close()  
  return html

if __name__ == "__main__":
    app.run(debug=True)
```

### dinamico
<small>Creado: 2025-10-14 20:42</small>

`009-dinamico.py`

```python
from flask import Flask, request, jsonify
import sqlite3
import requests
import html

app = Flask(__name__)

DB_PATH = "empresa.db"

def get_conn():
    # Row factory opcional si luego quisieras dicts
    con = sqlite3.connect(DB_PATH)
    return con

# ---------- API interna ----------
@app.route("/api/tables")
def api_tables():
    con = get_conn()
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tablas = [r[0] for r in cur.fetchall() if r[0] != "sqlite_sequence"]
    con.close()
    return jsonify(tablas)

@app.route("/api/table/<table_name>")
def api_table(table_name):
    # Pequeña validación: que la tabla exista
    con = get_conn()
    cur = con.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    valid_tables = {r[0] for r in cur.fetchall() if r[0] != "sqlite_sequence"}
    if table_name not in valid_tables:
        con.close()
        return jsonify({"error": "Tabla no encontrada"}), 404

    # Columnas
    cur.execute(f"PRAGMA table_info({table_name});")
    columns = [row[1] for row in cur.fetchall()]

    # Filas
    cur.execute(f"SELECT * FROM {table_name};")
    rows = cur.fetchall()
    con.close()
    return jsonify({"columns": columns, "rows": rows})

# ---------- UI ----------
@app.route("/")
def index():
    # Base URL para que requests llame a nuestra propia app
    base = request.host_url.rstrip("/")
    # 1) Obtener lista de tablas mediante requests
    r = requests.get(f"{base}/api/tables")
    r.raise_for_status()
    tablas = r.json()

    # Tabla seleccionada (por querystring) o la primera disponible
    seleccion = request.args.get("table") or (tablas[0] if tablas else None)

    # 2) Si hay selección, pedir sus datos al endpoint interno
    cols, rows = [], []
    if seleccion:
        r2 = requests.get(f"{base}/api/table/{seleccion}")
        if r2.status_code == 200:
            data = r2.json()
            cols = data.get("columns", [])
            rows = data.get("rows", [])
        else:
            seleccion = None  # Evita render de tabla si hay error

    # Render HTML
    html_out = '''
    <style>
      body{display:flex;margin:0;padding:0;font-family:system-ui,Arial,sans-serif;}
      nav{flex:1;background:indigo;color:white;padding:20px;min-height:100vh;box-sizing:border-box;}
      main{flex:5;padding:20px;box-sizing:border-box;}
      nav a{text-decoration:none;color:indigo;display:block;background:white;padding:10px;margin:10px 0;border-radius:8px;}
      nav a.active{background:#fff2; color:white; border:1px solid #fff8;}
      table{width:100%;border-collapse:collapse;}
      th,td{padding:8px 10px;text-align:left;}
      tr{border-bottom:1px solid indigo;}
      h1{margin-top:0}
      .muted{opacity:.7}
    </style>
    <body>
      <nav>
        <h3>Tablas</h3>
    '''
    # Enlaces de tablas
    for t in tablas:
        active = "active" if t == seleccion else ""
        html_out += f'<a class="{active}" href="/?table={html.escape(t)}">{html.escape(t)}</a>'

    html_out += '</nav><main>'

    if not tablas:
        html_out += "<h1>Sin tablas</h1><p class='muted'>La base de datos no contiene tablas.</p>"
    elif not seleccion:
        html_out += "<h1>Selecciona una tabla</h1>"
    else:
        html_out += f"<h1>{html.escape(seleccion)}</h1>"
        if cols:
            html_out += "<table><tr>"
            for c in cols:
                html_out += f"<th>{html.escape(str(c))}</th>"
            html_out += "</tr>"
            for row in rows:
                html_out += "<tr>"
                for cell in row:
                    html_out += f"<td>{html.escape(str(cell))}</td>"
                html_out += "</tr>"
            html_out += "</table>"
        else:
            html_out += "<p class='muted'>No hay columnas o datos para esta tabla.</p>"

    html_out += "</main></body>"
    return html_out

if __name__ == "__main__":
    # threaded=True para permitir que 'requests' llame a nuestra propia app sin bloquear
    app.run(debug=True, threaded=True)
```

### example
<small>Creado: 2025-10-14 19:41</small>

`example.db`

```

```


<a id="simulacro-de-examen"></a>
## Simulacro de examen

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/010-Simulacro%20de%20examen)


<a id="simulacro-de-examen-2"></a>
## Simulacro de examen 2

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/011-Simulacro%20de%20examen%202)


<a id="ejercicio-final-de-unidad-1"></a>
## Ejercicio final de unidad

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/101-Ejercicio%20final%20de%20unidad)


<a id="examen-final"></a>
## Examen final

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/001-Identificaci%C3%B3n%20de%20sistemas%20ERP-CRM/104-Examen%20final)

### crear tablas
<small>Creado: 2025-11-12 16:51</small>

`001-crear tablas.sql`

```sql
CREATE DATABASE portafolioceac;

USE portafolioceac;


CREATE TABLE Piezas(
  Identificador INT auto_increment PRIMARY KEY,
  titulo VARCHAR(255),
  descripcion VARCHAR(255),
  imagen VARCHAR(255),
  url VARCHAR(255),
  id_categoria INT
);

CREATE TABLE Categorias(
  Identificador INT auto_increment PRIMARY KEY,
  titulo VARCHAR(255),
  descripcion VARCHAR(255)
);
```

### insertar
<small>Creado: 2025-11-12 16:51</small>

`002-insertar.sql`

```sql
INSERT INTO Categorias VALUES(
  NULL,
  'General',
  'Esta es la categoria general'
);

INSERT INTO Piezas VALUES(
  NULL,
  'Primera pieza',
  'Esta es la descripcion de la primera pieza',
  'josevicente.jpg',
  'https://jocarsa.com',
  1
);
```

### fk
<small>Creado: 2025-11-12 16:51</small>

`003-fk.sql`

```sql
ALTER TABLE Piezas
ADD CONSTRAINT fk_piezas_categorias
FOREIGN KEY (id_categoria) REFERENCES Categorias(identificador)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

### selecciones
<small>Creado: 2025-11-12 16:51</small>

`004-selecciones.sql`

```sql
SELECT * FROM Categorias;

SELECT * FROM Piezas;
```

### left join
<small>Creado: 2025-11-12 16:51</small>

`005-left join.sql`

```sql
SELECT 
* 
FROM Piezas
LEFT JOIN Categorias
ON Piezas.id_categoria = Categorias.Identificador;
```

### ahora creo la vista
<small>Creado: 2025-11-12 16:51</small>

`006-ahora creo la vista.sql`

```sql
CREATE VIEW piezas_y_categorias AS 
SELECT 
Categorias.titulo AS categoriatitulo,
Categorias.descripcion AS categoriadescripcion,
Piezas.titulo AS piezatitulo,
Piezas.descripcion AS piezadescripcion,
imagen,
url
FROM Piezas
LEFT JOIN Categorias
ON Piezas.id_categoria = Categorias.Identificador;

SELECT * FROM piezas_y_categorias;
```

### usuario
<small>Creado: 2025-11-12 16:51</small>

`007-usuario.sql`

```sql
-- crea usuario nuevo con contraseña
-- creamos el nombre de usuario que queramos
CREATE USER 
'portafolioceac'@'localhost' 
IDENTIFIED  BY 'portafolioceac';

-- permite acceso a ese usuario
GRANT USAGE ON *.* TO 'portafolioceac'@'localhost';
--[tuservidor] == localhost
-- La contraseña puede requerir Mayus, minus, numeros, caracteres, min len

-- quitale todos los limites que tenga
ALTER USER 'portafolioceac'@'localhost' 
REQUIRE NONE 
WITH MAX_QUERIES_PER_HOUR 0 
MAX_CONNECTIONS_PER_HOUR 0 
MAX_UPDATES_PER_HOUR 0 
MAX_USER_CONNECTIONS 0;

-- dale acceso a la base de datos empresadam
GRANT ALL PRIVILEGES ON portafolioceac.* 
TO 'portafolioceac'@'localhost';

-- recarga la tabla de privilegios
FLUSH PRIVILEGES;
```



<a id="instalacion-y-configuracion-de-sistemas-erp-crm"></a>
# Instalación y configuración de sistemas ERP-CRM

<a id="tipos-de-instalacion"></a>
## Tipos de instalación.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/002-Instalaci%C3%B3n%20y%20configuraci%C3%B3n%20de%20sistemas%20ERP-CRM/001-Tipos%20de%20instalaci%C3%B3n.)


<a id="modulos-de-un-sistema-erp-crm"></a>
## Módulos de un sistema ERP-CRM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/002-Instalaci%C3%B3n%20y%20configuraci%C3%B3n%20de%20sistemas%20ERP-CRM/002-M%C3%B3dulos%20de%20un%20sistema%20ERP-CRM%20)

### Pantallas
<small>Creado: 2025-09-17 16:06</small>

`001-Pantallas`

```
Pantalla de selección de módulos

Pantalla de contactos (rejilla)

Información del contacto (formulario)

Calendario
-Mensual
-Semanal
-Anual
-Dietario

ERP Crea un nuevo lenguaje y ese lenguaje tiene que ser consistente

Ventana flotante - Ventana modal

Ventana kanban
```

### rejilla de clientes
<small>Creado: 2025-09-17 16:14</small>

`002-rejilla de clientes.html`

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      body,html{padding:0px;margin:0px;font-family:sans-serif;}
      header{
        background:#71639e;
        color:white;
        display:flex;
        justify-content: space-between;
        padding:10px;
      }
      ul{
        display:flex;
        list-style-type:none;
        padding:0px;
        margin:0px;
      }
      li{
        padding:5px;
       }
    </style>
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li>Contactos</li>
          <li>Contactos</li>
          <li>Configuración</li>
        </ul>
      </nav>
      <nav>
        <ul>
          <li>M</li>
          <li>R</li>
          <li>My Company</li>
          <li>A</li>
        </ul>
      </nav>
    </header>
  </body>
</html>
```

### barra de busqueda
<small>Creado: 2025-09-17 16:18</small>

`003-barra de busqueda.html`

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      body,html{padding:0px;margin:0px;font-family:sans-serif;}
      header{
        background:#71639e;
        color:white;
        display:flex;
        justify-content: space-between;
        padding:10px;
      }
      ul{
        display:flex;
        list-style-type:none;
        padding:0px;
        margin:0px;
      }
      li{
        padding:5px;
       }
       #barra{
        display:flex;
        justify-content: space-between;
        padding:10px;
        border-bottom:1px solid grey;
       }
       #barra button{
        background:#71639e;
        color:white;
        border-radius:4px;
        border:none;
        padding:15px;
       }
    </style>
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li>Contactos</li>
          <li>Contactos</li>
          <li>Configuración</li>
        </ul>
      </nav>
      <nav>
        <ul>
          <li>M</li>
          <li>R</li>
          <li>My Company</li>
          <li>A</li>
        </ul>
      </nav>
    </header>
    <div id="barra">
      <div id="nuevo">
        <button>Nuevo</button>
      </div>
      <input type="search" placeholder="Buscar...">
      <div id="herramientas">
        A
      </div>
    </div>
  </body>
</html>
```

### rejilla
<small>Creado: 2025-09-17 16:21</small>

`004-rejilla.html`

```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      body,html{padding:0px;margin:0px;font-family:sans-serif;}
      header{
        background:#71639e;
        color:white;
        display:flex;
        justify-content: space-between;
        padding:10px;
      }
      ul{
        display:flex;
        list-style-type:none;
        padding:0px;
        margin:0px;
      }
      li{
        padding:5px;
       }
       #barra{
        display:flex;
        justify-content: space-between;
        padding:10px;
        border-bottom:1px solid grey;
       }
       #barra button{
        background:#71639e;
        color:white;
        border-radius:4px;
        border:none;
        padding:15px;
       }
       #rejilla{
        display:grid;
        grid-template-columns: auto auto auto;
        background:rgb(240,240,240);
       }
       #rejilla article{
        width:400px;
        height:100px;
        margin:10px;
        background:white;
        padding:10px;
       }
    </style>
  </head>
  <body>
    <header>
      <nav>
        <ul>
          <li>Contactos</li>
          <li>Contactos</li>
          <li>Configuración</li>
        </ul>
      </nav>
      <nav>
        <ul>
          <li>M</li>
          <li>R</li>
          <li>My Company</li>
          <li>A</li>
        </ul>
      </nav>
    </header>
    <div id="barra">
      <div id="nuevo">
        <button>Nuevo</button>
      </div>
      <input type="search" placeholder="Buscar...">
      <div id="herramientas">
        A
      </div>
    </div>
    <div id="rejilla">
      <article>
        Persona
      </article>
      <article>
        Persona
      </article>
      <article>
        Persona
      </article>
      <article>
        Persona
      </article>
      <article>
        Persona
      </article>
      <article>
        Persona
      </article>
      <article>
        Persona
      </article>
    </div>
  </body>
</html>
```


<a id="procesos-de-instalacion-del-sistema-erp-crm"></a>
## Procesos de instalación del sistema ERP-CRM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/002-Instalaci%C3%B3n%20y%20configuraci%C3%B3n%20de%20sistemas%20ERP-CRM/003-Procesos%20de%20instalaci%C3%B3n%20del%20sistema%20ERP-CRM)


<a id="parametros-de-configuracion-del-sistema-erp-crm"></a>
## Parámetros de configuración del sistema ERP-CRM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/002-Instalaci%C3%B3n%20y%20configuraci%C3%B3n%20de%20sistemas%20ERP-CRM/004-Par%C3%A1metros%20de%20configuraci%C3%B3n%20del%20sistema%20ERP-CRM%20)


<a id="actualizacion-del-sistema-erp-crm-y-aplicacion-de-actualizaciones"></a>
## Actualización del sistema ERP-CRM y aplicación de actualizaciones

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/002-Instalaci%C3%B3n%20y%20configuraci%C3%B3n%20de%20sistemas%20ERP-CRM/005-Actualizaci%C3%B3n%20del%20sistema%20ERP-CRM%20y%20aplicaci%C3%B3n%20de%20actualizaciones)


<a id="servicios-de-acceso-al-sistema-erp-crm"></a>
## Servicios de acceso al sistema ERP-CRM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/002-Instalaci%C3%B3n%20y%20configuraci%C3%B3n%20de%20sistemas%20ERP-CRM/006-Servicios%20de%20acceso%20al%20sistema%20ERP-CRM%20)


<a id="entornos-de-desarrollo-pruebas-y-explotacion"></a>
## Entornos de desarrollo, pruebas y explotación

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/002-Instalaci%C3%B3n%20y%20configuraci%C3%B3n%20de%20sistemas%20ERP-CRM/007-Entornos%20de%20desarrollo%2C%20pruebas%20y%20explotaci%C3%B3n)



<a id="organizacion-y-consulta-de-la-informacion"></a>
# Organización y consulta de la información

<a id="definicion-de-campos"></a>
## Definición de campos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/001-Definici%C3%B3n%20de%20campos)


<a id="consultas-de-acceso-a-datos"></a>
## Consultas de acceso a datos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/002-Consultas%20de%20acceso%20a%20datos)


<a id="interfaces-de-entrada-de-datos-y-de-procesos"></a>
## Interfaces de entrada de datos y de procesos.

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/003-Interfaces%20de%20entrada%20de%20datos%20y%20de%20procesos.%20)


<a id="informes-y-listados-de-la-aplicacion"></a>
## Informes y listados de la aplicación

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/004-Informes%20y%20listados%20de%20la%20aplicaci%C3%B3n)


<a id="gestion-de-pedidos"></a>
## Gestión de pedidos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/005-Gesti%C3%B3n%20de%20pedidos)


<a id="graficos"></a>
## Gráficos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/006-Gr%C3%A1ficos)


<a id="herramientas-de-monitorizacion-y-de-evaluacion-del-rendimiento"></a>
## Herramientas de monitorización y de evaluación del rendimiento

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/007-Herramientas%20de%20monitorizaci%C3%B3n%20y%20de%20evaluaci%C3%B3n%20del%20rendimiento)


<a id="incidencias-identificacion-y-resolucion"></a>
## Incidencias identificación y resolución

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/008-Incidencias%20identificaci%C3%B3n%20y%20resoluci%C3%B3n)


<a id="procesos-de-extraccion-de-datos-en-sistemas-de-erp-crm-y-almacenes-de-datos"></a>
## Procesos de extracción de datos en sistemas de ERP-CRM y almacenes de datos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/009-Procesos%20de%20extracci%C3%B3n%20de%20datos%20en%20sistemas%20de%20ERP-CRM%20y%20almacenes%20de%20datos)


<a id="inteligencia-de-negocio-business-intelligence"></a>
## Inteligencia de negocio (Business Intelligence)

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/003-Organizaci%C3%B3n%20y%20consulta%20de%20la%20informaci%C3%B3n/010-Inteligencia%20de%20negocio%20%28Business%20Intelligence%29)



<a id="implantacion-de-sistemas-erp-crm-en-una-empresa"></a>
# Implantación de sistemas ERP-CRM en una empresa

<a id="tipos-de-empresa-necesidades-de-la-empresa"></a>
## Tipos de empresa. Necesidades de la empresa

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/004-Implantaci%C3%B3n%20de%20sistemas%20ERP-CRM%20en%20una%20empresa/001-Tipos%20de%20empresa.%20Necesidades%20de%20la%20empresa)


<a id="seleccion-de-los-modulos-del-sistema-erp-crm"></a>
## Selección de los módulos del sistema ERP-CRM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/004-Implantaci%C3%B3n%20de%20sistemas%20ERP-CRM%20en%20una%20empresa/002-Selecci%C3%B3n%20de%20los%20m%C3%B3dulos%20del%20sistema%20ERP-CRM)


<a id="tablas-y-vistas-que-es-preciso-adaptar"></a>
## Tablas y vistas que es preciso adaptar

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/004-Implantaci%C3%B3n%20de%20sistemas%20ERP-CRM%20en%20una%20empresa/003-Tablas%20y%20vistas%20que%20es%20preciso%20adaptar)


<a id="consultas-necesarias-para-obtener-informacion"></a>
## Consultas necesarias para obtener información

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/004-Implantaci%C3%B3n%20de%20sistemas%20ERP-CRM%20en%20una%20empresa/004-Consultas%20necesarias%20para%20obtener%20informaci%C3%B3n)


<a id="creacion-de-formularios-personalizados"></a>
## Creación de formularios personalizados

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/004-Implantaci%C3%B3n%20de%20sistemas%20ERP-CRM%20en%20una%20empresa/005-Creaci%C3%B3n%20de%20formularios%20personalizados)


<a id="creacion-de-informes-personalizados"></a>
## Creación de informes personalizados

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/004-Implantaci%C3%B3n%20de%20sistemas%20ERP-CRM%20en%20una%20empresa/006-Creaci%C3%B3n%20de%20informes%20personalizados)


<a id="paneles-de-control-dashboards"></a>
## Paneles de control (Dashboards)

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/004-Implantaci%C3%B3n%20de%20sistemas%20ERP-CRM%20en%20una%20empresa/007-Paneles%20de%20control%20%28Dashboards%29)


<a id="integracion-con-otros-sistemas-de-gestion"></a>
## Integración con otros sistemas de gestión

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/004-Implantaci%C3%B3n%20de%20sistemas%20ERP-CRM%20en%20una%20empresa/008-Integraci%C3%B3n%20con%20otros%20sistemas%20de%20gesti%C3%B3n)



<a id="desarrollo-de-componentes"></a>
# Desarrollo de componentes

<a id="arquitectura-del-erp-crm"></a>
## Arquitectura del ERP-CRM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/005-Desarrollo%20de%20componentes/001-Arquitectura%20del%20ERP-CRM)


<a id="lenguaje-proporcionado"></a>
## Lenguaje proporcionado

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/005-Desarrollo%20de%20componentes/002-Lenguaje%20proporcionado)


<a id="entornos-de-desarrollo-y-herramientas-del-sistema-erp-y-crm"></a>
## Entornos de desarrollo y herramientas del sistema ERP y CRM

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/005-Desarrollo%20de%20componentes/003-Entornos%20de%20desarrollo%20y%20herramientas%20del%20sistema%20ERP%20y%20CRM)


<a id="insercion-modificacion-y-eliminacion-de-datos-en-los-objetos"></a>
## Inserción, modificación y eliminación de datos en los objetos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/005-Desarrollo%20de%20componentes/004-Inserci%C3%B3n%2C%20modificaci%C3%B3n%20y%20eliminaci%C3%B3n%20de%20datos%20en%20los%20objetos)


<a id="operaciones-de-consulta-herramientas"></a>
## Operaciones de consulta. Herramientas

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/005-Desarrollo%20de%20componentes/005-Operaciones%20de%20consulta.%20Herramientas)


<a id="formularios-e-informes"></a>
## Formularios e informes

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/005-Desarrollo%20de%20componentes/006-Formularios%20e%20informes)


<a id="procesamiento-de-datos-y-obtencion-de-la-informacion"></a>
## Procesamiento de datos y obtención de la información

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/005-Desarrollo%20de%20componentes/007-Procesamiento%20de%20datos%20y%20obtenci%C3%B3n%20de%20la%20informaci%C3%B3n)


<a id="llamadas-a-funciones-librerias-de-funciones-apis"></a>
## Llamadas a funciones, librerías de funciones (APIs)

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/005-Desarrollo%20de%20componentes/008-Llamadas%20a%20funciones%2C%20librer%C3%ADas%20de%20funciones%20%28APIs%29)


<a id="depuracion-y-tratamiento-de-errores"></a>
## Depuración y tratamiento de errores

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/005-Desarrollo%20de%20componentes/009-Depuraci%C3%B3n%20y%20tratamiento%20de%20errores)



<a id="proyecto-trimestral"></a>
# Proyecto trimestral

<a id="inicio"></a>
## Inicio

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/006-Proyecto%20trimestral/001-Inicio)

### index
<small>Creado: 2026-02-17 16:06</small>

`index.php`

```
<!doctype html>
<html lang="es">
	<head>
  	<title>SSGG</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="base/estilo/comun.css">
  </head>
  <body>
    <?php
      include "interfaces/login.php";
    ?>
  </body>
</html>
```


<a id="login"></a>
## Login

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/006-Proyecto%20trimestral/002-Login)

### index
<small>Creado: 2026-02-17 19:26</small>

`index.php`

```
<!doctype html>
<html lang="es">
	<head>
  	<title>SSGG</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="base/estilo/comun.css">
  </head>
  <body>
    <?php
      include "interfaces/login.php";
    ?>
  </body>
</html>
```


<a id="selector-de-modulos"></a>
## selector de modulos

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/006-Proyecto%20trimestral/003-selector%20de%20modulos)

### index
<small>Creado: 2026-02-17 19:59</small>

`index.php`

```
<?php session_start(); ?>
<!doctype html>
<html lang="es">
	<head>
  	<title>SSGG</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="base/estilo/comun.css">
  </head>
  <body>
    <?php
    	if(!isset($_SESSION['usuario'])){					// Si no existe la variable de sesion usuario
      	include "interfaces/login.php";					// Carga el login para que pueda iniciar sesion
      }else{
      	include "interfaces/selectormodulos.php";	// Cargame el escritorio
      }
    ?>
  </body>
</html>
```


<a id="seguridad-basica"></a>
## seguridad basica

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/006-Proyecto%20trimestral/004-seguridad%20basica)

### index
<small>Creado: 2026-02-17 20:21</small>

`index.php`

```
<?php
	session_start(); 
  include "util/saneador.php";
?>
<!doctype html>
<html lang="es">
	<head>
  	<title>SSGG</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="base/estilo/comun.css">
  </head>
  <body>
    <?php
    	if(!isset($_SESSION['usuario'])){					// Si no existe la variable de sesion usuario
      	include "interfaces/login.php";					// Carga el login para que pueda iniciar sesion
      }else{
      	include "interfaces/selectormodulos.php";	// Cargame el escritorio
      }
    ?>
  </body>
</html>
```



<a id="repaso-php"></a>
# Repaso PHP

<a id="repaso-inicial"></a>
## Repaso inicial

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/007-Repaso%20PHP/001-Repaso%20inicial)

### salidas
<small>Creado: 2026-02-17 19:31</small>

`001-salidas.php`

```
<?php
	echo "Esto es una salida en PHP";
?>
```

### embebido
<small>Creado: 2026-02-17 19:32</small>

`002-embebido.php`

```
Esto es HTML

<?php
	echo "Esto es una salida en PHP";
?>

Y esto vuelve a ser HTML
```

### multiembebido
<small>Creado: 2026-02-17 19:32</small>

`003-multiembebido.php`

```
Esto es HTML

<?php
	echo "Esto es una salida en PHP";
?>

Y esto vuelve a ser HTML

<?php
	echo "Y esto vuelve a ser PHP";
?>
```

### PHP hace calculos
<small>Creado: 2026-02-17 19:33</small>

`004-PHP hace calculos.php`

```
4+3
<br>
<?php

	echo 4+3

?>
```

### variables
<small>Creado: 2026-02-17 19:34</small>

`005-variables.php`

```
<?php
	$edad = 47;
  echo $edad;
?>
```

### operadores aritmeticos
<small>Creado: 2026-02-17 19:35</small>

`006-operadores aritmeticos.php`

```
<?php
	echo 4+3;
  echo "<br>";
  echo 4-3;
  echo "<br>";
  echo 4*3;
  echo "<br>";
  echo 4/3;
  echo "<br>";
?>
```

### estructuras condicionales
<small>Creado: 2026-02-17 19:36</small>

`007-estructuras condicionales.php`

```
<?php
	
  $edad = 47;
  
  if($edad < 10){
  	echo "Eres un niño";
  }
  
?>
```

### clausula else
<small>Creado: 2026-02-17 19:37</small>

`008-clausula else.php`

```
<?php
	
  $edad = 47;
  
  if($edad < 10){
  	echo "Eres un niño";
  }else{
  	echo "No eres un niño";
  }
  
?>
```

### else if
<small>Creado: 2026-02-17 19:37</small>

`009-else if.php`

```
<?php
	
  $edad = 47;
  
  if($edad < 10){
  	echo "Eres un niño";
  }else if(edad >= 10 && edad < 20){
  	echo "Eres un adolescente";
  }else if(edad >= 20 && edad < 30){
  	echo "Eres un joven";
  }else{
  	echo "Ya no eres un joven";
  }
  
?>
```

### switch
<small>Creado: 2026-02-17 19:39</small>

`010-switch.php`

```
<?php
	
  $diadelasemana = "martes";
  
  switch($diadelasemana){
  	case "lunes":
     	echo "Hoy es el peor día de la semana";
      break;
     case "martes":
     	echo "Hoy es el segundo peor día de la semana";
      break;
     case "miercoles":
     	echo "Ya estamos a mitad de semana";
      break;
     case "jueves":
     	echo "Ya es casi viernes";
      break;
     case "viernes":
     	echo "Por fin es viernes";
      break;
     case "sabado":
     	echo "Hoy es el mejor día de la semana";
      break;
     case "domingo":
     	echo "Parece mentira que mañana ya sea lunes";
      break;
  }
  
?>
```



<a id="git"></a>
# .git

<a id="branches"></a>
## branches

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/.git/branches)


<a id="hooks"></a>
## hooks

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/.git/hooks)


<a id="info"></a>
## info

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/.git/info)


<a id="logs"></a>
## logs

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/.git/logs)


<a id="objects"></a>
## objects

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/.git/objects)


<a id="refs"></a>
## refs

[📁 Ver carpeta en GitHub](https://github.com/jocarsa/sistemasdegestionempresarial/tree/main/.git/refs)
