# software-design-II-2025

## James Araya Rodríguez - B70528
## UCR - Laboratorio 2

### Ejercicio 1

Quieres combinar múltiples commits pequeños en uno solo para dejar el historial más
limpio, antes de enviar al remoto. ¿Qué comando se utiliza?

> b) git rebase -i


Hiciste un commit con un mensaje incorrecto y aún no lo has enviado al repositorio remoto.
¿Cuál es el comando correcto para modificar el mensaje del último commit?

> c) git commit --amend


Subiste un commit al repositorio remoto con un error y necesitas deshacerlo creando un
nuevo commit que revierta los cambios. ¿Qué comando usarías?

> b) git revert HEAD


Brevemente indique, ¿cuál es la diferencia principal entre git clone y git fork en GitHub?
> git clone: Descarga una copia local de un repositorio remoto existente, manteniendo el enlace con el repositorio original.

> git fork: Crea una copia en tu propia cuenta de GitHub (repositorio remoto independiente), permitiendo contribuir mediante pull requests sin afectar el repo original directamente.

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
