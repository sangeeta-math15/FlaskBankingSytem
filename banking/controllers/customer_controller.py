from bson import ObjectId
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from banking.models.transaction_model import Transaction

customer_bp = Blueprint('customer', __name__)

@customer_bp.route('/deposit', methods=['POST'])
@jwt_required()
def deposit():
    data = request.get_json()
    if 'amount' not in data:
        return jsonify({"error_msg": "Amount is Required"}), 400
    amount = data.get('amount')
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError
    except (ValueError, TypeError):
        return jsonify({"error_msg": "Invalid amount. Amount must be a positive number"}), 400

    user_identity = get_jwt_identity()
    Transaction.create_transaction(user_identity['username'], amount, 'deposit')
    return jsonify({"msg": "Deposit successful"}), 200


@customer_bp.route('/withdraw', methods=['POST'])
@jwt_required()
def withdraw():
    data = request.get_json()
    amount = data.get('amount')
    user_identity = get_jwt_identity()
    try:
        amt = int(amount)
    except ValueError:
        return jsonify({"msg": "Invalid amount"}), 400
    transactions = Transaction.get_transactions(user_identity['username'])
    bal = sum(float(t['amount']) for t in transactions if 'amount' in t)
    if bal < amt:
        return jsonify({"msg": "Insufficient balance"}), 400
    Transaction.create_transaction(user_identity['username'], -amt, 'withdraw')
    return jsonify({"msg": "Withdrawal successful"}), 200


@customer_bp.route('/balance', methods=['GET'])
@jwt_required()
def balance():
    user_identity = get_jwt_identity()
    transactions = Transaction.get_transactions(user_identity['username'])
    bal = 0
    for t in transactions:
        bal += float(t['amount'])

    return jsonify(balance=bal), 200


def convert_obj_ids(transaction):
    for key, value in transaction.items():
        if isinstance(value, ObjectId):
            transaction[key] = str(value)
        elif isinstance(value, list):
            for item in value:
                convert_obj_ids(item)
    return transaction


@customer_bp.route('/history', methods=['GET'])
@jwt_required()
def history():
    user_identity = get_jwt_identity()
    transactions = Transaction.get_transactions(user_identity['username'])
    transactions = [convert_obj_ids(transaction) for transaction in transactions]
    return jsonify(transactions=transactions), 200
