# Importar la clase Flask y la función request del módulo flask
from flask import Flask, request

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Define la ruta para la solicitud GET al root path (/)
@app.route("/", methods=["GET"])
def get_hello():
    return "¡Prueba de GET satisfactoria!"

# Define la ruta para la solicitud POST al root path (/)
@app.route("/", methods=["POST"])
def post_name():
    # Usa request.get_json() para obtener los datos enviados en formato JSON
    data = request.get_json()
    if data and "name" in data:
        # Extrae el valor del campo 'name' del JSON
        name = data["name"]
        return f"Received name: {name}"
    else:
        # Retorna un error si el JSON es inválido o no contiene el campo 'name'
        return "Error: No se encontró el campo 'name' en el JSON.", 400

# Define la ruta para la solicitud GET con un parámetro de URL
@app.route("/petName/<pet_name>", methods=["GET"])
def get_pet_name(pet_name):
    return f"Your pet name is {pet_name}!"

if __name__ == "__main__":
    # app.run() inicia el servidor de desarrollo
    # debug=True activa el modo de depuración
    app.run(debug=True)
