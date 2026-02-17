from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import loginManager
from config import config


db = SQLAlchemy()
login_Manager = loginManager()
login_Manager.login_view = "auth.login"


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    login_Manager.init_app(app)

    from .routes import main
    from .auth import auth

    app.register_blueprint(main)
    app.register_blueprint(auth)
    return app