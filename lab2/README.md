# Flask - Mini App

Esta es una pequeña aplicación desarrollada con Flask, que muestra el manejo de diferentes métodos HTTP (`GET` y `POST`) y el uso de parámetros en la URL.

## Requisitos

- **Python 3**
- **Flask** 

### Instalación de dependencias

```bash
pip install flask
```

## Ejecución del servidor

1. Ejecute el archivo de la app:

   ```bash
   python3 app.py
   ```
2. Por defecto se ejecutará en:

   ```
   http://127.0.0.1:5000/
   ```

---

## HTTP requests (sin interfáz gráfica)

### 1️. GET al root path `/`

Verifica que el servidor responda correctamente.

**Request:**

```
GET /
```

**Response:**

```
GET test was succesful!
```

---

### 2️. POST al root path `/`

Recibe un JSON que en el body del request incluye un campo `name`.

**Request (JSON):**

```json
{
  "name": "Paula"
}
```

**Response:**

```
Received name: Paula
```

Si no se envía el campo `name`, la respuesta será:

```
'name' field not found in JSON
```

---

### 3️. GET con parámetro en URL

Recibe un parámetro en la URL que representa el nombre de una mascota.

**Request:**

```
GET /petName/Coco
```

**Response:**

```
Your pet's name is Coco
```
