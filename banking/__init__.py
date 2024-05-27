from flask import Flask
from flask_jwt_extended import JWTManager

jwt = JWTManager()
from banking.controllers.auth_controller import auth_bp
from banking.controllers.banker_controller import banker_bp
from banking.controllers.customer_controller import customer_bp
import config


def create_app():
    app = Flask(__name__)

    app.config.from_object(config.Config)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(banker_bp)

    return app


