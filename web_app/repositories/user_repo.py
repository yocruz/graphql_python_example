from web_app.models.user import User
from web_app import DB


class UserRepo:

    def get(self, id=None):
        if not id:
            return self._get_all_users()
        return self._get_user_by_id(id)

    def _get_all_users(self):
        users = User.query.all()
        return [u.to_json() for u in users]

    def _get_user_by_id(self, user_id):
        raise NotImplementedError()

    def add(self, user_data):
        raise NotImplementedError()

    def delete(self, user_id):
        raise NotImplementedError()

    def update(self, user_id, user_data):
        raise NotImplementedError()
