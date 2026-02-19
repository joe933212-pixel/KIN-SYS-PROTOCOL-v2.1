import os
from flask import Flask
from flask_cors import CORS

# Create Flask application
app = Flask(__name__)

# Set up CORS
CORS(app)

# Import routes and register them (assuming there is a routes file)
from routes import register_routes
register_routes(app)

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 5000))