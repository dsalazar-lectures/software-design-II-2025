from flask import Flask
from flask import request

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/', methods=['GET'])
def rootResponse():
    response = "GET del root"
    return response

@app.route('/', methods=['POST'])
def rootHello():
    nameResponse = request.json.get("name")
    response = f"Hola {nameResponse}"
    return response

@app.route('/timesTwo/<int:numInput>', methods=['GET'])
def timesTwo(numInput):
    numResponse = numInput * 2
    response = f"{numInput} * 2 = {numResponse}"
    return response

if __name__ == '__main__':
    app.run(debug=True)
