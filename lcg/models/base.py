from marshmallow import Schema, fields

from .validators import IPValidator


class IPv6Addr(Schema):
    ipv6_address = fields.Str()
    eui_64 = fields.Str()
    link_local = fields.Str()
    anycast = fields.Str()


class IPv4Addr(Schema):
    address = fields.Str(required=True, validate=IPValidator())
    netmask = fields.Str(required=True)


class BaseInterface(Schema):
    link_id = fields.Str(required=True)
    dot1q = fields.Str()
    is_mgmt = fields.Boolean()
    description = fields.Str()
    bandwidth = fields.Str()
    ipv4_addrs = fields.List(fields.Nested(IPv4Addr))
    ipv6_addrs = fields.List(fields.Nested(IPv6Addr))


class BaseNode(Schema):
    node_type = fields.Str()
    hostname = fields.Str()
    domain = fields.Str()
    interfaces = fields.List(fields.Nested(BaseInterface))
