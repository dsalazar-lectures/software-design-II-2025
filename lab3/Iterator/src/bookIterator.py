from iterator import Iterator
from typing import List


class BookIterator(Iterator):
    """Iterador que recorre los libros en orden secuencial"""

    def __init__(self, books: List):
        self._books = books
        self._position = 0

    def has_next(self):
        return self._position < len(self._books)

    def next(self):
        if self.has_next():
            book = self._books[self._position]
            self._position += 1
            return book
        return None
