from web_app.models.user import User
from web_app import DB


class UserRepo:

    def get(self, id=None):
        if not id:
            return self._get_all_users()
        return self._get_user_by_id(id)

    def _get_all_users(self):
        users = User.query.all()
        return users

    def _get_user_by_id(self, user_id):
        user = User.query.get(user_id)
        return user

    def add(self, user_data: dict):
        new_user = User.from_json(user_data)
        DB.session.add(new_user)
        DB.session.commit()
        new_user.reload()
        return new_user

    def delete(self, user_id):
        raise NotImplementedError()

    def update(self, user_id, user_data):
        raise NotImplementedError()
