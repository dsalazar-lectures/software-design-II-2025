# Lab 3 — Patrón **Observer** aplicado a Auditoría y Logging (Python)

**Estudiante:** Christopher Obando Salgado  
**Carnet:** C05610  
**Curso:** Diseño de Software

----------

## 1) Justificación (caso de uso del proyecto)

El proyecto requiere **auditar acciones** (crear/editar/eliminar usuarios, recetas, vetos, etc.) y enviar cada evento a **múltiples destinos**: consola para depuración, **JSONL** y **CSV** para ingesta/analítica, **TXT** para revisión rápida y **métricas** en memoria (contadores).  
Con **Observer**, la lógica de dominio solo “publica” un evento; **cada destino es un observador** independiente (handler) que reacciona sin acoplarse al módulo de negocio. Esto permite **agregar o quitar** destinos sin tocar la funcionalidad central.

----------

## 2) Parte teórica (50%)

### 2.1 Definición y tipo

**Observer** es un patrón **de comportamiento** que define una dependencia **uno-a-muchos** entre objetos: cuando el _Subject/Publisher_ cambia de estado (o publica un evento), **notifica automáticamente** a todos sus _Observers_ suscritos.

### 2.2 Problema común que resuelve

Evita el **acoplamiento fuerte** entre la fuente de eventos y sus consumidores. Sin Observer, el módulo que genera el evento debería conocer **cómo** y **dónde** escribir (archivo, base, métricas, correo…), volviendo el código rígido y difícil de mantener.

### 2.3 Cómo mejora mantenimiento o escalabilidad

-   **Bajo acoplamiento / OCP:** se agregan nuevos observadores sin modificar el _Subject_.
    
-   **Reuso y pruebas:** se “mockean” observers en tests sin tocar la lógica de negocio.
    
-   **Evolución segura:** se puede escalar a más destinos (p. ej., colas/event bus) sin romper el dominio.
    

### 2.4 Otras ventajas y desventajas

**Ventajas**

-   Extensible y fácil de entender (uno-a-muchos).
    
-   Favorece **separación de responsabilidades** (SoC) y principio **OCP**.
    

**Desventajas**

-   El **orden** de notificación no está garantizado si no se define.
    
-   Puede ser más difícil de depurar si hay **cadenas** de notificaciones.
    
-   Si los observadores realizan **I/O pesado**, conviene **asincronía/colas** para no bloquear.
    

### 2.5 Referencias breves

-   Refactoring.guru — Observer: [Link](https://refactoring.guru/es/design-patterns/observer)
    
-   Python `logging` (handlers/appenders como observadores): [Link](https://docs.python.org/3/library/logging.html)
    

----------

## 3) Parte práctica (50%)

Este repo implementa un **mini framework** usando `logging` de Python como _Subject_ y varios **Handlers** como _Observers_:

-   `JSONLinesHandler`: escribe **una línea JSON por evento** (`audit.jsonl`).
    
-   `CSVHandler`: escribe una fila **CSV** por evento (`audit.csv`).
    
-   `PlainTextHandler`: escribe una línea **TXT** formateada por evento (`audit.txt`).
    
-   `MetricsHandler`: mantiene **conteos en memoria** por `action|LEVEL`.
    
-   `StreamHandler` (consola): para ver los eventos en tiempo real.
    

### 3.1 Estructura de carpetas

```
lab3/
  observer/
    README.md              # este documento
    src/
      custom_logger.py     # implementación (Observer sobre logging)
      demo.py              # script de demostración
    out/                   # se generan audit.jsonl, audit.csv y audit.txt

```

### 3.2 Requisitos

-   Python **3.10+** (no requiere dependencias externas).
    

### 3.3 Cómo ejecutar el ejemplo

```bash
# desde la raíz del repositorio
python lab3/observer/src/demo.py

```

**Resultados esperados:**

-   Salida en **consola** con los eventos.
    
-   Archivos generados en `lab3/observer/out/`:
    
    -   `audit.jsonl` (formato JSONL, una línea por evento)
        
    -   `audit.csv` (encabezado + filas por evento)
        
    -   `audit.txt` (líneas de texto plano formateadas)
        
-   Impresión en consola de **métricas** (conteo por `action|LEVEL`).
    

### 3.4 API de uso (en el código)

```python
from custom_logger import CustomLogger, build_default_handlers

logger = CustomLogger("AuditLogger", handlers=build_default_handlers())

logger.info(   user="u-001", role="superadmin", action="create_user",   description="Created demo user")
logger.warning(user="u-002", role="admin",      action="ban_user",      description="Temporary ban (24h)")
logger.error(  user="u-003", role="user",       action="delete_recipe",  description="Insufficient permission")
logger.debug(  user="u-004", role="analyst",    action="search_recipe",  description="Query 'tacos'")

```

> **Handlers intercambiables:** puedes quitar/poner destinos sin tocar la lógica de negocio—esa es la esencia de **Observer**.

