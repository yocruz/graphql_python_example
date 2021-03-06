import os
import pytest
from flask.testing import FlaskClient
from web_app import init_app, DB
from web_app.repositories.user_repo import UserRepo


@pytest.fixture
def app_client() -> FlaskClient:
    app = init_app('web_app.config.config_test')
    with app.test_client() as client:
        with app.app_context():
            DB.create_all()
        yield client
    return app
