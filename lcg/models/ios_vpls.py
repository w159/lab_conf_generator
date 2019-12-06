from marshmallow import Schema, fields

VPLS_ENCAPSULATION_TYPES = ["DOT1Q"]


# TODO: Add Schema for VFI-Peers
class IOSVFIPeersSchema(Schema):
    remote_addr = fields.Str()


# TODO: Add Schema for VFI
class IOSVFISchema(Schema):
    name = fields.Str(required=True)
    vfi_id = fields.Str(required=True)
    vfi_peers = fields.Nested(IOSVFIPeersSchema)


# TODO: Add Schema for bridge-domain
# TODO: Add Schema for bridge-domain members

class IOSVPLSEncapsulationSchema(Schema):
    encap_type = fields.Str(required=True)
    c_tag = fields.Int()
    p_tag = fields.Int()


class IOSEFPSchema(Schema):
    link_id = fields.Str(required=True)
    instance_id = fields.Str(required=True)
    encapsulation = fields.Nested(IOSVPLSEncapsulationSchema)


class IOSVPLSSchema(Schema):
    pass
