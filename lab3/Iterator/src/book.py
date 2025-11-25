class Book:
    """Clase que representa un libro"""

    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"'{self.title}' por {self.author} ({self.genre})"
