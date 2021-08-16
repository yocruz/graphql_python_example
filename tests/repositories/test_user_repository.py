import pytest
from tests import app_client
from web_app.repositories.user_repo import UserRepo


class TestUserRepository():

    def test_add_user(self, app_client):
        with app_client.application.app_context():
            repo = UserRepo()
            user_data = {
                'username': 'test_user',
                'email': 'a@a.com',
                'gender': 'M'
            }

            new_user = repo.add(user_data)
            assert new_user.id == 1
