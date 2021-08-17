import pytest
from tests import app_client
from sqlalchemy.exc import IntegrityError
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
            new_user = repo.create(user_data)
            assert new_user.id == 1

    def test_add_user_missing_fields(self, app_client):
        with app_client.application.app_context():
            repo = UserRepo()
            user_data = {
                'username': 'test_user',
            }
            try:
                new_user = repo.create(user_data)
                assert new_user.id == 1
            except IntegrityError as err:
                assert True
            else:
                assert False, "The integrity error wasn't throw"
