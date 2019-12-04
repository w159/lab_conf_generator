from marshmallow import Schema, fields


class IOSInterfaceSchema(Schema):
    link_id = fields.Str()
    description = fields.Str()
    ip_address = fields.Str()
    netmask = fields.Str()


class IOSManagementSchema(Schema):
    link_id = fields.Str()
    description = fields.Str()
    ip_address = fields.Str()
    netmask = fields.Str()


class IOSNodeSchema(Schema):
    hostname = fields.Str()
    management = fields.Nested(IOSManagementSchema)
    interfaces = fields.List(fields.Nested(IOSInterfaceSchema))
