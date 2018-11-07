from datetime import datetime
from app.helpers.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, nullable=False)
    body = db.Column(db.String(), nullable=False)
    sub_body = db.Column(db.String(), default='')
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())

    def set_sub_body(self, value):
        self.sub_body = value[0:300]

    def __repr__(self):
        return '<Post {}>'.format(self.title)
