from flask import current_app
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
import config

mongo_conn = MongoClient(config.Config.MONGO_URI)


class User:
    @staticmethod
    def create_user(username, password, role='customer'):
        password_hash = generate_password_hash(password, method='pbkdf2:sha256')
        with current_app.app_context():
            user_id = mongo_conn.db.users.insert_one({
                'username': username,
                'password': password_hash,
                'role': role
            }).inserted_id
        return str(user_id)

    @staticmethod
    def find_by_username(username):
        user = mongo_conn.db.users.find_one({'username': username})
        return user

    @staticmethod
    def check_password(user, password):
        return check_password_hash(user['password'], password)
