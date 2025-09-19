# Lab 2 - Mini Flask App

This is a small Flask application built as part of Lab 2.
It demonstrates the use of **HTTP GET and POST requests** with and without parameters.

##  How to run the app

1. Make sure you have **Python 3** installed.
2. Install Flask if you don’t have it yet:

```bash
pip install flask
```

3. Save the file as `miniApp.py` and run it:

```bash
python miniApp.py
```

4. The app will run locally at:

```
http://127.0.0.1:5000/
```

---

## Endpoints

### 1. GET `/`

Returns a simple greeting message.
Example Response:

```
Hello! This is the Mini App for Lab 2
```

---

### 2. POST `/`

Consumes JSON data containing a `name`.
Example Request:

```json
{
  "name": "Camila"
}
```

Example Response:

```
Hello Camila! I received your message correctly
```

---

### 3. GET `/petName/<paramName>`

Returns a message including the parameter from the URL.
Example Request:

```
http://127.0.0.1:5000/petName/Gaia
```

Example Response:

```
Hello Gaia! You are a very special pet
```

---

### Documentation 

[Flask Quickstart](https://flask.palletsprojects.com/en/3.0.x/quickstart/#routing)

---

### Author
Camila Rodríguez - C36624