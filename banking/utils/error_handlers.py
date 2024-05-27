from flask import Blueprint, jsonify

error_bp = Blueprint('errors', __name__)

@error_bp.app_errorhandler(404)
def not_found_error(error):
    return jsonify({"msg": "Not found"}), 404

@error_bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({"msg": "Internal server error"}), 500
