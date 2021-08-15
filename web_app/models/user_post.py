from datetime import datetime
from web_app import DB as db


class UserPost(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    text = db.Column(db.Text, nullable=False)
    # created = db.Column(db.DateTime, nullable=False, defaul=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
