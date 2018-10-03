from flask import Flask
from flask_dotenv import DotEnv
from .model import db

__all__ = ['create_app']


def create_app():
    app = Flask(__name__)
    initialize_extensions(app)
    initialize_blueprints(app)
    return app


def initialize_extensions(app):
    env = DotEnv()

    db.init_app(app)
    env.init_app(app)


def initialize_blueprints(app):

    from .main import main

    for bp in [main]:
        app.register_blueprint(bp)
