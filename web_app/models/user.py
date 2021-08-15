from web_app import DB as db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(1), nullable=True)
    posts = db.relationship('UserPost', backref='user', lazy=True)