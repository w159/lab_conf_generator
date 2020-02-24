from marshmallow import Schema, fields


class IOSInterfaceSchema(Schema):
    link_id = fields.Str(required=True)
    bandwidth = fields.Str(description="Bandwidth of link, expressed in megabits per second")
    description = fields.Str()
    ip_address = fields.Str()
    netmask = fields.Str()


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
