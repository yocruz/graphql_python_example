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

    def test_remove_user(self, app_client):
        with app_client.application.app_context():
            repo = UserRepo()
            user_data = {
                'username': 'test_user',
                'email': 'a@a.com',
                'gender': 'M'
            }
            new_user = repo.create(user_data)
            assert new_user.id == 1

            repo.delete(new_user.id)

            is_deleted = repo.get(new_user.id)
            assert is_deleted is None

    def test_update_user(self, app_client):
        with app_client.application.app_context():
            repo = UserRepo()
            user_data = {
                'username': 'test_user',
                'email': 'a@a.com',
                'gender': 'M'
            }
            new_user = repo.create(user_data)
            assert new_user.id == 1

            result = repo.update(new_user.id, email='b@b.com')
            assert result.email == 'b@b.com', 'The email address was not updated'

    def test_update_non_existing_user(self, app_client):
        with app_client.application.app_context():
            repo = UserRepo()
            try:
                repo.update(100, email='mao@meo.com')
            except Exception as err:
                assert True
            else:
                assert False, 'An exception in not thrown when updating a non existing user'
