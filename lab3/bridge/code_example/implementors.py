from abc import ABC, abstractmethod

# --- Implementor ---
class DataSource(ABC):
    @abstractmethod
    def get_data(self):
        pass

# --- Concrete Implementors ---
class CSVDataSource(DataSource):
    def get_data(self):
        return ["A,10", "B,15", "C,7"]


class APIDataSource(DataSource):
    def get_data(self):
        return {"A": 12, "B": 20, "C": 9}


class DatabaseDataSource(DataSource):
    def get_data(self):
        return [("A", 8), ("B", 18), ("C", 11)]