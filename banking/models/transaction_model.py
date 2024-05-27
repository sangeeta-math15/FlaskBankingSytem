from flask import current_app
import datetime
from .user_model import mongo_conn

class Transaction:
    @staticmethod
    def create_transaction(user_id, amount, transaction_type):
        transaction_id = mongo_conn.db.transactions.insert_one({
            'user_id': user_id,
            'amount': amount,
            'transaction_type': transaction_type,
            'timestamp': datetime.datetime.utcnow()
        }).inserted_id
        return str(transaction_id)

    @staticmethod
    def get_transactions(user_id):
        transactions = mongo_conn.db.transactions.find({'user_id': user_id})
        return list(transactions)
