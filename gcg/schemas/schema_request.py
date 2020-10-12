from datetime import datetime

from marshmallow import Schema, fields


class APIOpts(Schema):
    template_type = fields.Str(required=True)


class GCGAPIOpts(APIOpts):
    lab_name = fields.Str(default=f'GCG_API_{str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))}')
    name = fields.Str(default=f'GCG_API_{str(datetime.now().strftime("%m_%d_%Y"))}')
    store_aws = fields.Boolean(default=False)


class APIRequest(Schema):
    opts = fields.Nested(APIOpts)
    data = fields.Dict()
