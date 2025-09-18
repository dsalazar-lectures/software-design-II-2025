from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def test():
    return "Hola, Prueba de GET"

@app.route("/", methods=["POST"])
def ask_recipe():
    data = request.json
    name = data.get("name")
    if not name:
        return "Error, indique un nombre en el JSON"
    return f"Hola {name}, ¿cuál es su receta favorita?"

@app.route("/recipe/<specific_recipe>", methods=["GET"])
def favorite_recipe(specific_recipe):
    return f"Excelente elección, yo también quiero {specific_recipe}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)