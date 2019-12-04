from marshmallow import Schema, fields


class IOSBGPPolicySchema(Schema):
    node_type = fields.Str(required=True)
    policy_name = fields.Str(required=True)
    send_community_both = fields.Bool()
    orf_bidir = fields.Bool()
    soft_reconfiguration = fields.Bool()
    maximum_prefix = fields.Int()
    route_map_in = fields.Str()
    route_map_out = fields.Str()
    site_of_origin = fields.Str()


class IOSBGPSessionSchema(Schema):
    node_type = fields.Str(required=True)
    policy_name = fields.Str(required=True)
    remote_as = fields.Str(required=True)
    description = fields.Str()
    password = fields.Str()
    update_source = fields.Str()
