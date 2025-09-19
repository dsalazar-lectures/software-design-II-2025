from flask import Flask, request

app = Flask(__name__)

# GET
@app.route("/", methods=["GET"])
def home():
    h1 = "<h1>Welcome to my page</h1>"
    h2 = "<h2>Connection successful</h2>"
    h3 = "<h2>Get test successful</h2>"
    return f"{h1}{h2}{h3}"

# POST
@app.route("/", methods=["POST"])
def receive_name():
    data = request.get_json()
    if not data or "name" not in data:
        return "Missing 'name' in request", 400
    h1 = "<h1>Request received</h1>"
    h2 = f"<h2>Your name is: {data['name']}</h2>"
    return f"{h1}{h2}"

# Dynamic URL
@app.route("/favoriteFood/<food>")
def favorite_food(food):
    return f"<h1>Your favorite food is: {food}</h1>"

if __name__ == "__main__":
    app.run(debug=True)