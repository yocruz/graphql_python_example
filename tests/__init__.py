import os
import pytest
from web_app import init_app, DB


@pytest.fixture
def app_client():
    app = init_app('web_app.config.config_test')
    with app.test_client() as client:
        with app.app_context():
            DB.create_all()
        yield client
    return app
