import re
from datetime import datetime

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Teacher and classmates!"

@app.route("/", methods=["POST"])
def receive_name():
    data = request.get_json()

    name = data.get("name", "Desconocido")

    return f"Received name: {name}"

@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    
    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route("/petName/<pet_name>")
def show_pet_name(pet_name):
    return f"Your pet name is {pet_name}!"