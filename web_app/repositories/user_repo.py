from web_app.models.user import User
from web_app import DB

from .base_repository import BaseRepository


class UserRepo(BaseRepository[User]):

    model = User

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
