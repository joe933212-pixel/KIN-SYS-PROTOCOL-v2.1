from flask import jsonify

def register_routes(app):
    @app.route('/api/health', methods=['GET'])
    def health():
        return jsonify({'status': 'healthy'}), 200
    
    @app.route('/api/test', methods=['GET'])
    def test():
        return jsonify({'message': 'KIN-SYS PROTOCOL v2.1 is running'}), 200
    
    @app.route('/', methods=['GET'])
    def home():
        return jsonify({'message': 'KIN-SYS PROTOCOL v2.1'}), 200
