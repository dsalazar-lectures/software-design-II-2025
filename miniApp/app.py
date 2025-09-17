from flask import Flask, request

app = Flask(__name__)

@app.get("/")
def getTest():
    return "Prueba de GET satisfactoria!", 200

@app.post("/")
def received_name():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not name:
        return "No se recibe 'name' en JSON.", 400
    return f"Received name: {name}", 200

@app.get("/petName/<string:pet>")
def pet_name(pet: str):
    return f"Your pet name is {pet}!", 200

if __name__ == "__main__":
    app.run(debug=True)