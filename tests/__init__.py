import pytest
from web_app import init_app


@pytest.fixture
def setup_app():
    app = init_app('web_app.config.config_test')

    return app
