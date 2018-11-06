from marshmallow import Schema, fields


class PostSchema(Schema):
    title = fields.Str()
    body = fields.Str()
    sub_body = fields.Str()