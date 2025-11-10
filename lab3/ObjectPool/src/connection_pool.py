import threading
import time
from typing import List, Optional

class DatabaseConnection:
    def __init__(self, connection_id: int):
        self.connection_id = connection_id
        self.in_use = False
        self.created_at = time.time()
        
    def connect(self):
        print(f"Conexión {self.connection_id} establecida")
        
    def execute_query(self, query: str):
        print(f"Conexión {self.connection_id} ejecutando: {query}")
        
    def reset(self):
        """Resetea la conexión para reutilización"""
        self.in_use = False

class ConnectionPool:
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        self._available_connections: List[DatabaseConnection] = []
        self._in_use_connections: List[DatabaseConnection] = []
        self.max_size = 5
        self._initialize_pool()
    
    def _initialize_pool(self):
        """Inicializa el pool con conexiones listas para usar"""
        for i in range(self.max_size):
            connection = DatabaseConnection(i + 1)
            connection.connect()
            self._available_connections.append(connection)
    
    def acquire_connection(self) -> Optional[DatabaseConnection]:
        """Obtiene una conexión del pool"""
        if self._available_connections:
            connection = self._available_connections.pop()
            connection.in_use = True
            self._in_use_connections.append(connection)
            print(f"Conexión {connection.connection_id} adquirida")
            return connection
        else:
            print("No hay conexiones disponibles en el pool")
            return None
    
    def release_connection(self, connection: DatabaseConnection):
        """Devuelve una conexión al pool"""
        if connection in self._in_use_connections:
            self._in_use_connections.remove(connection)
            connection.reset()
            self._available_connections.append(connection)
            print(f"Conexión {connection.connection_id} liberada")
    
    def get_pool_status(self):
        """Muestra el estado actual del pool"""
        print(f"\nEstado del Pool:")
        print(f"Disponibles: {len(self._available_connections)}")
        print(f"En uso: {len(self._in_use_connections)}")
        print(f"Total: {self.max_size}")