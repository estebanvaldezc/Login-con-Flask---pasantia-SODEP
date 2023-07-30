# File: app.py (Presentation Layer)

from flask import Flask, request, jsonify
from logica import auntenticacion

app = Flask(__name__)

# API endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"Aviso": "Usuario y contrasenha son requeridos."}), 400

    authenticated = auntenticacion(username, password)

    if authenticated:
        return jsonify({"Aviso": "Ingreso exitoso."}), 200
    else:
        return jsonify({"Aviso": "Credenciales Invalidas."}), 401

if __name__ == '__main__':
    app.run(debug=True)

