import os
from flask import Flask
from .model import db
from dotenv import load_dotenv

__all__ = ['create_app']


def create_app(config=None):
    load_dotenv()   
    app = Flask(__name__)
    # initialize_extensions(app)
    initialize_blueprints(app)
    initialize_configuration(app)
    return app


# def initialize_extensions(app):
#     db.init_app(app)


def initialize_blueprints(app):

    from .main import main

    for bp in [main]:
        app.register_blueprint(bp)

def initialize_configuration(app):
    import json

    with open('config.json', 'r') as f:
        config = json.load(f)

    env = os.getenv('ENV_TYPE')

    if env == 'dev':
        app.config = config['DEVELOPMENT']
    elif env == 'test':
        app.config = config['TEST']
    elif env == 'prod':
        app.config = config['PRODUCTION']
    else:
        raise ValueError('Invalid environment name')
