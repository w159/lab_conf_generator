from marshmallow import Schema, fields


class IPV6Address(Schema):
    ipv6_address = fields.Str()
    eui_64 = fields.Str()
    link_local = fields.Str()
    anycast = fields.Str()


class IOSInterfaceSchema(Schema):
    link_id = fields.Str(required=True)
    bandwidth = fields.Str(description="Bandwidth of link, expressed in megabits per second")
    description = fields.Str()
    ip_address = fields.Str()
    netmask = fields.Str()
    ipv6_addresses = fields.List(fields.Nested(IPV6Address))


class IOSManagementSchema(Schema):
    link_id = fields.Str()
    description = fields.Str()
    ip_address = fields.Str()
    netmask = fields.Str()


class IOSNodeSchema(Schema):
    node_type = fields.Str()
    hostname = fields.Str()
    management = fields.Nested(IOSManagementSchema)
    interfaces = fields.List(fields.Nested(IOSInterfaceSchema))
