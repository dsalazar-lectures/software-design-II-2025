# Patrón Command

Geiner Montoya Barrientos

Carné C25063

## ¿Qué es Command?

El patrón Command (Comando) es un patrón de diseño comportamental que encapsula una petición o acción como un objeto. Al envolver una operación en un objeto, el patrón desacopla al objeto que invoca la operación (invocador) del objeto que la realiza (receptor). Esto permite parametrizar objetos con operaciones, almacenar y ejecutar operaciones más tarde, mantener un historial para deshacer/rehacer, y soportar colas y procesamiento asíncrono.

## Problema que resuelve

Cuando el código consumidor (invocador) necesita ejecutar operaciones sobre distintos receptores o realizar acciones que deben ser ejecutadas en distintos momentos (por ejemplo: programadas, en cola o de forma remota), el acoplamiento directo entre el invocador y las acciones dificulta la extensión, el registro y la gestión del historial. El patrón Command resuelve este problema separando la petición (qué se quiere hacer) de su ejecución (cómo se hace), encapsulando la petición en un objeto que puede pasarse, almacenarse y manipularse.

## Ventajas

- Desacoplamiento del Invocador y Receptor.
- Soporte para operaciones Deshacer/Rehacer (Undo/Redo).
- Facilita el uso de Colas de Comandos y procesamiento asíncrono.

## Desventajas

- Aumento de la complejidad y de la cantidad de clases.
- Mayor sobrecarga para tareas muy simples.
- Posible aumento del uso de memoria (al almacenar el historial de comandos).

## Partes que lo forman (participantes)

- Client (Cliente): Crea y configura objetos comando asociándoles un receptor y, opcionalmente, parámetros. El cliente instancia ConcreteCommand y lo entrega al invocador.
- Command (Interfaz/Abstracción): Declara una interfaz común para ejecutar la acción, normalmente un método como `execute()`; puede incluir métodos para `undo()`/`redo()` si se soporta historial.
- ConcreteCommand (Comando concreto): Implementa la interfaz `Command`, mantiene una referencia al Receiver y llama a las operaciones concretas del receptor en su método `execute()`. También puede almacenar el estado necesario para `undo()`.
- Receiver (Receptor): Objeto que conoce cómo realizar las operaciones concretas. El comando delega la ejecución en el receptor.
- Invoker (Invocador): Pide al comando que ejecute la petición. Puede almacenar comandos, invocarlos en distintos momentos, y mantener un historial para deshacer/rehacer.
- (Opcional) MacroCommand: Un comando que agrupa y ejecuta una lista de comandos (útil para operaciones compuestas o grabar macros).
- (Opcional) History/Stack: Estructura que almacena comandos ejecutados para soportar `undo`/`redo`.

## Flujo típico

1. El Client crea una o más instancias de ConcreteCommand, pasando referencias al Receiver y parámetros necesarios.
2. El Client registra o pasa el ConcreteCommand al Invoker.
3. El Invoker llama a `execute()` sobre el Command cuando corresponda.
4. El ConcreteCommand invoca operaciones en el Receiver para realizar la acción.
5. Si se necesita `undo`, el ConcreteCommand implementa `undo()` y el Invoker lo llama usando el historial.

## Casos de uso comunes

- Sistemas con acciones de usuario reversibles (editores con undo/redo).
- Colas de tareas y ejecución diferida (job queues, tasks programadas).
- Implementación de operaciones en UIs (botones que ejecutan comandos).
- Implementación de macros o grabación de secuencias de acciones.
- Comunicación distribuida (serializar comandos para ejecutarlos en otra máquina).



