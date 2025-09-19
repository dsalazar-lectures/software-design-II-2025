# Camila Rodríguez - C36624

from flask import Flask, request, jsonify

app = Flask(__name__)

# GET request 
@app.route('/', methods=['GET'])
def getRoot():
    return "Hello! This is the Mini App for Lab 2\n"

# POST request 
@app.route('/', methods=['POST'])
def postRoot():
    data = request.get_json()
    if data and 'name' in data:
        return f"Hello {data['name']}! I received your message correctly from Lab II\n"
    return "No valid name was received\n"

# GET request with a parameter in the URL
@app.route('/url/<paramName>')
def getParamName(paramName):
    return f"The URL has {paramName}!"

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
