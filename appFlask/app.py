from flask import Flask, request, jsonify

app = Flask(__name__)

# GET /
@app.route("/", methods=["GET"])
def root():
    return jsonify({"message": "Hola CI-0136 – Lab 2 (GET /)"}), 200

# POST /
@app.route("/", methods=["POST"])
def echo_name():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not name:
        return jsonify({"error": "El campo 'name' es requerido"}), 400
    return jsonify({"message": f"Hola, {name}! (POST /)"}), 200

# GET /petName/<pet_name>
@app.route("/petName/<pet_name>", methods=["GET"])
def pet_name(pet_name):
    return jsonify({"message": f"Tu mascota se llama {pet_name}"}), 200

if __name__ == "__main__":
    # También puedes correr así: python app.py
    app.run(debug=True)
