from abc import ABC, abstractmethod


class Iterator(ABC):
    """Interfaz base para los iteradores"""

    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass
