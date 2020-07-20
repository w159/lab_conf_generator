from marshmallow import Schema, fields


class APIOpts(Schema):
    store = fields.Boolean(default=False)
    lab_name = fields.Str(required=True)
    dev_name = fields.Str(required=True)
    update = fields.Boolean(default=False)
    node_eve_id = fields.Str()


class APIRequest(Schema):
    opts = fields.Nested(APIOpts)
    data = fields.Dict()
