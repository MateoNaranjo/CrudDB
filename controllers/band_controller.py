from flask import Blueprint

band_bp = Blueprint('band_bp', __name__)

@app.route('/bands', methods=['GET'])
    print("hola")

@app.route('/bands/<int:band_id>', methods=['GET'])
    print("hola")

@app.route('/bands', methods=['POST'])
    print("hola")

@app.route('/bands/<int:band_id>', methods=['PUT'])
    print("hola")

@app.route('/bands/<int:band_id>', methods=['DELETE'])
    print("hola")