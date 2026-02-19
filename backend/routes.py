from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

@api.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

@api.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'KIN-SYS PROTOCOL v2.1'}), 200