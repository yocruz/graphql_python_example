from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def register_blueprints(app: Flask):
    pass


def init_db(flask: Flask):
    db = SQLAlchemy(flask)
    return db


def init_app():
    app = Flask(__name__)
    return app


