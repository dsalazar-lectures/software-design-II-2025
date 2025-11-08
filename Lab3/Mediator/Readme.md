# Patrón de Diseño: `Mediator`

José Manuel Mora Z - C35280

## Definición

El patrón de diseño `Mediator` es un patrón de comportamiento que permite reducir el caos de dependencias entre objetos. El patrón restringe la comunicación directa entre los objetos y los obliga a colaborar a través de un objeto mediador centralizado. [[1]](#referencias)

## Problema a resolver

En sistemas con múltiples objetos que interactúan entre sí, la comunicación directa puede llevar a un acoplamiento fuerte, lo que dificulta el mantenimiento y la escalabilidad del software. Cada objeto puede depender de muchos otros, lo que complica la gestión de cambios y la comprensión del sistema en su conjunto. [[1]](#referencias)

### Solución al problema

El patrón `Mediator` aborda este problema al centralizar la comunicación en un mediador, lo que reduce las dependencias entre los objetos y facilita la gestión de las interacciones. Esto también tiene como beneficio el permitir la reutilización de componentes, ya que los objetos no dependen directamente unos de otros. [[1]](#referencias)

## Impacto sobre el mantenimiento y escalabilidad del software

El uso del patrón `Mediator` mejora significativamente el mantenimiento y la escalabilidad del software. Al centralizar la comunicación, los cambios en un objeto no afectan directamente a otros, lo que facilita la implementación de nuevas funcionalidades y la corrección de errores. Además, el mediador puede ser modificado o reemplazado sin afectar a los objetos que interactúan a través de él, lo que permite una mayor flexibilidad en la evolución del sistema.

## Estructura

![Estructura del patrón Mediator](https://refactoring.guru/images/patterns/diagrams/mediator/structure-indexed-1.5x.png)
*Imagen: Refactoring.Guru - Mediator Pattern [[1]](#referencias)*

1. **Componentes**: Son las clases que contienen la lógica de negocio. Cada uno tiene una referencia al mediador, declarada con el tipo de interfaz del mediador. El componente no conoce la clase concreta del mediador, lo que permite cambiar el mediador sin afectar a los componentes.
2. **Interfaz del Mediador**: Declara los métodos de comunicación con los componentes, que usualmente es simplemente una función de notificación única.
3. **Mediador Concreto**: Encapsulan las relaciones entre varios componentes. Usualmente mantienen referencias a todos los componentes que gestionan e incluso manejan su ciclo de vida en algunos casos.
4. Los componentes no deben conocer otros componentes. Si algo importante ocurre dentro o a un componente, este debe notificar solo al mediador. Este puede identificar al emisor y decidir que hacer en consecuencia. [[1]](#referencias)

Desde la perspectiva del componente, todo es una caja negra. El emisor no sabe quién se encarga de su request y el receptor no sabe quien la envió para empezar. [[1]](#referencias)

## Aplicabilidad

El patrón `Mediator` es aplicable en los siguientes escenarios:

* Cuando es difícil modificar alguna clase debido a que está estrechamente acoplada a muchas otras clases.
  * El patrón permite extraer las relaciones entre clases a una clase aparte, lo que aísla los cambios hechos a un componente del resto del sistema. [[1]](#referencias)
* Cuando no se puede reutilizar un componente debido a que es demasiado dependiente de otros componentes.
  * Luego de aplicar el patrón, los componentes individuales dejan de conocer al resto. Esto permite reutilizarlos en otros contextos, siendo la única dependencia el mediador. [[1]](#referencias)
* Cuando se están creando muchas subclases solo para reutilizar comportamientos básicos en diferentes contextos.
  * Ya que las relaciones entre componentes se manejan en el mediador, es fácil definir nuevas formas de colaboración entre componentes creando nuevos mediadores, en lugar de nuevos subtipos de componentes. [[1]](#referencias)

## Ventajas y Desventajas

| Ventajas | Desventajas |
|:---------|:------------|
| SRP. Se pueden extraer las comunicaciones entre componentes a un solo lugar. Facilitando la comprensión y el mantenimiento del código. [[1]](#referencias) | Si se le agregan demasiadas responsabilidades, el mediador puede convertirse en un "God Object" que conoce demasiado sobre los componentes y sus interacciones. Esto dificulta su mantenimiento, testeo y puede llegar a romper SRP. [[1]](#referencias) [[2]](#referencias) |
| OPP. Se pueden introducir nuevos mediadores sin tener que cambiar los componentes. [[1]](#referencias) | Puede llegar a crear overhead y afectar el rendimiento del programa si no se dispone de los recursos necesarios. [[2]](#referencias) |
| Reduce acoplamiento entre componentes. [[1]](#referencias) | Si las interacciones del programa son simples, implementar el patrón es complicarse la vida por gusto [[2]](#referencias) |
| Facilita la reutilización de componentes. [[1]](#referencias) |  |

## Relaciones con otros patrones

* **Chain of Responsibility**, **Command**, **Observer** y **Mediator**: Todos estos patrones abordan la comunicación entre objetos, pero de diferentes maneras:
  * *Chain of Responsibility* pasa el request secuencialmente a través de una cadena dinámica de posibles receptores hasta que uno lo maneja.
  * *Command* establece conexiones unidireccionales entre el emisor y el receptor a través de un objeto comando.
  * *Mediator* elimina las conexiones directas entre objetos y los obliga a comunicarse a través de un mediador centralizado.
  * *Observer* deja que los receptores se suscriban a y desuscriban de recibir notificaciones dinámicamente. [[1]](#referencias)
* **Facade** y **Mediator**: Ambos tienen trabajos similares: tratan de organizar la colaboración entre varios objetos estrechamente acoplados.
  * *Facade* define una interfaz simplificada para un subsistema de objetos, pero no introduces nuevas funcionalidades. El subsistema en sí no conoce a la fachada y los objetos dentro de este pueden seguir comunicándose directamente.
  * *Mediator* centraliza la comunicación entre los componentes del sistema. Los componentes solo conocen al mediador y no pueden comunicarse directamente entre sí. [[1]](#referencias)

## Cómo implementar

1. Identificar un grupo de objetos que interactúan estrechamente entre sí, que se beneficiarían de mayor independencia.
2. Declarar la interfaz del mediador y describir el protocolo de comunicación entre los componentes y mediadores. Generalmente, con un solo método de notificación basta.
   * La interfaz es crucial para la reutilización. Siempre y cuando los componentes trabajen con una interfaz genérica, se pueden enlazar con diferentes mediadores sin cambios.
3. Implementar el mediador concreto. Es recomendable guardar referencias a todos los componentes que maneja, así el mediador puede llamarlos directamente desde sus métodos.
4. Como extra, se puede responsabilizar al mediador de crear y destruir los componentes que maneja. Esto hace que el mediador pueda parecer un `Factory` o `Facade`.
5. Los componentes deberían mantener una referencia al mediador. Usualmente se le pasa el mediador al constructor del componente.
6. Cambiar los componentes para que se comuniquen solo con el mediador, en lugar de otros componentes. Extraer el código de comunicación a los métodos del mediador, que se llaman cuando el mediador es notificado por un componente. [[1]](#referencias)

## Casos de Uso

A continuación, se presenta una simple lista de casos de uso del patrón `Mediator`, pues ya se han mencionado y explicado anteriormente:

* Comunicación compleja entre componentes y se quiere reducir las dependencias.
* Reducción del acoplamiento entre componentes.
* Centralización del control sobre las interacciones entre componentes.
* Poder hacer cambios en el comportamiento de los componentes sin afectar a otros.
* Reutilización de componentes en diferentes contextos. [[2]](#referencias)

### ¿Cuándo no usar el patrón `Mediator`?

Como extra, es importante saber cuándo no usar el patrón `Mediator`:

* Cuando las interacciones entre componentes son simples, directas y no presentan un problema.
* Cuando el mediador se vuelve demasiado complejo y difícil de mantener.
* Cuando el rendimiento es crítico y la sobrecarga del mediador puede ser un problema. [[2]](#referencias)

## Testing

En tema de testing, al reducir las dependencias entre componentes, el patrón `Mediator` facilita la creación de pruebas unitarias para cada componente de manera aislada. Como cada componente solo depende del mediador, al construir el test solo se necesita incluir o mockear el mediador, en lugar de todos los componentes relacionados.

En cuanto al mediador en sí, la situación se complica un poco más, pero no en el sentido de que haya que hacer tests complejos, sino que hay que centrarse en lo importante. El mediador coordina a los componentes, por lo que éste debe ser el objetivo principal de las pruebas.

Para probar el mediador, se pueden mockear los componentes individuales y verificar que el mediador coordina correctamente las interacciones entre ellos. Esto permite asegurar que el mediador cumple su función sin necesidad de probar la lógica interna de cada componente en este contexto.

Posteriormente, se pueden realizar pruebas de integración para asegurar que los componentes y el mediador trabajan juntos correctamente en un entorno realista.

## Ejemplo de Código

El código se encuentra en [mediator_example.py](./mediator_example.py).

Este simula brevemente la creación de un menú para dos usuarios, uno con restricciones alimenticias y otro sin restricciones. El mediador se encarga de coordinar las interacciones entre los servicios de menú, recetas y perfiles de usuario.

Cada componente maneja su propia lógica, mientras que el mediador centraliza la comunicación y asegura que los componentes trabajen juntos de manera coherente.

## Referencias

[1] Refactoring.Guru, “[Mediator](https://refactoring.guru/design-patterns/mediator),” Refactoring.Guru, Jan. 01, 2025.

[2] GeeksforGeeks, “[Mediator design pattern](https://www.geeksforgeeks.org/system-design/mediator-design-pattern/),” GeeksforGeeks, Dec. 18, 2024.
