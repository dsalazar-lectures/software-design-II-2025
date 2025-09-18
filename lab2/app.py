from flask import Flask
from flask import request

app = Flask(__name__)

# 1. GET to root path
@app.route("/", methods=["GET"])
def home():
    return "Test completed (c27796)"

# 2. POST to root path "/"
@app.route("/", methods=["POST"])
def postRootPath():
    data = request.get_json()
    name = data.get("name", "Unknown")
    return f"Name received: {name}"

# 3. GET value from URL
@app.route("/petName/<string:petName>", methods=["GET"])
def pet(petName):
    return f"Pet name found: {petName}"

if __name__ == "__main__":
    app.run(debug=True)
