from abc import ABC, abstractmethod
import threading
import time
import random
import queue

# Producto Abstracto
class Pedido(ABC):
    def __init__(self, id):
        self.id = id
        self.estado = "pendiente"
        self.tipo = ""
    
    @abstractmethod
    def preparar(self):
        pass

# Productos Concretos
class Hamburguesa(Pedido):
    def __init__(self, id):
        super().__init__(id)
        self.tipo = "Hamburguesa"
    
    def preparar(self):
        tiempo_preparacion = random.uniform(1, 3)
        time.sleep(tiempo_preparacion)  # Simula tiempo de preparación
        self.estado = "listo"
        return f"Hamburguesa {self.id} preparada (tiempo: {tiempo_preparacion:.2f}s)"

class Pizza(Pedido):
    def __init__(self, id):
        super().__init__(id)
        self.tipo = "Pizza"
    
    def preparar(self):
        tiempo_preparacion = random.uniform(2, 4)
        time.sleep(tiempo_preparacion)
        self.estado = "listo"
        return f"Pizza {self.id} preparada (tiempo: {tiempo_preparacion:.2f}s)"

# Creator Abstracto
class CreadorPedidos(ABC):
    @abstractmethod
    def crear_pedido(self, id):
        pass

# Concrete Creators
class CreadorHamburguesas(CreadorPedidos):
    def crear_pedido(self, id):
        return Hamburguesa(id)

class CreadorPizzas(CreadorPedidos):
    def crear_pedido(self, id):
        return Pizza(id)

# Servicio Principal con concurrencia
class ServicioPedidos:
    def __init__(self, num_cocineros=2):
        self.cola_pedidos = queue.Queue()
        self.pedidos_procesados = []
        self.lock = threading.Lock()
        self.num_cocineros = num_cocineros
        self.cocineros = []
        
    def agregar_pedido(self, pedido):
        self.cola_pedidos.put(pedido)
    
    def cocinero_worker(self, id_cocinero):
        while True:
            try:
                # Obtener pedido de la cola (con timeout para evitar bloqueo permanente)
                pedido = self.cola_pedidos.get(timeout=2)
                
                if pedido is None:  # Señal para terminar
                    break
                    
                print(f"[COCINERO {id_cocinero}] Preparando pedido {pedido.id} ({pedido.tipo})")
                
                # Preparar el pedido
                resultado = pedido.preparar()
                
                # Usar lock para actualizar la lista de forma segura
                with self.lock:
                    self.pedidos_procesados.append(pedido)
                
                print(f"[EVENTO] Pedido {pedido.id} listo: {resultado}")
                
                # Marcar tarea como completada
                self.cola_pedidos.task_done()
                
            except queue.Empty:
                # No hay más pedidos en la cola
                break
    
    def procesar_pedidos(self):
        # Crear e iniciar cocineros (hilos)
        for i in range(self.num_cocineros):
            cocinero = threading.Thread(target=self.cocinero_worker, args=(i+1,))
            cocinero.daemon = True
            cocinero.start()
            self.cocineros.append(cocinero)
        
        # Esperar a que todos los pedidos sean procesados
        self.cola_pedidos.join()
        
        print("[SISTEMA] Todos los pedidos han sido procesados")
        
        # Mostrar resumen
        print("\n--- RESUMEN DE PEDIDOS ---")
        with self.lock:
            for pedido in self.pedidos_procesados:
                print(f"Pedido {pedido.id} ({pedido.tipo}): {pedido.estado}")

# Main para prueba
if __name__ == "__main__":
    # Crear servicio con 2 cocineros
    servicio = ServicioPedidos(num_cocineros=2)
    
    # Factory para hamburguesas
    creador_hamburguesas = CreadorHamburguesas()
    for i in range(3):
        pedido = creador_hamburguesas.crear_pedido(i)
        servicio.agregar_pedido(pedido)
    
    # Factory para pizzas
    creador_pizzas = CreadorPizzas()
    for i in range(3, 6):  # IDs 3, 4, 5
        pedido = creador_pizzas.crear_pedido(i)
        servicio.agregar_pedido(pedido)
    
    # Procesar todos los pedidos
    servicio.procesar_pedidos()