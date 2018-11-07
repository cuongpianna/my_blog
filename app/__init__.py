from flask import Flask
from flask_cors import CORS

from config import config
from app.helpers.extensions import db


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    register_extensions(app)
    from app.post import bp as post_blueprint
    app.register_blueprint(post_blueprint)
    return app


def register_extensions(app):
    db.init_app(app)
    CORS(app)
