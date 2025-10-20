### ¿Qué es?

El patrón State es un patrón de comportamiento que permite que un objeto cambie su comportamiento cuando su estado interno cambia. Parece como si el objeto cambiase de clase.
Por ejemplo: un documento que está en estado “Draft”, “Moderation” o “Published” se comporta de manera diferente según su estado actual.

### ¿Cuándo usarlo?

Este patrón es adecuado cuando:

- Un objeto debe comportarse de forma diferente según su estado interno.
- Hay muchas condiciones (`if`/`switch`) que dependen del estado y eso hace que el código sea difícil de mantener.
- Se esperan nuevos estados en el futuro
- Los estados cambian con frecuencia.
- El comportamiento que cambia con el estado puede agruparse de forma coherente.

Por el contrario, no se recomienda si el número de estados es muy pequeño o los comportamientos son simples, ya que puede resultar excesivo (overkill).

### ¿Cómo funciona (estructura)?

Los componentes típicos del patrón son:

- **Contexto (Context)**: es el objeto que cambia de comportamiento. Contiene una referencia al estado actual y delega el trabajo al objeto estado. También puede tener métodos propios que no se deleguen a los estados.
- **Interfaz de Estado (State interface)**: define los métodos que cada estado concreto debe implementar.
- **Estados Concretos (Concrete States)**: implementan la interfaz de estado, encapsulan el comportamiento asociado a un estado específico y, a menudo, pueden cambiar el estado del contexto.

El flujo típico es:

1. El cliente envía una petición al contexto.
2. El contexto delega al estado actual.
3. El estado realiza su comportamiento específico y puede indicarle al contexto que transicione a otro estado.
4. El contexto actualiza su referencia al nuevo estado y continúa con ese nuevo comportamiento.

### Ventajas y desventajas

**Ventajas**:

- Separa los comportamientos dependientes de estado en clases distintas (mejora principio de Responsabilidad Única).
- Facilita la extensibilidad: se pueden añadir nuevos estados sin modificar el código del contexto o los demás estados (mejora principio Abierto/Cerrado).
- Reduce la lógica condicional en el contexto, haciendo el diseño más limpio y mantenible.

**Desventajas**:

- Puede añadir complejidad innecesaria si hay pocos estados o el comportamiento es simple.
- Si los cambios de estado son muy frecuentes o hay muchos objetos y muchos estados, el seguimiento podría complicarse.
- Puede implicar creación de muchas clases adicionales (una clase por estado) y posibles sobrecargas de llamadas de método.

### Pasos básicos para implementarlo

1. Identificar la clase que actúa como contexto (ya contiene lógica que depende del estado).
2. Definir una interfaz de estado con los métodos que representarán las acciones que varían según el estado.
3. Crear clases concretas para cada estado, moviendo la lógica de las condicionales de la clase original a estos estados.
4. En el contexto, mantener una referencia al estado actual y delegar las peticiones a ese estado. Añadir método para cambiar el estado.
5. Sustituir la lógica de condicionales en el contexto por delegaciones al estado correspondiente.

## Referencias

- [Refactoring Guru](https://refactoring.guru/design-patterns/state "State")
- [GeeksforGeeks](https://www.geeksforgeeks.org/system-design/state-design-pattern/ "State Design Pattern - GeeksforGeeks")
