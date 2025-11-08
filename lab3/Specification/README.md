# Patrón de Diseño Specification

## Índice
1. [¿Qué es el patrón Specification?](#qué-es-el-patrón-specification)
2. [Estructura del Patrón](#estructura-del-patrón)
3. [Ventajas](#ventajas)
4. [Desventajas](#desventajas)
5. [Usos Más Comunes](#usos-más-comunes)
6. [Usos Menos Comunes](#usos-menos-comunes)
7. [Aprovechamiento del Patrón](#aprovechamiento-del-patrón)
8. [Aplicaciones Prácticas](#aplicaciones-prácticas)
9. [Ejemplos en Compañías Grandes](#ejemplos-en-compañías-grandes)
10. [Ejemplos de Código](#ejemplos-de-código)

---

## ¿Qué es el patrón Specification?

El **patrón Specification** es un patrón de diseño empresarial introducido por Eric Evans y Martin Fowler en el contexto de Domain-Driven Design (DDD). Su propósito principal es **encapsular reglas de negocio en objetos reutilizables y combinables** que pueden ser evaluados contra candidatos para determinar si cumplen ciertos criterios.

### Concepto Central

En lugar de dispersar la lógica de validación y filtrado a través de la aplicación, el patrón Specification permite:
- Centralizar reglas de negocio en objetos específicos
- Combinar especificaciones mediante operadores lógicos (AND, OR, NOT)
- Reutilizar lógica de negocio en diferentes contextos
- Facilitar el testing de reglas de negocio de forma aislada

### Problema que Resuelve

**Antes del patrón:**
```python
def find_premium_customers(customers):
    results = []
    for customer in customers:
        if customer.total_purchases > 10000 and customer.years_active > 2 and customer.status == "active":
            results.append(customer)
    return results
```

**Con el patrón:**
```python
premium_spec = PremiumPurchaseSpec().and_(LongTermCustomerSpec()).and_(ActiveCustomerSpec())
premium_customers = [c for c in customers if premium_spec.is_satisfied_by(c)]
```

---

## Estructura del Patrón

### Componentes Principales

```
┌─────────────────────────┐
│  <<interface>>          │
│   Specification<T>      │
├─────────────────────────┤
│ + is_satisfied_by(T)    │
│ + and_(Specification)   │
│ + or_(Specification)    │
│ + not_()                │
└─────────────────────────┘
           △
           │
           │ implements
    ┌──────┴──────┬──────────────────┬─────────────────┐
    │             │                  │                 │
┌───┴────┐  ┌────┴─────┐  ┌─────────┴────┐  ┌────────┴────────┐
│Concrete│  │   And    │  │     Or       │  │      Not        │
│  Spec  │  │   Spec   │  │    Spec      │  │     Spec        │
└────────┘  └──────────┘  └──────────────┘  └─────────────────┘
```

### Interfaz Base

```python
from abc import ABC, abstractmethod

class Specification(ABC):
    """Interfaz base para todas las especificaciones"""
    
    @abstractmethod
    def is_satisfied_by(self, candidate):
        """Verifica si el candidato cumple con la especificación"""
        pass
    
    def and_(self, other):
        """Combina con otra especificación usando AND lógico"""
        return AndSpecification(self, other)
    
    def or_(self, other):
        """Combina con otra especificación usando OR lógico"""
        return OrSpecification(self, other)
    
    def not_(self):
        """Niega la especificación actual"""
        return NotSpecification(self)
```

---

## Ventajas

### 1. **Separación de Responsabilidades**
- Las reglas de negocio están aisladas en clases específicas
- Facilita el principio de Responsabilidad Única (SRP)
- El código del dominio se mantiene limpio y enfocado

### 2. **Reutilización de Código**
- Las especificaciones pueden usarse en múltiples contextos
- No hay duplicación de lógica de validación
- Reduce el acoplamiento entre componentes

### 3. **Composición Flexible**
- Permite construir reglas complejas mediante combinación
- Operadores lógicos (AND, OR, NOT) facilitan la expresividad
- Nuevas combinaciones sin modificar código existente

### 4. **Testabilidad**
- Cada especificación puede probarse de forma aislada
- Tests más pequeños y enfocados
- Facilita el TDD (Test-Driven Development)

### 5. **Expresividad del Código**
- El código se lee como lenguaje natural
- Intención clara y explícita
- Reduce la complejidad cognitiva

### 6. **Mantenibilidad**
- Cambios en reglas de negocio localizados
- Fácil de extender sin modificar código existente (OCP)
- Versionamiento de reglas más sencillo

### 7. **Domain-Driven Design**
- Alinea perfectamente con DDD
- El lenguaje ubicuo se refleja en el código
- Expertos del dominio pueden entender las especificaciones

---

## Desventajas

### 1. **Complejidad Inicial**
- Requiere crear múltiples clases para reglas simples
- Curva de aprendizaje para equipos nuevos
- Puede parecer sobre-ingeniería en proyectos pequeños

### 2. **Proliferación de Clases**
- Incrementa el número de archivos en el proyecto
- Puede ser abrumador en proyectos con muchas reglas
- Requiere una buena organización del código

### 3. **Rendimiento**
- Múltiples llamadas a métodos para evaluaciones complejas
- Overhead de objetos en comparación con código inline
- Puede impactar en operaciones críticas de performance

### 4. **Dificultad con ORMs**
- No todas las especificaciones pueden traducirse a SQL
- Puede forzar evaluación en memoria vs. en base de datos
- Requiere patrones adicionales para queries eficientes

### 5. **Sobre-abstracción**
- Riesgo de crear especificaciones innecesarias
- Puede dificultar el debugging si se abusa
- Balance difícil entre flexibilidad y simplicidad

### 6. **Dependencias entre Especificaciones**
- Algunas especificaciones pueden depender de otras
- Gestión de dependencias puede complicarse
- Riesgo de crear jerarquías profundas

---

## Usos Más Comunes

1. **Validación de Entidades de Dominio** - Verificar que objetos cumplan reglas de negocio
2. **Filtrado de Colecciones** - Seleccionar elementos que cumplan ciertos criterios
3. **Reglas de Negocio Complejas** - Combinar múltiples condiciones de forma declarativa
4. **Construcción de Queries Dinámicas** - Búsquedas avanzadas con filtros combinables
5. **Control de Acceso y Autorización** - Determinar permisos de usuarios
6. **Validación de Formularios y DTOs** - Verificar datos de entrada
7. **Procesamiento de Eventos** - Decidir qué eventos procesar según criterios

---

## Usos Menos Comunes

1. **Machine Learning** - Selección de características relevantes para modelos
2. **Optimización de Recursos** - Decisiones sobre caché, memoria, etc.
3. **Testing y QA** - Determinar qué tests ejecutar según cambios
4. **Circuit Breaker y Resilience** - Evaluar salud de servicios
5. **Data Pipeline y ETL** - Validación de calidad de datos
6. **Gaming - AI Behavior** - Decisiones de comportamiento de NPCs
7. **Blockchain** - Validación de transacciones y smart contracts

---

## Aprovechamiento del Patrón

### Cuándo Usar el Patrón Specification

**SÍ usar cuando:**
- Tienes reglas de negocio complejas que cambian frecuentemente
- Necesitas combinar criterios de diferentes maneras
- El mismo criterio se usa en múltiples lugares
- Trabajas con Domain-Driven Design
- Necesitas expresar reglas de negocio de forma declarativa
- Quieres testing granular de reglas de negocio

**NO usar cuando:**
- Las reglas son extremadamente simples y estables
- El proyecto es muy pequeño o prototipo
- El rendimiento es crítico y cada milisegundo cuenta
- El equipo no está familiarizado y no hay tiempo para aprender
- Las reglas están fuertemente acopladas a la persistencia

### Mejores Prácticas

#### 1. **Nombrado Descriptivo**
Las especificaciones deben tener nombres que expresen claramente su intención.

#### 2. **Especificaciones Inmutables**
Una vez creadas, las especificaciones no deben modificar su estado interno.

#### 3. **Composición sobre Herencia**
Preferir combinar especificaciones con operadores lógicos en lugar de herencia compleja.

#### 4. **Factory Methods**
Usar factories para especificaciones comunes y reutilizables.

#### 5. **Integración con Repositorios**
Los repositorios deben aceptar especificaciones para filtrar entidades.

---

## Aplicaciones Prácticas

### 1. **E-Commerce**
- Búsqueda y filtrado de productos con múltiples criterios
- Determinación de elegibilidad para promociones y descuentos
- Recomendaciones personalizadas de productos

### 2. **Finanzas y Banking**
- Aprobación automática de préstamos basada en criterios
- Detección de transacciones fraudulentas
- Cumplimiento de regulaciones (KYC, AML)

### 3. **Healthcare (Salud)**
- Elegibilidad de pacientes para ensayos clínicos
- Asignación de tratamientos según condiciones
- Validación de recetas y medicamentos

### 4. **Recursos Humanos**
- Match de candidatos con posiciones vacantes
- Evaluación de desempeño según criterios
- Determinación de beneficios y compensaciones

### 5. **Logística y Supply Chain**
- Optimización de rutas de entrega
- Selección de proveedores
- Gestión de inventario

### 6. **SaaS y Cloud Computing**
- Rate limiting y throttling de APIs
- Asignación de recursos según tier de usuario
- Políticas de backup y retención de datos

---

## Ejemplos en Compañías Grandes

### 1. **Amazon**
- **Prime Eligibility**: Determinar productos elegibles para envío Prime
- **Recomendaciones**: Sugerir productos basados en historial y preferencias
- **Dynamic Pricing**: Ajustar precios según demanda, competencia y stock

### 2. **Netflix**
- **Content Recommendation**: Seleccionar contenido relevante por usuario
- **Auto-play**: Decidir si reproducir siguiente episodio automáticamente
- **Quality Adaptation**: Ajustar calidad de streaming según conexión

### 3. **Uber**
- **Driver-Rider Matching**: Emparejar conductores con pasajeros óptimamente
- **Surge Pricing**: Aplicar precios dinámicos según oferta/demanda
- **Safety Features**: Validar seguridad de viajes y conductores

### 4. **Airbnb**
- **Listing Quality**: Evaluar calidad de propiedades para rankings
- **Instant Book**: Determinar elegibilidad para reserva instantánea
- **Pricing Suggestions**: Recomendar precios basados en múltiples factores

### 5. **Spotify**
- **Playlist Curation**: Seleccionar canciones para playlists automáticas
- **Discover Weekly**: Generar recomendaciones personalizadas semanales
- **Ad Targeting**: Mostrar anuncios relevantes a usuarios gratuitos

### 6. **LinkedIn**
- **Job Recommendations**: Sugerir empleos según perfil y experiencia
- **Connection Suggestions**: Recomendar contactos profesionales
- **Content Feed**: Filtrar publicaciones relevantes para cada usuario

### 7. **Google Ads**
- **Ad Targeting**: Mostrar anuncios a audiencias específicas
- **Quality Score**: Evaluar calidad de anuncios y landing pages
- **Bid Optimization**: Ajustar pujas según probabilidad de conversión

---