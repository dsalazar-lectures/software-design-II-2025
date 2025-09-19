from flask import Flask
from flask import request

app = Flask(__name__)

@app.get("/")
def getTest():
    return "<p>¡Prueba de GET satisfactoria!</p>"

@app.post("/")
def postTest():
    name = request.json.get("name")
    return f"<p>Received name: {name}</p>"

@app.get("/recipe/<string:recipe_name>")
def getRecipeFromID(recipe_name):
    return f"<p>La receta seleccionada es: {recipe_name}</p>"

if __name__ == '__main__':
   app.run()