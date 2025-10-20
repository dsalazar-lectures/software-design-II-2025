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