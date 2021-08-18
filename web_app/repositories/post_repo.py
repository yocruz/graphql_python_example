from .base_repository import BaseRepository

from web_app.models import UserPost

class PostRepo(BaseRepository[UserPost]):

    model = UserPost
