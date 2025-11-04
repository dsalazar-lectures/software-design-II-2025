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

## Ejemplo

## Ventajas y Desventajas

## Referencias

[1] Refactoring.Guru, “Mediator,” Refactoring.Guru, Jan. 01, 2025. https://refactoring.guru/design-patterns/mediator
