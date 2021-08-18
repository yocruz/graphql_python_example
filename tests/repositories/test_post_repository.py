import pytest
from flask.testing import FlaskClient
from tests import app_client

from web_app.models.user import User
from web_app.repositories.user_repo import UserRepo
from web_app.repositories.post_repo import PostRepo


class TestPostRepository():

    def create_app_user(self, app_client: FlaskClient) -> User:
        with app_client.application.app_context():
            repo = UserRepo()
            user_data = {
                'username': 'test_user',
                'email': 'a@a.com',
                'gender': 'M'
            }
            return repo.create(user_data)


    def test_create_user_post(self, app_client: FlaskClient):
        user = self.create_app_user(app_client)
        assert user.id == 1
        with app_client.application.app_context():
            repo = PostRepo()
            post_data = {
                'text': 'Lorem ipsum',
                'user': user
            }
            post = repo.create(post_data)
            assert post.id == 1
            assert post.text == 'Lorem ipsum'

    def test_delete_user_post(self, app_client: FlaskClient):
        user = self.create_app_user(app_client)
        assert user.id == 1
        with app_client.application.app_context():
            repo = PostRepo()
            post_data = {
                'text': 'Lorem ipsum',
                'user': user
            }
            post = repo.create(post_data)
            assert post.id == 1
            assert post.text == 'Lorem ipsum'

            user.reload()
            assert len(user.posts) == 1
            repo.delete(post.id)
            user.reload()
            assert len(user.posts) == 0

    def test_update_post(self, app_client: FlaskClient):
        user = self.create_app_user(app_client)
        assert user.id == 1
        with app_client.application.app_context():
            repo = PostRepo()
            post_data = {
                'text': 'Lorem ipsum',
                'user': user
            }
            post = repo.create(post_data)
            assert post.text == 'Lorem ipsum'
            res = repo.update(post.id, text='modified!')
            assert res.text == 'modified!'

