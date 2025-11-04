# Patrón de Diseño: `Mediator`

José Manuel Mora Z - C35280

## Definición

El patrón de diseño `Mediator` es un patrón de comportamiento que permite reducir el caos de dependencias entre objetos. El patrón restringe la comunicación directa entre los objetos y los obliga a colaborar a través de un objeto mediador centralizado. [1]

## Problema a resolver

En sistemas con múltiples objetos que interactúan entre sí, la comunicación directa puede llevar a un acoplamiento fuerte, lo que dificulta el mantenimiento y la escalabilidad del software. Cada objeto puede depender de muchos otros, lo que complica la gestión de cambios y la comprensión del sistema en su conjunto. [1]

### Solución al problema

El patrón `Mediator` aborda este problema al centralizar la comunicación en un mediador, lo que reduce las dependencias entre los objetos y facilita la gestión de las interacciones. Esto también tiene como beneficio el permitir la reutilización de componentes, ya que los objetos no dependen directamente unos de otros. [1]

## Impacto sobre el mantenimiento y escalabilidad del software

El uso del patrón `Mediator` mejora significativamente el mantenimiento y la escalabilidad del software. Al centralizar la comunicación, los cambios en un objeto no afectan directamente a otros, lo que facilita la implementación de nuevas funcionalidades y la corrección de errores. Además, el mediador puede ser modificado o reemplazado sin afectar a los objetos que interactúan a través de él, lo que permite una mayor flexibilidad en la evolución del sistema.

## Estructura

![Estructura del patrón Mediator](https://refactoring.guru/images/patterns/diagrams/mediator/structure-indexed-1.5x.png)

1. **Componentes**: Son las clases que contienen la lógica de negocio. Cada uno tiene una referencia al mediador, declarada con el tipo de interfaz del mediador. El componente no conoce la clase concreta del mediador, lo que permite cambiar el mediador sin afectar a los componentes.
2. **Interfaz del Mediador**: Declara los métodos de comunicación con los componentes, que usualmente es simplemente una función de notificación única.
3. **Mediador Concreto**: Encapsulan las relaciones entre varios componentes. Usualmente mantienen referencias a todos los componentes que gestionan e incluso manejan su ciclo de vida en algunos casos.
4. Los componentes no deben conocer otros componentes. Si algo importante ocurre dentro o a un componente, este debe notificar solo al mediador. Este puede identificar al emisor y decidir que hacer en consecuencia. [1]

Desde la perspectiva del componente, todo es una caja negra. El emisor no sabe quién se encarga de su request y el receptor no sabe quien la envió para empezar. [1]

## Aplicabilidad

El patrón `Mediator` es aplicable en los siguientes escenarios:

* Cuando es difícil modificar alguna clase debido a que está estrechamente acoplada a muchas otras clases.
  * El patrón permite extraer las relaciones entre clases a una clase aparte, lo que aísla los cambios hechos a un componente del resto del sistema.
* Cuando no se puede reutilizar un componente debido a que es demasiado dependiente de otros componentes.
  * Luego de aplicar el patrón, los componentes individuales dejan de conocer al resto. Esto permite reutilizarlos en otros contextos, siendo la única dependencia el mediador.
* Cuando se están creando muchas subclases solo para reutilizar comportamientos básicos en diferentes contextos.
  * Ya que las relaciones entre componentes se manejan en el mediador, es fácil definir nuevas formas de colaboración entre componentes creando nuevos mediadores, en lugar de nuevos subtipos de componentes. [1]

## Ventajas y Desventajas

| Ventajas | Desventajas |
|:---------|:------------|
| SRP. Se pueden extraer las comunicaciones entre componentes a un solo lugar. Facilitando la comprensión y el mantenimiento del código. | Puede volverse un "God Object" que conoce demasiado sobre los componentes y sus interacciones, lo que dificulta su mantenimiento. |
| OPP. Se pueden introducir nuevos mediadores sin tener que cambiar los componentes | |
| Reduce acoplamiento entre componentes. | |
| Facilita la reutilización de componentes. | |

## Relaciones con otros patrones

## Cómo implementar

## Ejemplo de Código

## Referencias

[1] Refactoring.Guru, “Mediator,” Refactoring.Guru, Jan. 01, 2025. https://refactoring.guru/design-patterns/mediator
