from marshmallow import Schema, fields, validates, ValidationError
from app.post.models import Post, Category


class PostSchema(Schema):
    title = fields.Str()
    body = fields.Str()

    @validates('title')
    def validate_title(self, value):
        if len(value) < 6:
            raise ValidationError('Title must be greater than 6')
        elif len(value) > 64:
            raise ValidationError('Title must not be greater than 64')
        else:
            post = Post.query.filter_by(title=value).first()
            if post:
                raise ValidationError('Title does not exist!')


class CategorySchema(Schema):
    name = fields.Str()

    @validates('name')
    def validate_name(self, value):
        if len(value) < 6:
            raise ValidationError('Title must be greater than 6')
        elif len(value) > 64:
            raise ValidationError('Title must not be greater than 100')
        else:
            post = Category.query.filter_by(name=value).first()
            if post:
                raise ValidationError('Category does not exist!')
