# Design Pattern - Proxy

## Definición y tipo

* Proxy es un objeto “representante” que implementa la misma interfaz que un objeto real y controla el acceso a él.

* Pertenece a los patrones estructurales (GoF).

## Problema común que resuelve

* Control de acceso sin modificar el objeto real.

* Carga diferida (lazy) para evitar costos de inicialización hasta que sea necesario.

* Caché transparente para evitar trabajo repetido y reducir latencia.

* Resiliencia: aplicar timeouts, reintentos y registro de errores alrededor de recursos remotos.

* Gobernanza: límites de uso (rate-limit), auditoría y métricas centralizadas.

## ¿Cómo mejora el mantenimiento y la escalabilidad?

* Desacopla políticas transversales (seguridad, caché, límites) del código de negocio → clases más simples y testeables.

* Sustitución transparente: el cliente programa contra una interfaz, y en despliegue se elige real o proxy por configuración.

* Evolución segura: cambiar políticas (TTL, retries, permisos) no requiere tocar a los clientes ni al objeto real.

* Escalabilidad operativa: cacheo y rate-limit reducen carga en servicios y bases de datos, mejorando throughput y costos.

### Ventajas

* Control centralizado del acceso y del ciclo de vida del objeto real.

* Mejor rendimiento percibido con lazy y caché.

* Observabilidad: fácil añadir logging/métricas sin invadir la lógica de negocio.

* Testabilidad: permite inyectar reemplazos (real, proxy, fakes) manteniendo la misma interfaz.

### Desventajas

* Mayor complejidad e indirección (más clases y saltos de llamada).

* Riesgo de “Dios Proxy” si acumula demasiadas responsabilidades (auth + caché + rate-limit + métricas).

* Depuración más difícil si no hay buena trazabilidad (¿falló el real, la red o la política del proxy?).

* Caché peligrosa si se configuran mal TTL/invalidaciones (datos obsoletos o inconsistentes).