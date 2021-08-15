from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()
migrate = Migrate()

#hack so migrate detects the models
from .models import *


def register_blueprints(app: Flask):
    from .views.user_view import User

    app.add_url_rule('/users', view_func=User.as_view('users'))


def init_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    with app.app_context():
        DB.init_app(app)
        migrate.init_app(app, DB)
        register_blueprints(app)
        return app


