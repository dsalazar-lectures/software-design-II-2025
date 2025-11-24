# Patrón de Diseño Adapter

### 1. Definición del patrón y a qué tipo pertenece

El patrón **Adapter** (Adaptador) es un patrón de diseño **estructural**.

**Definición:**
El propósito del Adaptador es **permitir la colaboración entre objetos con interfaces incompatibles**. Actúa como un puente (bridge) o un envoltorio (*wrapper*) especial que convierte la interfaz de un objeto para que otro objeto pueda comprenderla.

En esencia, el adaptador envuelve uno de los objetos (el *Adaptee*) para ocultar la complejidad de la conversión que ocurre "tras bambalinas". De esta manera, un objeto existente puede invocar con seguridad los métodos del adaptador, el cual, a su vez, pasa la solicitud al segundo objeto en el formato y orden que este espera.

Los componentes clave del patrón Adaptador son:
*   **Interfaz con el Cliente (Target Interface):** El protocolo que las clases cliente esperan utilizar.
*   **Servicio (Adaptee):** La clase útil existente (a menudo de un tercero o heredada) que tiene una interfaz incompatible y el cliente no puede usar directamente.
*   **Adaptador (Adapter):** La clase que implementa la Interfaz con el Cliente y envuelve el objeto de Servicio, traduciendo las llamadas del cliente al formato que el objeto de servicio espera.
*   **Cliente (Client):** La lógica de negocio que utiliza la Interfaz con el Cliente.

Existen diferentes implementaciones, como el **Adaptador de Objetos** (basado en composición, que es más flexible y ampliamente utilizado) y el **Adaptador de Clase** (basado en herencia, requiere herencia múltiple como en C++). También puede existir un **adaptador de dos direcciones** que convierte las llamadas en ambos sentidos.

### 2. ¿Cuál es el problema común que resuelve?

El patrón Adapter resuelve el problema de la **incompatibilidad de interfaces**. Permite utilizar una clase existente (un *Adaptee*) cuya interfaz no es compatible con el resto del código.

**Escenario de ejemplo:**
Un problema común es la necesidad de **integrar código heredado o bibliotecas de terceros**. Por ejemplo, si está construyendo una aplicación de monitoreo que descarga datos en formato **XML**, pero necesita integrar una biblioteca de análisis inteligente de terceros que solo funciona con datos en formato **JSON**.

La solución no es modificar la biblioteca (lo cual podría ser imposible si no se tiene acceso al código fuente o si podría descomponer código existente). En su lugar, se crea una clase intermedia (*el Adaptador*) que actúa como **traductora** entre el código cliente (que espera XML) y la clase de servicio (que espera JSON). El adaptador convierte los datos XML entrantes a una estructura JSON y luego pasa la llamada al objeto de análisis envuelto.

Otros ejemplos en el mundo real incluyen *drivers* de dispositivos, conectores de bases de datos, conversores de lenguaje, o software que utiliza adaptadores para convertir datos entre formatos (como CSV, JSON, XML).

### 3. ¿Cómo mejora el mantenimiento o escalabilidad del sistema?

El patrón Adapter impacta positivamente el mantenimiento y la escalabilidad de varias maneras, principalmente a través del **desacoplamiento** y la **reutilización de código**:

1.  **Promueve la Reutilización de Código:** Permite reutilizar código o bibliotecas existentes (como clases de terceros o heredadas) sin tener que reescribirlas para que coincidan con la nueva interfaz.
2.  **Facilita la Modificación (Principio Abierto/Cerrado):** Se pueden introducir nuevos tipos de adaptadores en el programa sin descomponer el código cliente existente. Esto se logra siempre y cuando el código cliente trabaje con la clase adaptadora a través de la interfaz con el cliente. Si la interfaz de la clase de servicio subyacente cambia o se sustituye, se puede crear un nuevo adaptador sin modificar el código cliente.
3.  **Mejora el Mantenimiento (Responsabilidad Única):** El patrón ayuda a **separar la interfaz o el código de conversión de datos** de la lógica de negocio primaria del programa. Esto simplifica el mantenimiento al centralizar los cambios de compatibilidad en el adaptador.
4.  **Desacoplamiento:** Desacopla el sistema de implementaciones concretas del servicio (el *Adaptee*), lo que facilita las modificaciones y el intercambio de componentes. Simplifica la integración de nuevos componentes, manteniendo el sistema flexible.

### 4. Otras ventajas y desventajas de su uso

#### Ventajas:

*   **Reutilización de código:** Promueve la reutilización de código ya existente sin necesidad de modificarlo.
*   **Aislamiento de lógica:** Mantiene a las clases enfocadas en su lógica central al aislar las tareas de adaptación.
*   **Flexibilidad de interfaces:** Soporta múltiples interfaces a través de adaptadores intercambiables.
*   **Principio de Open/Close:** Permite extender la funcionalidad (introducir nuevos adaptadores) sin modificar el código cliente.
*   **Principio de Responsabilidad Única:** Separa la conversión de datos y la gestión de interfaces de la lógica de negocio.

#### Desventajas:

*   **Aumento de la complejidad:** La complejidad general del código aumenta, ya que se deben introducir nuevas interfaces y clases para manejar la adaptación.
*   **Indirección y sobrecarga de rendimiento:** Introduce una ligera sobrecarga de rendimiento (*performance overhead*) debido a la capa de indirección extra que implica la llamada al adaptador antes de llegar al servicio.
*   **Mantenimiento de múltiples adaptadores:** Si hay muchas interfaces incompatibles, la gestión y el mantenimiento de múltiples adaptadores puede aumentar el esfuerzo.
*   **Riesgo de uso excesivo:** Existe el riesgo de usar el patrón para cambios menores donde sería más sencillo modificar la clase de servicio original para que coincida con el resto del código.
