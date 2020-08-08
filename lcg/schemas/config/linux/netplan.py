from lcg.schemas.network import IPv4Addr, IPv6Addr, Schema, fields, IPValidator


class NetplanInterfaceSchema(Schema):
    link_id = fields.Str(required=True)
    ipv4_addrs = fields.List(fields.Nested(IPv4Addr()))
    nameservers = fields.List(fields.Str(validate=IPValidator()))
    ipv4_gateway = fields.Str()


class NetplanSchema(Schema):
    template_type = fields.Str(required=True)
    interfaces = fields.List(fields.Nested(NetplanInterfaceSchema()))
