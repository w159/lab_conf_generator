from marshmallow import Schema, fields, validate

from .base import BaseNode, BaseInterface

OSPF_NETWORK_TYPES = [
    "point-to-point",
    "point-to-multipoint",
    "non-broadcast ",
    "broadcast ",
]

class IOSMessageDigest(Schema):
    key_id = fields.Str(required=True)
    val = fields.Str(required=True)

class IOSInterfaceOSPFAuth(Schema):
    key_chain = fields.Str()
    key = fields.Str()
    message_digest = fields.List(fields.Nested(IOSMessageDigest))
    is_null = fields.Boolean(default=False)


class IOSInterfaceOSPF(Schema):
    p_id = fields.Str(required=True)
    area_id = fields.Str(required=True)
    network_type = fields.Str(default="point-to-point", validate=validate.OneOf(OSPF_NETWORK_TYPES))
    priority = fields.Str(default=1)
    is_shutdown = fields.Boolean(default=False)
    mtu_ignore = fields.Boolean(default=False)
    auth = fields.Nested(IOSInterfaceOSPFAuth)


class IOSInterfaceMPLS(Schema):
    ldp = fields.Boolean(default=False)
    mpls_te = fields.Boolean(default=False)

class IOSInterface(BaseInterface):
    ospf = fields.Nested(IOSInterfaceOSPF)
    mpls = fields.Nested(IOSInterfaceMPLS)


class IOSNodeSchema(BaseNode):
    interfaces = fields.List(fields.Nested(IOSInterface))
