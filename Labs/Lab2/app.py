from flask import Flask
from flask import request

app = Flask(__name__)

@app.get("/")
def getTest():
    return "<p>Prueba Get Satisfactoria!!</p>"

@app.post("/")
def postTest():
    name = request.json.get("name")
    return f"<p>El nombre es: {name}</p>"

@app.get("/recipe/<int:recipe_id>")
def getRecipeFromID(recipe_id):
    return f"<p>El ID de la receta es: {recipe_id}</p>"