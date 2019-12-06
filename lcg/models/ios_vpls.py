from marshmallow import Schema, fields

VPLS_ENCAPSULATION_TYPES = ["DOT1Q"]


# TODO: Add Schema for VFI
# TODO: Add Schema for VFI-Peers
# TODO: Add Schema for bridge-domain
# TODO: Add Schema for bridge-domain members

class IOSVPLSEncapsulationSchema(Schema):
    encap_type = fields.Str(required=True)
    c_tag = fields.Int()
    p_tag = fields.Int()


class IOSVPLSEFPSchema(Schema):
    link_id = fields.Str(required=True)
    instance_id = fields.Str(required=True)
    encapsulation = fields.Nested(IOSVPLSEncapsulationSchema)


class IOSVPLSSchema(Schema):
    pass
