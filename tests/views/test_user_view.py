import pytest
from tests import app_client
from web_app import DB
from web_app.models.user import User


def setup_users(app_client):
    with app_client.application.app_context():
        user = User()
        user.username = 'user1'
        user.email = 'a@a.com'
        user.gender = 'U'
        DB.session.add(user)
        DB.session.commit()




def test_user_get(app_client):
    setup_users(app_client)
    rv = app_client.get('/users')
    assert {'users': [{'id': 1, 'username': 'user1', 'email': 'a@a.com', 'gender': 'U', 'posts': []}]} == rv.json
