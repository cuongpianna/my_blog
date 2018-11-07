from marshmallow import Schema, fields, validates, ValidationError


class PostSchema(Schema):
    title = fields.Str()
    body = fields.Str()

    @validates('title')
    def validate_title(self, value):
        if len(value) < 6:
            raise ValidationError('Title must be greater than 6')
        elif len(value) > 64:
            raise ValidationError('Title must not be greater than 64')