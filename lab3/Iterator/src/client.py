from book import Book
from iterator import Iterator
from bookCollection import BookCollection


def print_books(iterator: Iterator, title: str):
    """Función cliente que usa el iterador sin conocer su implementación"""
    print(f"\n{title}")
    while iterator.has_next():
        book = iterator.next()
        print(f"  {book}")


def main():
    # Crear la colección de libros
    library = BookCollection()

    # Agregar libros
    library.add_book(Book("Cien años de soledad", "Gabriel García Márquez", "Ficción"))
    library.add_book(Book("1984", "George Orwell", "Distopía"))
    library.add_book(Book("El Quijote", "Miguel de Cervantes", "Clásico"))
    library.add_book(Book("Fahrenheit 451", "Ray Bradbury", "Distopía"))
    library.add_book(Book("Rayuela", "Julio Cortázar", "Ficción"))

    # 1. Iterador secuencial
    sequential_iterator = library.create_iterator()
    print_books(sequential_iterator, "Recorrido Secuencial:")

    # 2. Iterador inverso
    reverse_iterator = library.create_reverse_iterator()
    print_books(reverse_iterator, "Recorrido Inverso:")


if __name__ == "__main__":
    main()
