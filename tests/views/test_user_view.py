import pytest
from tests import app_client
from web_app import DB
from web_app.models.user import User

USERS = [
    {
        'username': 'user1',
        'email': 'u1@a.com',
        'gender': 'F',
    },
    {
        'username': 'user2',
        'email': 'u2@a.com',
        'gender': 'F',
    },
    {
        'username': 'user3',
        'email': 'u3@a.com',
        'gender': 'F',
    },
    {
        'username': 'user4',
        'email': 'u4@a.com',
        'gender': 'F',
    },
    {
        'username': 'user5',
        'email': 'u5@a.com',
        'gender': 'F',
    },
    {
        'username': 'user6',
        'email': 'u6@a.com',
        'gender': 'F',
    },

]


class TestUserView():

    def setup_users(self, app_client):
        with app_client.application.app_context():
            for u in USERS:
                user = User()
                user.username = u['username']
                user.email = u['email']
                user.gender = u['gender']
                DB.session.add(user)
            DB.session.commit()

    def test_get_all_users(self, app_client, mocker):
        def return_function(*args, **kwargs):
            return [User.from_json(u) for u in USERS]

        mocker.patch(
            'web_app.repositories.user_repo.UserRepo._get_all_users', return_function)
        rv = app_client.get('/users')
        users = rv.json['users']
        assert len(USERS) == len(users)

    def test_get_user_by_id(self, app_client, mocker):
        def get_single_user(*args, **kwargs):
            return User.from_json(USERS[0])

        mocker.patch(
            'web_app.repositories.user_repo.UserRepo._get_user_by_id', get_single_user)

        resp = app_client.get('/users?user_id=1')
        assert resp.json['user'] == USERS[0]

    def test_get_user_by_id(self, app_client, mocker):
        def get_single_user(*args, **kwargs):
            return None

        mocker.patch(
            'web_app.repositories.user_repo.UserRepo._get_user_by_id', get_single_user)

        resp = app_client.get('/users?user_id=100')
        assert resp.json == {'errors': 'User not found'}
        assert resp.status_code == 404

    def test_create_user_success(self, app_client, mocker):
        user = {
            'username': 'test_user',
            'email': 'a@a.com',
            'gender': 'M'
        }

        def add_user(*args, **kwargs):
            new_user = User.from_json(user)
            new_user.id = 1
            return new_user

        mocker.patch(
            'web_app.repositories.user_repo.UserRepo.add', add_user)

        resp = app_client.post('/users', json=user)
        assert resp.status_code == 201
        user = resp.json.get('user')
        assert user
        assert user['id'] == 1
        assert user['username'] == 'test_user'
