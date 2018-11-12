from datetime import datetime
from slugify import slugify
from app.helpers.extensions import db
from app.mixin.base import PaginatedAPIMixin


class Post(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    slug_title = db.Column(db.String(255), unique=True)
    body = db.Column(db.String(), nullable=False)
    sub_body = db.Column(db.String(), default='')
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def __setattr__(self, key, value):
        super(Post, self).__setattr__(key, value)
        if key == 'title':
            self.slug_title = slugify(self.title)

    def to_json(self):
        return dict(
            id = self.id,
            title = self.title,
            slug_title = self.slug_title,
            category_id = self.category_id,
            body = self.body,
            sub_body = self.sub_body,
            time_stamp = self.time_stamp.strftime('%Y-%m-%d %H:%M:%S')
        )

    def __repr__(self):
        return '<Post {}>'.format(self.title)

class Category(PaginatedAPIMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    slug_name = db.Column(db.String(255), unique=True)
    posts = db.relationship('Post', backref='category', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __setattr__(self, key, value):
        super(Category, self).__setattr__(key, value)
        if key == 'name':
            self.slug_name = slugify(self.name)
    
    def to_json(self):
        return dict(
            id = self.id,
            name = self.name,
            slug_name = self.slug_name,
            created_at = self.created_at
            )


