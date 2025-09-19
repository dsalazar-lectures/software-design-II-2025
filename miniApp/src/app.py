from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_root():
    return jsonify({
        "message": "Prueba del GET",
    })

@app.route('/', methods=['POST'])
def post_root():
    data = request.get_json()
    return jsonify({
        "message": f"name: {data['name']}"
    })

@app.route('/petName/<string:pet_name>', methods=['GET'])
def get_pet_name(pet_name):
    return jsonify({
        "message": f"Pet name: {pet_name}"
    })

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)