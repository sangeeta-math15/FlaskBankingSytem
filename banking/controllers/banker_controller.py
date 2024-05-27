from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from banking.controllers.customer_controller import convert_obj_ids
from banking.models.user_model import mongo_conn
banker_bp = Blueprint('banker', __name__)


@banker_bp.route('/accounts', methods=['GET'])
@jwt_required()
def accounts():
    user_identity = get_jwt_identity()

    if user_identity['role'] != 'banker':
        return jsonify({"msg": "Access denied"}), 403

    users = mongo_conn.db.users.find()
    user_acc = [convert_obj_ids(user) for user in list(users)]

    return jsonify(users=user_acc), 200


@banker_bp.route('/transactions', methods=['GET'])
@jwt_required()
def transactions():
    user_identity = get_jwt_identity()

    if user_identity['role'] != 'banker':
        return jsonify({"msg": "Access denied"}), 403

    transaction = mongo_conn.db.transactions.find()
    banker_transactions = [convert_obj_ids(transaction) for transaction in list(transaction)]
    return jsonify(transactions=banker_transactions), 200
