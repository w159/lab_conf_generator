from marshmallow import Schema, fields

VPLS_ENCAPSULATION_TYPES = ["DOT1Q"]


class IOSVFIPeersSchema(Schema):
    remote_addr = fields.Str()


class IOSVFISchema(Schema):
    name = fields.Str(required=True)
    vfi_id = fields.Str(required=True)
    vfi_peers = fields.List(fields.Nested(IOSVFIPeersSchema))
    bridge_domain = fields.Str(required=True)


# TODO: Add Schema for bridge-domain
class IOSBridgeDomainMemberSchema(Schema):
    member_type = fields.Str()
    link_id = fields.Str()
    instance_id = fields.Int()


class IOSBridgeDomainSchema(Schema):
    bridge_id = fields.Int()
    members = fields.List(fields.Nested(IOSBridgeDomainMemberSchema))


class IOSVPLSEncapsulationSchema(Schema):
    encap_type = fields.Str(required=True)
    c_tag = fields.Int()
    p_tag = fields.Int()


class IOSEFPSchema(Schema):
    link_id = fields.Str(required=True)
    instance_id = fields.Str(required=True)
    encapsulation = fields.Nested(IOSVPLSEncapsulationSchema)
    bridge_domain = fields.Str(required=True)
