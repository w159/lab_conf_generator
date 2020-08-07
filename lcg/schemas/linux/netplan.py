from lcg.schemas.network import IPv4Addr, IPv6Addr, Schema, fields, IPValidator


class NetplanInterfaceSchema(Schema):
    ipv4_addrs = fields.List(fields.Nested(IPv4Addr))


class NetplanSchema(Schema):
    interfaces = fields.List(fields.Nested(NetplanInterfaceSchema))
    ipv4_gateway = fields.Str()
    nameservers = fields.List(fields.Nested(fields.Str(validate=IPValidator())))
