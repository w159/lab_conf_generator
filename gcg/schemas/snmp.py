from marshmallow import Schema, fields, validate
from .validators import IPValidator
SNMPV2_GROUP_TYPES = [
    "ro",
    "rw"
]

SNMPV3_MODES = [
    "noAuthNoPriv",
    "AuthNoPriv",
    "AuthPriv"
]

AUTH_ALGS = [
    "md5",
    "sha"
]

PRIV_ALGS = [
    "3des",
    "aes_128",
    "aes_192",
    "aes_256",
    "des"
]


class BaseSNMPv2(Schema):
    community = fields.Str()
    group_type = fields.Str(validate=validate.OneOf(SNMPV2_GROUP_TYPES))


class BaseSNMPv3(Schema):
    mode = fields.Str(validate=validate.OneOf(SNMPV3_MODES))
    peer = fields.Str(validate=IPValidator())
    group_name = fields.Str(required=True)
    username = fields.Str(required=True)
    auth_pw = fields.Str()
    priv_pw = fields.Str()
    auth_alg = fields.Str(validate=validate.OneOf(AUTH_ALGS))
    priv_alg = fields.Str(validate=validate.OneOf(PRIV_ALGS))
