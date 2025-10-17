# Patrón Data Access Object (DAO)

## ¿Qué es el patrón DAO y a qué tipo pertenece?

El **patrón Data Access Object (DAO)** es un patrón de diseño estructural que abstrae y encapsula el acceso a una fuente de datos (como bases de datos) mediante una interfaz común independiente del tipo específico de almacenamiento.

Su función es aislar la lógica de negocio de los detalles de persistencia y acceso a los datos, proporcionando métodos estándar CRUD para interactuar con la fuente de datos.

## Problema que resuelve

En muchas aplicaciones, el acceso a la base de datos está acoplado directamente al código de la lógica de negoci, lo que dificulta el mantenimiento y la escalabilidad. Además, si se cambia la base de datos o su estructura, se debe modificar la lógica de negocio, incrementando el riesgo de errores.

El patrón DAO resuelve este problema separando claramente estas responsabilidades. De esta manera, la lógica de negocio no depende de detalles técnicos de acceso a datos y cualquier cambio en la base de datos afecta solo la capa DAO.


## ¿Cómo mejora el mantenimiento o escalabilidad?

- **Mantenimiento más sencillo:** la lógica de negocio queda independiente de la fuente de datos, permitiendo cambiar detalles internos sin impactar el sistema completo.  
- **Facilidad para cambiar bases de datos:** migraciones o cambios en el sistema de almacenamiento solo requieren modificar la capa DAO.  
- **Portabilidad:** permite que la aplicación soporte varias bases de datos en paralelo sin alterar la lógica principal.  
- **Mejora testabilidad:** se puede probar la lógica de negocio usando mocks del DAO, sin depender de bases de datos reales.

## Ventajas y desventajas

### Ventajas
- Separación clara de responsabilidades.  
- Código más modular y organizado.  
- Facilita la reutilización y evolución del código.  
- Mejora la testabilidad al abstraer la persistencia.

### Desventajas
- Puede añadir complejidad innecesaria en aplicaciones simples.  
- Dependencia aún puede darse con frameworks específicos de persistencia.  
- Puede implicar duplicación de código.  
- En algunos casos, el patrón **Repository** u otros pueden ser más adecuados según la arquitectura.

## Casos de uso comunes

- Aplicaciones con persistencia compleja en donde se necesite acceder a múltiples tablas o bases de datos sin mezclar la lógica de negocio con consultas SQL.  
- Sistemas donde se requiere cambiar fácilmente la fuente de datos (por ejemplo entre bases de datos SQL y noSQL)
- Aplicaciones que integran múltiples fuentes de datos, como bases SQL, archivos CSV u otros, un DAO por fuente facilita la organización del acceso.

## Código de ejemplo

### Interfaz (contrato DAO)
```py
# recipe_dao.py
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Recipe:
    id: int
    name: str
    ingredients: list[str]
    author: str

class RecipeDAO(ABC):
    @abstractmethod
    def create(self, name, ingredients, author):
        pass
    @abstractmethod
    def get_all(self):
        pass
    @abstractmethod
    def get_by_id(self, recipe_id):
        pass
    @abstractmethod
    def update(self, recipe_id, name=None, ingredients=None):
        pass
    @abstractmethod
    def delete(self, recipe_id):
        pass
```

- La capa de negocio depende del contrato (`RecipeDAO`), no de una BD concreta.
- Cambiar la persistencia no afecta a quien consume el DAO.

### Implementación
```py
# recipe_dao_impl.py
from recipe_dao import RecipeDAO, Recipe

class RecipeDAOImpl(RecipeDAO):
    def __init__(self):
        self._data = []
        self._next_id = 1

    def create(self, name, ingredients, author):
        r = Recipe(self._next_id, name.strip(), list(ingredients), author.strip())
        self._data.append(r)
        self._next_id += 1
        return r

    def get_all(self):
        return list(self._data)

    def get_by_id(self, recipe_id):
        return next((r for r in self._data if r.id == recipe_id), None)

    def update(self, recipe_id, name=None, ingredients=None):
        r = self.get_by_id(recipe_id)
        if not r:
            return None
        if name is not None:
            r.name = name.strip()
        if ingredients is not None:
            r.ingredients = list(ingredients)
        return r

    def delete(self, recipe_id):
        r = self.get_by_id(recipe_id)
        if not r:
            return False
        self._data.remove(r)
        return True
```
- Cumple el contrato, se puede reemplazar por una variante SQL, NoSQL, una API, etc...

### Uso desde la aplicación
```py
# main.py
from recipe_dao_impl import RecipeDAOImpl

def main():
    dao = RecipeDAOImpl()
    r1 = dao.create("Pasta al Pesto", ["pasta", "albahaca"], "Jose")
    r2 = dao.create("Sándwich", ["pan", "queso"], "Luis")

    print("\nRecetas:")
    for r in dao.get_all():
        print("-", r)

    dao.update(r2.id, name="Sándwich de queso")
    dao.delete(r1.id)
```
Beneficios:
- Se podría crear un DAO que interactue con una base de datos SQL y solo se debería cambiar `RecipeDAOImpl()` por `SqlRecipeDAO()` sin tocar el resto del código.
