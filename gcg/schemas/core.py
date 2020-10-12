from marshmallow import Schema, fields


class TaskSchema(Schema):
    opts = fields.Dict()
    data = fields.Dict()
