import os


class Config:

    SECRET_KEY = os.getenv('SECRET_KEY', 'default_flask_secret_key')
    MONGO_URI = os.getenv('MONGO_URI')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_jwt_secret_key')

