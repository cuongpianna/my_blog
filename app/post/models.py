from datetime import datetime
from slugify import slugify
from app.helpers.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), unique=True, nullable=False)
    slug_title = db.Column(db.String(64), unique=True, nullable=False)
    body = db.Column(db.String(), nullable=False)
    sub_body = db.Column(db.String(), default='')
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())

    @staticmethod
    def get_sub_body(value):
        return value[0:300]

    def __setattr__(self, key, value):
        super(Post, self).__setattr__(key, value)
        if key == 'body':
            self.sub_body = self.get_sub_body(self.body)
        if key == 'title':
            self.slug_title = slugify(self.title)

    def __repr__(self):
        return '<Post {}>'.format(self.title)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    slug_name = db.Column(db.String(100), unique=True, nullable=False)

    def __setattr__(self, key, value):
        super(Category, self).__setattr__(key, value)
        if key == 'name':
            self.slug_name = slugify(self.name)

    def __repr__(self):
        return '<Category {}>'.format(self.name)

