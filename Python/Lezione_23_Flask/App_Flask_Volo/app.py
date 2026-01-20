from flask import Flask, jsonify, request
import data

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>Benvenuto in Voli!</h2>'

@app.route('/Nazioni', methods=['GET', 'POST'])
def get_nazioni():
    if request.method == 'GET':
        return jsonify(data.dati['Nazioni']), 200

    if request.method == 'POST':
        nuova = request.json
        if not nuova or 'id' not in nuova or 'nome' not in nuova:
            return jsonify({"error": "Dati mancanti"}), 400

        if nuova['id'] in data.dati['Nazioni']:
            return jsonify({"error": "Nazione già presente"}), 400

        data.dati['Nazioni'][nuova['id']] = nuova
        return jsonify(nuova), 201
    
@app.route('/Nazioni/<int:id>', methods= ['GET', 'PUT'])
def handler_nazione(id):
    if request.method == 'GET':
        return jsonify(data.dati['Nazioni'][id]), 200
    
    elif request.method == 'PUT':
        nuova = request.json
        if not nuova or 'id' not in nuova or 'nome' not in nuova:
            return jsonify({"error": "Dati mancanti"}), 400

        if nuova['id'] in data.dati['Nazioni']:
            return jsonify({"error": "Nazione già presente"}), 400

        data.dati['Nazioni'][nuova['id']] = nuova
        return jsonify(nuova), 201