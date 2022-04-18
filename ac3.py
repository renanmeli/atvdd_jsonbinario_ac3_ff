import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/binario')
def index2():
    return render_template('binario.html')

@app.route('/json')
def index5():
    return render_template('json.html')

@app.route('/api/binario', methods=['POST'])
def say_name2():
    nome = request.form['nome']
    email = request.form['email']
    print(nome)
    print(email)
    return jsonify(nome=nome, email=email)

@app.route('/api/json', methods=['POST'])
def say_name5():

    json = request.get_json()
    nome = json['nome']
    email = json['email']
    return jsonify(nome=nome, email=email)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True)

