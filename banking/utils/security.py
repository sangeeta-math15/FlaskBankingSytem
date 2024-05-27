from flask_jwt_extended import verify_jwt_in_request, get_jwt_claims
from functools import wraps


def role_required(role):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_claims()
            if claims['role'] != role:
                return {"msg": "Access denied"}, 403
            return fn(*args, **kwargs)

        return decorator

    return wrapper
