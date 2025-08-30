from flask import Blueprint

band_bp = Blueprint('band_bp', __name__)

@app.route('/bands', methods=['GET'])

@app.route('/bands/<int:band_id>', methods=['GET'])

@app.route('/bands', methods=['POST'])

@app.route('/bands/<int:band_id>', methods=['PUT'])

@app.route('/bands/<int:band_id>', methods=['DELETE'])