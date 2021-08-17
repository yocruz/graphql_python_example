from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


DB = SQLAlchemy()
migrate = Migrate()

# hack so migrate detects the models
from .models import *


def register_blueprints(app: Flask):
    from .views.user_view import User

    app.add_url_rule('/users', endpoint='users',
                     view_func=User.as_view('users'))
    app.add_url_rule('/users/<user_id>', endpoint='user',
                     view_func=User.as_view('users'))


def init_app(config_file='web_app.config.default'):
    app = Flask(__name__)
    app.config.from_object(config_file)
    with app.app_context():
        DB.init_app(app)
        migrate.init_app(app, DB)
        register_blueprints(app)
        return app
