# software-design-II-2025

## James Araya Rodríguez - B70528
## UCR - Laboratorio 2

### Ejercicio 2
La mini app posee su propio README por tal razón se decidio adjuntar el siguiente link para poder ver toda la información asociada y las pruebas de los ejercicios asicnados.
[Ir al README de la– Mini App Flask](labs/lab2_miniapp_Flask/README.md)

### Investigue y conteste únicamente una de las siguientes tres preguntas (15%)
Seleccione la pregunta que le parezca más interesante

#### 1. ¿Cuál sería una buena arquitectura de software a realizar con el framework que seleccionó "Flask".

Con Flask una arquitectura recomendable podria ser una que utilice MVC(Modelo, Vista, COntrolador) simplificada.
El Modelo representaria los datos y parte de la logica del negocio.
El controlador representaria la parte que maneja las rutas GET y POST y parte de la logica del negocio. Además, de la funcionalidad de comunicarse con el modelo. 
El controlador seria la parte que debe interactuar con el usuario y comunicarse con el resto del sistema. 

#### ¿Por qué?

Considero que la separación en el uso del MVC facilita la mantenibilidad del codigo, además permitiria promover la modularización del codigo y el futuro crecimiento
y modificación del mismo facilitando pruebas unitarias. 
