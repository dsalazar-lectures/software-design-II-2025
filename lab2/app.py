from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    animalUser = data.get('animal')
    return render_template('index.html', animal=animalUser)

@app.route('/craving/<food>', methods=['GET'])
def get_url(food):
    return render_template('index.html', food=food)

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
