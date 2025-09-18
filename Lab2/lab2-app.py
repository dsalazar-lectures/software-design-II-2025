from flask import Flask, request

app = Flask(__name__)

# 1. GET al root
@app.route("/", methods=["GET"])
def home():
    h1 = "<h1>Welcome!</h1>"
    h2 = "<h2>This is the home page.</h2>"
    return f"{h1}{h2}"

# 2. POST al root (leer JSON)
@app.route("/", methods=["POST"])
def receive_name():
    data = request.get_json()
    if not data or "name" not in data:
        return "Missing 'name' in request", 400
    h1 = "<h1>Received!</h1>"
    h2 = f"<h2>Your name is: {data['name']}</h2>"
    return f"{h1}{h2}"

# 3. Valor en la URL
@app.route("/petName/<pet>")
def pet_name(pet):
    return f"<h1>Your pet name is {pet}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
