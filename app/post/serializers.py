from marshmallow import Schema, fields, validates, ValidationError
from app.post.models import Category


class PostSchema(Schema):
    title = fields.Str()
    body = fields.Str()

    @validates('title')
    def validate_title(self, value):
        if len(value) < 6:
            raise ValidationError('Title must be greater than 6')
        elif len(value) > 255:
            raise ValidationError('Title must not be greater than 255')

class CategorySchema(Schema):
    name = fields.Str()

    @validates('name')
    def validate_name(self, value):
        if len(value) < 6:
            raise ValidationError('Category name must be greater than 6')
        elif len(value) > 255:
            raise ValidationError('Category must not be greater than 255')
        else:
            cate = Category.query.filter_by(name=value).first()
            if cate:
                raise ValidationError('Category already exists')
