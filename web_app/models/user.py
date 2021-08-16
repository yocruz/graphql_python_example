from web_app import DB as db
from .serializable_model import SerializableModel


class User(db.Model, SerializableModel):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
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
