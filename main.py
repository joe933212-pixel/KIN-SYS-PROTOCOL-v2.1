from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from backend.routes import api
app.register_blueprint(api)

if __name__ == '__main__':
    app.run(debug=False)