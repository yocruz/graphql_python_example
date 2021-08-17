from flask import jsonify, request
from flask.views import MethodView
from web_app.repositories.user_repo import UserRepo


class User(MethodView):

    def __init__(self):
        super().__init__()
        self.repo = UserRepo()

    def get(self):
        user_id = request.args.get('user_id')
        users = self.repo.get(user_id)
        if not users:
            return jsonify(errors='User not found'), 404

        if user_id:
            return jsonify(user=users.to_json())

        return jsonify(users=[u.to_json() for u in users])

    def post(self):
        data = request.json
        try:
            user = self.repo.create(data)
            return jsonify(user=user.to_json()), 201
        except Exception as err:
            return jsonify(errors=str(err)), 400
