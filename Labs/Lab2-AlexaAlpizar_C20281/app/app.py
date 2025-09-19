LAB2 - Alexa Alpizar Mora - C20282


from flask import Flask, request, jsonify

app = Flask(__name__)

# 1. GET en root
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Prueba de GET satisfactoria!"})

# 2. POST en root: recibe JSON o form-data con "name"
@app.route("/", methods=["POST"])
def post_name():
    name = None

    # Si viene JSON
    if request.is_json:
        data = request.get_json()
        name = data.get("name")

    # Si viene form-data
    if not name:
        name = request.form.get("name")

    if not name:
        return jsonify({"error": "No name provided"}), 400

    return jsonify({"message": f"Received name: {name}"})

# 3. GET con parámetro en la URL
@app.route("/petName/<string:name>", methods=["GET"])
def get_pet_name(name):
    return jsonify({"message": f"Your pet name is {name.capitalize()}!"})


if __name__ == "__main__":
    app.run(debug=True)
