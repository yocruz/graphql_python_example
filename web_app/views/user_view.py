from flask import jsonify
from flask.views import MethodView
from web_app.repositories.user_repo import UserRepo


class User(MethodView):

    def __init__(self):
        super().__init__()
        self.repo = UserRepo()

    def get(self):
        users = self.repo.get()
        return jsonify(users=users)

    def post(self):
        return 'ok', 201
