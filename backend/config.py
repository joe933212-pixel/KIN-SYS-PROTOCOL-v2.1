import os

# Flask configuration
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'

# Database configuration
class DatabaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# JWT settings
class JWTConfig:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'your_jwt_secret'
    JWT_ACCESS_TOKEN_EXPIRES = 3600  # seconds

# Polygon settings
class PolygonConfig:
    POLYGON_API_KEY = os.environ.get('POLYGON_API_KEY')  # Your Polygon API Key
    POLYGON_API_URL = 'https://api.polygon.io'
