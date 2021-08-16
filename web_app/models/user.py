from web_app import DB as db
from .base_model import BaseModel, SerializableModel


class User(db.Model, BaseModel, SerializableModel):
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(1), nullable=True)
    posts = db.relationship('UserPost', backref='user', lazy=True)

    SERIALIZABLE_FIELDS = [
        'id',
        'username',
        'email',
        'gender',
        'posts',
    ]
