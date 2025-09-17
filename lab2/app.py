from flask import Flask, request

app = Flask(__name__)

# 1. GET al root path /
@app.route("/", methods=["GET"])
def get_test():
    return "GET test was succesful!"

# 2. POST al root path /
@app.route("/", methods=["POST"])
def post_root():
    # espera un JSON en el body del request
    data = request.get_json()
    name = data.get("name")

    if not name:
        return "'name' field not found in JSON"
    return f"Received name: {name}"

# 3. GET con parámetro en URL
@app.route("/petName/<name>", methods=["GET"])
def pet_name(name):
    return f"Your pet's name is {name}"

if __name__ == "__main__":
    app.run(debug=True)