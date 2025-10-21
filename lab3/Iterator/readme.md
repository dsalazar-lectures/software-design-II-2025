# Patrón Iterador

- Javier Cruz. C02517

## Definición

Iterator es un patrón de diseño de comportamiento que permite recorrer los elementos de una colección sin exponer su representación, por ejemplo lista, pila,stack, árbol, etc... 

## Problema que resuelve

Si bien los conjuntos son uno de los tipos de datos más usados en la programación, no dejan de ser un contenedor para un grupo de objetos. 

Independientemente de cómo se estructure una colección, se debe proporcionar alguna forma de acceder a sus elementos para que otro código pueda utilizarlos, es decir, debe existir una manera de recorrer cada elemento de la colección sin acceder a los mismos elementos repetidamente. 

Al tratar de acceder a dichos elementos, puede ser sencillo si se tiene una lista simple, el problema viene cuando se necesita recorrer de manera secuencial en una estructura más compleja como un árbol. Por ejemplo, en algún momento se puede requerir una búsqueda en profundidad, luego en anchura, y luego algo como acceso aleatorio.

Agregar diferentes algoritmos de recorrido al árbol puede opacar su responsabilidad principal, que es almacenar datos de manera eficiente. Por otro lado, puede que el código fuente de un programa almacene datos de diferentes formas, el problema principal radica en que las colecciones tiene diferentes formas de acceder a sus datos, por lo que hay que adaptar el código a estas colecciones específicas.

## Solución al problema

La idea principal del patrón iterator es extraer el comportamiento de recorrido de una colección en un objeto separado llamado iterador.

Además de implementar el algoritmo en sí, un iterador encapsula todos los detalles del recorrido, como la posición actual y cuántos elementos quedan hasta el final. Debido a esto, varios interadores pueden recorrer la misma colección al mismo tiempo, independientemente unos de otros.

Por lo general, los iteradores proporcionan un método principal para obtener elementos de una colección. Este método se puede seguir ejecutando hasta que no devuelva nada, lo que significa que iterator ha recorrido todos los elementos. 

Todos los iteradores deben implementar la misma interfaz. Esto hace que el código sea compatible con cualquier tipo de colección o cualquier algoritmo de recorrido, siempre que haya un iterador adecuado. En caso de necesitar una forma especial de recorrer una colección, se puede crear una nueva clase iteradora, sin tener que cambiar la colección.

## Ejemplo de Iterator

Un ejemplo de la vida real sobre cómo funciona iterator lo podemos encontrar al estar visitando una ciudad, en la que tratamos de encontrar destinos turísticos sin mucho éxito. En este caso se tienen varias opciones, la primera sería descargar una aplicación para ubicarse en la ciudad, esto puede ser poco costoso y rápido. Otra opción sería contratar a un guía turístico con el cuál se va a disfrutar más el viaje, pero también será más costoso. Tanto las direcciones aleatorias tratando de buscar algún lugar, como la aplicación, como el guía turístico, son iteradores sobre la colección de atractivos turísticos de la ciudad.

Otro ejemplo de iterador se da cuando tenemos una playlist con diferentes canciones, en esta playlist tenemos opciones para reproducirla en orden secuencial o en modo aleatorio. Estos modos de reproducción tambipén actúan como iteradores sobre la misma colección de canciones, donde se puede cambiar de modo sin afectar la colección y donde se mantiene la canción actual al cambiarlo.

## Estructura de Itrerator

- La interfaz *Iterator* declara la operación requerida para recorrer la colección: obtener el siguiente elemento, recuperar la posición actual o reiniciar la iteración.

- Los interadores concretos implementan algoritmos específicos apra recorrer una colección. El objeto iterador debe rastrear el progreso del recorrido por sí mismo, lo cual permite que varios iteradores reocrran la misma colección independientemente unos de otros.

- La colección declara uno o varios métodos para obtener iteradores compatibles con la colección. El tipo de retorno de los métodos debe declararse como la interfaz del iterador para que las colecciones concretas puedan devolver varios tipos de iteradores.

- Las colecciones concretas devuelven nuevas instancias de una clase iteradora concreta particular cada vez que el cliente solicita una. El resto del código de la colección se encuentra en esta misma clase.

- El cliente trabaja tanto con colecciones como con iteradores a través de sus interfaces. De esta manera, el cliente no está acoplado a clases concretas, lo que permite utilizar varias colecciones e iteradores con el mismo código cliente.

## ¿Cómo mejora el mantenimiento y la escalabilidad del sistema?

- **Separación de responsabilidades:** Si se tiene una estructura de datos compleja, el iterador puede encapsular detalles en partes más sencillas, proporcionando métodos más simples para acceder los datos. 

- **Reducir la duplicación de código:** El código para algoritmos de iteración puede ser extenso. Si se integra ese código dentro de una aplicación, se puede perder la responsabilidad del código original y complicar su mantenimiento.

- **Facilita la escalabilidad:** El patrón se puede utilizar para recorrer estructuras de datos de las que se desconoce su tipo. Iterator tiene interfaces genéricas para colecciones e iteradores. Al usar estas colecciones, se pueden pasar diferentes tipos de colecciones e iteradores que implementen estas interfaces.

## Ventajas y desventajas

### Ventajas

- **Single Responsibility Principle:** Permite limpiar el código al extraer algoritmos de reocrrido a clases separadas.

- **Open/Closed Principle:** Se puede implementar nuevos tipos de colecciones e iteradores y pasarlos al código existente sin que deje de funcionar el programa.

- **Iterar en paralelo:** Dado que cada objeto iterador contiene su propio estado de iteración, se permite iterar la misma colección en paralelo.

- **Retrasar una iteración:** Por la misma razón (cada iterador contiene su estado de iteración), se puede retrasar una iteración y continuar cuando sea necesario. 

### Desventajas

- **Overkill:** Puede darse si la aplicación trabaja con colecciones simples.

- **Eficiencia:** Usar un iterador puede ser menos eficiente para algunas colecciones especializadas

### Presentación
[Presentación de patrón iterador](https://www.canva.com/design/DAG2Yus0nS4/pxQxIZwNADJValq16VKdXg/edit?utm_content=DAG2Yus0nS4&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Referencias

[Refactoring.guru - Iterator Pattern](https://refactoring.guru/design-patterns/iterator)