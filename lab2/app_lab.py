from flask import Flask, request, jsonify 

app = Flask(__name__)

# 1. Un mensaje cualquiera para el GET al root path: / .
@app.route("/", methods=["GET"])
def get_from_root():
    return "C02517. GET test completed."

# 2. Un mensaje que consuma una propiedad del request de un POST al root path: / . En el
# siguiente ejemplo, se mandó el siguiente request y se muestra el siguiente mensaje:

@app.route("/", methods=["POST"])
def post_root():
    data = request.get_json()
    
    name = data["name"]
    return "C02517. Received name correctly: " + name

# 3. Un mensaje mostrando un valor que venga en el URL. Por ejemplo, crear un nuevo URL:
# http://127.0.0.1:5000/petName/Coco mostraría:

@app.route("/menu/<string:recipe_name>", methods=["GET"])
def recipe(recipe_name):
    return "C02517. Found recipe " + recipe_name + " :D"



if __name__ == "__main__":
    app.run(debug=True)