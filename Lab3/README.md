## James Araya Rodríguez -B70528
## Laboratorio 3
----

# Patrón de Diseño: Singleton

## Definición
**Singleton** es un **patrón de diseño creacional** que garantiza que una clase tenga **una única instancia** durante la ejecución del programa y que proporcione un **punto de acceso global** a dicha instancia.

Este patrón se utiliza cuando es necesario que todos los módulos o componentes del sistema trabajen con el **mismo objeto compartido**, evitando la creación innecesaria de múltiples instancias.

---

## Función y propósito
El propósito principal del patrón **Singleton** es **evitar la duplicación de recursos** dentro del sistema, asegurando que solo exista una instancia que sea reutilizada por todos los módulos.  
Esto contribuye a:
- **Reducir el consumo de memoria y procesamiento**, al no crear múltiples objetos idénticos.
- **Mantener la consistencia de la información**, ya que todos los componentes acceden al mismo estado.
- **Centralizar el control de configuraciones o recursos globales**, evitando errores por variables duplicadas o modificadas por accidente.

---

## Problema común que resuelve
En sistemas grandes, a menudo se necesita **un único punto de control** para manejar:
- Configuraciones globales.
- Registros (*logs*).
- Conexiones a bases de datos.
- Controladores de eventos o recursos compartidos.

Sin un Singleton, podrían existir **múltiples instancias independientes**, lo que genera:
- Datos inconsistentes entre módulos.
- Mayor uso de memoria y recursos.
- Dificultad para sincronizar cambios globales.

El Singleton soluciona este problema proporcionando **una única instancia compartida** a todo el sistema.

---

## Casos de uso comunes

- **Control de eventos:**  
  Cuando se requiere que un único servicio notifique a todas las partes del sistema ante la ocurrencia de un evento, manteniendo la coherencia y evitando la replicación.

- **Conexión a base de datos:**  
  Útil cuando se necesita una sola instancia que administre la conexión a la base de datos, evitando la creación de múltiples conexiones simultáneas.

- **Configuración global:**  
  Ideal cuando todas las partes del sistema deben compartir la misma configuración, evitando cargas repetidas del mismo archivo.

---

## UML Singleton
![Diagrama UML del Singleton](/software-design-II-2025/Lab3/Imagenes/Singleton.png)

## Explicación del UML y estructura de código
![Diagrama UML del Singleton](/software-design-II-2025/Lab3/Imagenes/Singleton_Proyect.png)
### **Clases principales:**
- **Client:**  
  Utiliza la clase `CustomLogger`, la cual es compartida por todas las instancias que la necesiten.

- **CustomLogger:**  
  - Mantiene una **única instancia** de sí misma.  
  - Contiene una **bandera (`initialized`)** que indica si ya fue creada la instancia.  
  - Es el objeto central encargado de registrar *logs*.

### **Métodos clave:**
- `new()`: Controla la creación de la instancia, garantizando que solo se cree una vez.
  
- `__init__()`: Inicializa el logger solo si no ha sido inicializado previamente, usando la variable `initialized`.

- `log()`: Método que permite registrar mensajes o eventos en el log compartido.

---

## Cómo mejora el mantenimiento y la escalabilidad
El patrón **Singleton** mejora la mantenibilidad al centralizar la gestión de recursos globales.  
Al tener una sola instancia:
- Se **evita la duplicación de código** y configuración.  
- Cualquier cambio en la instancia se **propaga automáticamente** a todo el sistema.  
- Facilita el mantenimiento, ya que el comportamiento global está concentrado en un solo punto.  

Sin embargo, **no siempre es ideal para escalabilidad horizontal**, especialmente en sistemas distribuidos, donde puede ser necesario manejar múltiples instancias coordinadas (por ejemplo, en microservicios o entornos con múltiples procesos).

---

## Ventajas
- **Control de instancia:** Garantiza que solo exista un objeto de la clase.  
- **Ahorro de recursos:** Reduce el consumo de memoria y procesamiento.  
- **Consistencia de datos:** Toda la aplicación usa la misma información.  
- **Centralización:** Simplifica la gestión de configuraciones y estados globales.

---

## Desventajas
- **Dificultad en pruebas unitarias:** Es más complicado simular o aislar la instancia única durante el testing.
- **Acoplamiento global:** El acceso global puede generar dependencias difíciles de rastrear.
- **Riesgo de estado compartido:** Si no se maneja correctamente, los cambios en el estado del Singleton pueden afectar otras partes del sistema de forma inesperada.
- **Violación del principio de responsabilidad única (SRP):** La clase termina teniendo dos responsabilidades: su propia lógica y la gestión de su instancia.

---

## Conclusión
El patrón Singleton se utiliza para garantizar que una clase tenga una única instancia durante toda la ejecución del programa, permitiendo que diferentes módulos o componentes compartan los mismos datos o configuraciones sin duplicarlos.

En el contexto de este proyecto, su aplicación resulta especialmente útil para el manejo centralizado de logs, ya que evita la creación de múltiples instancias del logger, previniendo así la duplicación de handlers, las configuraciones inconsistentes y el exceso de consumo de memoria.

Gracias a la implementación del Singleton, se mantiene una única instancia compartida entre todos los módulos que la importan. Esto asegura que todos los mensajes de log generados en distintas partes del sistema sigan el mismo formato, lo cual garantiza la homogeneidad en los reportes, facilita la auditoría y centraliza la información registrada.

En conjunto, el uso del patrón Singleton en el componente CustomLogger contribuye a una mayor coherencia, eficiencia y mantenibilidad del sistema de registro, consolidando una estructura de logs uniforme y confiable en toda la aplicación.

## Bibliografía
Singleton. (2024, enero 1). Refactoring.Guru. https://refactoring.guru/design-patterns/singleton?utm_source

Singleton design pattern. (s/f). Sourcemaking.com. Recuperado el 1 de noviembre de 2025, de https://sourcemaking.com/design_patterns/singleton

Leiva, A. (s/f). Singleton - Patrones de diseño. Devexpert.io. Recuperado el 1 de noviembre de 2025, de https://devexpert.io/blog/singleton-patrones-diseno



