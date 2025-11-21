from connection_pool import ConnectionPool, DatabaseConnection

def main():
    # Crear el pool (singleton)
    pool = ConnectionPool()
    
    # Adquirir y usar conexiones
    conn1 = pool.acquire_connection()
    conn2 = pool.acquire_connection()
    conn3 = pool.acquire_connection()
    
    if conn1:
        conn1.execute_query("SELECT * FROM users")
    if conn2:
        conn2.execute_query("INSERT INTO logs VALUES ('test')")
    
    pool.get_pool_status()
    
    # Liberar conexiones
    if conn1:
        pool.release_connection(conn1)
    if conn2:
        pool.release_connection(conn2)
    
    pool.get_pool_status()
    
    # Adquirir más conexiones (deberían reutilizarse)
    conn4 = pool.acquire_connection()
    conn5 = pool.acquire_connection()
    
    pool.get_pool_status()

if __name__ == "__main__":
    main()