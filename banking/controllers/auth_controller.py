from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from banking.models.user_model import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
def home():
    return "Welcome To Banking System"


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.find_by_username(username)

    if user and User.check_password(user, password):
        access_token = create_access_token(identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    role = data.get('role', 'customer')

    if User.find_by_username(username):
        return jsonify({"msg": "Username already exists"}), 400

    user_id = User.create_user(username, password, role)
    return jsonify({"msg": "User created", "user_id": user_id}), 201
