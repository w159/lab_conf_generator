from marshmallow import Schema, fields


class IOSTETunnelSchema(Schema):
    tunnel_id = fields.Str(required=True)
    description = fields.Str()
    tunnel_source = fields.Str()
    tunnel_destination = fields.Str()
    autoroute = fields.Bool(default=False)


class IOSExplicitPathSchema(Schema):
    name = fields.Str(required=True)
    next_hops = fields.List(fields.Str())


