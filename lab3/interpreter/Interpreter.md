# Patrones de Diseño: Interpreter

## Tabla de Contenidos
1. [¿Qué es?](#qué-es)
2. [Casos de uso](#casos-de-uso)
3. [Estructura](#estructura)
4. [Diagrama](#diagrama)
5. [Ventajas y desventajas](#ventajas-y-desventajas)
6. [Ejemplo práctico](#ejemplo-práctico)
7. [Referencias](#referencias)


## ¿Qué es?

El patrón de diseño Interpreter es un patrón de comportamiento orientado al procesamiento de lenguajes. El mecanismo que provee
consiste en seccionar la gramática del lenguaje en sus partes más pequeñas. Se busca separar la expresión completa en varios componentes para su procesamiento individual. De esta manera convertimos un problema grande en sub-problemas más sencillos.

El patrón provee una estructura jerárquica para sus clases semejante a las estructuras de datos árboles. Por lo cual, en su implementación se introduce la recursividad junto al polimorfismo y la herencia.

## Casos de uso 

- Procesamiento de expresiones matemáticas o lógicas.
- Procesamiento de lenguajes sencillos en compiladores.
- Interpretación de comandos (SQL).

## Estructura

Los componentes clave del patrón Interpreter son las expresiones.
Hay de dos tipos: **terminales** y **no terminales**. Entendemos expresiones terminales como los componentes claves del lenguaje en
el contexto de nuestro programa. Y las expresiones no terminales
son una composición de expresiones terminales.

Las clases que define el manual de Interpreter son:

**AbstractExpression:** Define la interfaz que seguirán las expresiones concretas. Firmando con su método fundamental `interpret()`.

**TerminalExpression:** Implementación concreta de `AbstractExpression`. Debe definir la implementación del método
`interpret()`.

**NonTerminalExpression:** Implementación concreta de `AbstractExpression`. Provee una definición más compleja para la 
evaluación de las expresiones terminales que la componen.

**Context:** Clase de acceso global al Interpreter con la información necesaria para evaluar las expresiones.

**Client/Interpreter:** Clase encargada de dirigir el proceso de
interpretación. Entre sus funciones se encuentran el armar el árbol de expresiones.

> Dependiendo del ejemplo se puede encontrar al cliente y al interpretador en clases separadas.

### Diagrama
![Estructura Interpreter]()

## Ventajas y Desventajas

### Ventajas

- **Flexibilidad:** Provee un ambiente en el que es sencillo agregar operaciones sin modificar la lógica existente.
- **Separación de asuntos:** Su solución separa claramente la lógica de interpretación del resto de la implementación del programa; así, proporcionando un código más legible y fácil de mantener.

### Desventajas

- **Complejo:** Es considerado un patrón de diseño complejo de comprender.
- **Utilidad limitada:** Se le considera inadecuado cuando la gramática del problema resulta demasiado compleja.
- **Bajo rendimiento:** Para sistemas en los que es crucial el rendimiento, no es recomendable utilizar Interpreter.

## Consideraciones

A la hora de implementar Interpreter es necesario definir la gramática que seguirá el lenguaje a procesar. Posteriormente, se debe evaluar si lo que se requiere para evaluar dicho lenguaje es
compatible con el patrón. 

## Ejemplo Práctico

Para ejemplificar el uso de Interpreter se realizó un micro ejemplo de un sistema de procesamiento de búsquedas de usuario en un recetario.

Se definió la siguiente gramática:

`consulta` := `tipo_receta`?`incluir/excluir`?`ingredientes`

`tipo_receta` := "dinner" | "breakfast" | "dessert" ...
    
`incluir` := "with" `ingrediente` ("and" `ingrediente`)
    
`filter_exclusion` := "without" `ingrediente` ("and" `ingrediente`)

> **Ejemplo:** "Desserts with strawberries and whipped cream"

Para la implementación definimos los ingredientes y el tipo de
receta como las expresiones no terminales. Siendo el segmento
*"with `ingrediente` and `ingrediente`"* lo que se entendie por
expresiones no terminales.

La clase `SearchContext`además de encapsular la expresión completa
provee la lista de ingredientes completa que el programa soporta. 
El sentido de este atributo es que el programa sepa si ese token es un ingrediente válido.

## Compilación

La demo está programada en el lenguaje de programación `Rust`. Para probar su funcionamiento siga los siguientes pasos:

--> [Instalación de rust](https://rust-lang.org/tools/install) ó

Comando para la terminal en Linux/WSL:

> curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

Asegurese de estar en la carpeta correcta
>  cd interpreter

Compile y corra el proyecto
> cargo run

Ejemplo de output esperado:
> Request: recipes with chicken and rice
> 
> Result: Text("type: Some(\"General\"), include: [\"rice\", \"chicken\"], exclude: []")

## Referencias:

[1] [Oscar Blancarte - Interpreter](https://reactiveprogramming.io/blog/es/patrones-de-diseno/interpreter)

[2] [GeeksforGeeks - Interpreter Design Pattern](https://www.geeksforgeeks.org/system-design/interpreter-design-pattern)

[3] [GeeksforGeeks - Interpreter Method Design Pattern in Python](https://www.geeksforgeeks.org/system-design/interpreter-method-design-pattern-in-python)

[4] [Mentores Tech - Patrón Interpreter](https://www.mentorestech.com/resource-design-pattern-interpreter.php#:~:text=Casos%20de%20Uso%20*%20Interpretar%20expresiones%20matemáticas,y%20evaluación%20de%20reglas%20en%20sistemas%20expertos.)
