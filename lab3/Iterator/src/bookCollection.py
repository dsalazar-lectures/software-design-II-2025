from typing import List
from book import Book
from bookIterator import BookIterator
from reverseIterator import ReverseBookIterator


class BookCollection:
    """Colección de libros que proporciona diferentes iteradores"""

    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book):
        self._books.append(book)

    def create_iterator(self):
        """Crea un iterador secuencial normal"""
        return BookIterator(self._books)

    def create_reverse_iterator(self):
        """Crea un iterador que recorre en orden inverso"""
        return ReverseBookIterator(self._books)
