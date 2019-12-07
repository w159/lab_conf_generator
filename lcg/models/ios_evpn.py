from marshmallow import Schema, fields


class IOSEVISchema(Schema):
    instance_id = fields.Str(required=True)
    imports = fields.List(fields.Str, required=True)
    exports = fields.List(fields.Str, required=True)
    vlan_based = fields.Bool()


class IOSEFPSchema(Schema):
    port = fields.Str(required=True)
    efp_id = fields.Str(required=True)
    encap = fields.Str(required=True)
    c_tag = fields.Int()


class IOSBridgeDomainMemberSchema(Schema):
    member_type = fields.Str(required=True)
    efp_id = fields.Str()
    efp_instance = fields.Int()
    evpn_id = fields.Int()


class IOSBridgeDomainSchema(Schema):
    domain_id = fields.Int()
    members = fields.List(IOSBridgeDomainMemberSchema)


class IOSEVPNSchema(Schema):
    efps = fields.List(IOSEFPSchema)
    evis = fields.List(IOSEVISchema)
    bridge_domains = fields.List(IOSBridgeDomainSchema)
