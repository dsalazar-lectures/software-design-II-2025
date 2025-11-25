from iterator import Iterator
from typing import List


class ReverseBookIterator(Iterator):
    """Iterador que recorre los libros en orden inverso"""

    def __init__(self, books: List):
        self._books = books
        self._position = len(books) - 1

    def has_next(self) -> bool:
        return self._position >= 0

    def next(self):
        if self.has_next():
            book = self._books[self._position]
            self._position -= 1
            return book
        return None
