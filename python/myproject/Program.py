from flask import Flask, request, jsonify

app = Flask(__name__)

# Un mensaje cualquiera para el GET al root path: / .
@app.route("/", methods=["GET"])
def prueba_get():
    return "<p> Prueba de GET exitosa!</p>"

# Un mensaje que consuma una propiedad del request de un POST al root path: /
@app.route("/", methods=["POST"])
def root():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Falta la propiedad 'name'"}), 400
    
    name = data["name"]
    return jsonify(f"Nombre recibido: {name}")

# Un mensaje mostrando un valor que venga en el URL
@app.route("/petName/<pet>", methods=["GET"])
def pet_name(pet):
    return f"Tu mascota se llama {pet}"