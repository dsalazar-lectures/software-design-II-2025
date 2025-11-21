# Chain of Responsibility Pattern (CoR, Chain of Command)

Estudiante: Alexander Wang Wu

Carnet: C28559

## Tabla de Contenidos
1. [Definición](#Definición)
2. [Objetivo](#Objetivo)
2. [Problema y Solución](#Problema-y-Solución)
3. [Componentes de la Estructura](#Componentes-de-la-Estructura)
4. [Mantenibilidad y Escalabilidad](#Mantenibilidad-y-Escalabilidad)
5. [Ventajas y Desventajas](#Ventajas-y-Desventajas)
6. [Casos de usos](#Casos-de-usos)
7. [Relaciones con otros patrones](#Relaciones-con-otros-patrones)
8. [Compilar el código](#Compilar-el-código)
9. [Referencias](#Referencias)

---

## Definición:

El patrón Chain of Responsibility (Cadena de Responsabilidad) es un patrón de comportamiento que permite que un objeto transmita una solicitud a través de una cadena de manejadores (handlers). Cada manejador de la cadena decide si procesa la solicitud o la transmite al siguiente manejador.

---

## Objetivo

El objetivo del patrón CoR es fomentar un acoplamiento flexible entre el emisor y el receptor, proporcionando libertad en el manejo de la solicitud.

---

## Problema y Solución
### Problema
Problema común que resuelve el CoR es cuando tiene una petición que podría ser atendida por varios componentes/reglas que termina con:

* muchos ifs/switch gigantes anidados.
* baja extensibilidad en donde para agregar una nueva regla/paso debe editar mucho el código de las verificaciones.
* difícil de probar el código porque la lógica está mezclada por muchos elementos.
* orden frágil porque cambiando la prioridad de reglas tiene su dificultad y puede romper muy fácil el código.

### Solución
Encadenar manejadores "handlers" en donde:

* Intenta manejar la petición.
* Si no se puede, la delega al siguiente.
* Opcionalmente puede cortar la cadena cuando ya se resolvió la petición.
---

## Componentes de la estructura de CoR
1. La clase **Manejadora** declara la interfaz común a todos los manejadores concretos.
2. La clase **Manejadora Base** es opcional y es donde puede colocar el código cómun para todas las clases manejadoras.
3. Los **Manejadores Concretos** contienen el código para procesar las solicitudes. Cada manejador debe decidir si procesarla cuando reciba una solicitud o pasarla a lo largo de la cadena.
4. El **Cliente** puede componer cadenas una sola vez o componerlas dinámicamente, dependiendo de la aplicación
---

## Mantenibilidad y Escalabilidad
1. Acomplamento flexible: El remitente de una solicitud no necesita saber qué objeto específico la gestionará.
2. Cadena dinámica: Mientras el programa se ejecuta, modificar la cadena es sencillo, esto le otorga a su código una gran flexibilidad.
3. Orden Secuenciall: Las solicitudes se mueven por la cadena una a una, tieniendo la oportunidad de procesar la solicitud cada gestor en un orden específico.
4. Mecanismo de respaldo: Esto significa que existe una forma predeterminada de gestionar las solicitudes que no encajan en ningún otro lugar.
---

## Ventajas y Desventajas
### Ventajas
* Reducción de if/switch enormes.
* Principio abierto/cerrado (Open/Closed)
* Principio de Responsabilidad Única (SRP)
* Controlar el orden de control de solicitudes.

### Desventajas
* Rendimiento: puede generar sobrecarga y latencia al tener una cadena larga
* Complejidad: puede ser difícil de depurar
* Algunas solicitudes pueden acabar sin ser gestionadas
---

## Casos de usos
1. Utiliza el patrón CoR cuando tu programa deba procesar distintos tipos de solicitudes de varias maneras, pero los tipos exactos de solicitudes y sus secuencias no se conozcan de antemano.
2. Utiliza el patrón cuando sea fundamental ejecutar varios manejadores en un orden específico.
3. Utiliza el patrón CoR cuando el grupo de manejadores y su orden deban cambiar durante el tiempo de ejecución.
---

## Relaciones con otros patrones
1. **Command**, **Mediator** y **Observer** abordan distintas formas de conectar emisores y receptores de solicitudes.
2. Se utliza a menudo junto **Composite**.
3. Los manejadores de CoR se pueden implementar como **Command**.
4. CoR y **Decorator** tienen estructuras de clase muy similares.
---

## Compilar el código
Primero debe cargar el repositorio.

```bash
/software-design-II-2025/
```

Luego, ejecuta el siguiente comando para compilar el código y se muestra los resultados esperados.


```bash
python lab3/chain_of_responsibility/src/main.py
```

---

## Referencias
GeeksforGeeks. (2025). Chain of responsibility design pattern: System design. https://www.geeksforgeeks.org/system-design/chain-responsibility-design-pattern/#how-to-implement-chain-of-responsibiility-design-pattern

Refactoring.Guru. (s. f.). Cadena de responsabilidad (Chain of Responsibility). https://refactoring.guru/es/design-patterns/chain-of-responsibility