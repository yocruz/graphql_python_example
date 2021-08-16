import pytest
from tests import app_client


def test_user_get(app_client):
    rv = app_client.get('/users')
    assert {'users': []} == rv.json
