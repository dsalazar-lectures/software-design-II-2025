# Laboratorio 2: Desarrollo de una mini app
# Estudiante: Amber Villarreal Campos, C28481
from flask import Flask, request, render_template

app = Flask(__name__)

# 1.GET en root path: Datos en URL, leer datos
@app.route('/', methods=['GET'])
def hello():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!: GET test accomplished"

# 2.POST en root path: Datos ocultos (como en un JSON), enviar datos
@app.route('/', methods=['POST'])
def handle_post():
    if request.is_json:
        data = request.get_json()
        name = data.get('name', 'Unknown')
        # print(f"Flask: Received name {name} by json")
        return f"Received name {name}"
    
    name = request.form.get('name', 'Unknown')
    # print(f"Flask: Received name {name} by form")
    return f"Received name {name}"

# 3. Mensaje con valor en la URL
@app.route('/supermarket/<ingredient>', methods=['GET'])
def ask_supermarket_url(ingredient):
    return f"Guest asking for {ingredient}"

# EXTRA: Mensaje por string
@app.route('/supermarket', methods=['GET'])
def ask_supermarket_string():
    ingredient = request.args.get('ingredient', 'Unknown')
    return f"Guest asking for {ingredient}"

if __name__ == '__main__':
    app.run(debug=True)