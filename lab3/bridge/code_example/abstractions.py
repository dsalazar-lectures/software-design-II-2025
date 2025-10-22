from code_example.implementors import DataSource
from abc import ABC, abstractmethod

# --- Abstraction ---
class DataVisualization(ABC):
    def __init__(self, data_source: DataSource):
        self._data_source = data_source

    @abstractmethod
    def display(self):
        pass

    def set_data_source(self, new_source: DataSource):
        self._data_source = new_source


# --- Refined Abstractions ---
class BarChart(DataVisualization):
    def display(self):
        data = self._data_source.get_data()
        print("📊 Gráfico de barras con datos:", data)


class PieChart(DataVisualization):
    def display(self):
        data = self._data_source.get_data()
        print("🥧 Gráfico de pie con datos:", data)


class LineChart(DataVisualization):
    def display(self):
        data = self._data_source.get_data()
        print("📈 Gráfico de líneas con datos:", data)