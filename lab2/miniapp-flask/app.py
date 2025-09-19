from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/")
def root_get():
    return jsonify({"message": "Mini app is running"}), 200

@app.post("/")
def root_post():
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    data = request.get_json(silent=True) or {}
    animal = data.get("animal")
    if not animal:
        return jsonify({"error": "Missing 'animal' in request body"}), 400
    return jsonify({"message": f"Your animal is {animal}"}), 200

@app.get("/craving/<food>")
def craving(food: str):
    return jsonify({"food": food, "message": f"Craving for {food}"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
