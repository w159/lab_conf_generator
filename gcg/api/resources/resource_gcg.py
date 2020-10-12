from flask_restful import Resource, request
from gcg.api.controllers.controller_gcg import controller_gcg, Task, ControllerResult
from gcg.utils import make_json_response, make_text_response
from gcg.schemas import schema_request
from marshmallow.exceptions import ValidationError
from datetime import datetime
import json

from distutils.util import strtobool


class GCGResource(Resource):

    @staticmethod
    def post():
        request_schema = schema_request.GCGAPIOpts()

        json_data = request.json

        url_params = request.args

        # Extracts URL params
        return_type = url_params.get("return_type", "json")
        store_aws = url_params.get("return_type", False)
        template_type = url_params.get("template_type")
        name = url_params.get("name")
        lab_name = url_params.get("lab_name")

        # Extracts the request options in the JSON body
        request_opts = json_data.get("opts")
        if request_opts is None:
            return make_json_response({}, "Missing json body opts", status_code=409)

        try:
            request_opts = request_schema.loads(json.dumps(request_opts))
            if not request_opts.get("name"):
                name = f'GCG_API_{str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))}'
            else:
                name = request_opts.get("name")

            if not request_opts.get("lab_name"):
                lab_name = f'GCG_API_{str(datetime.now().strftime("%m_%d_%Y"))}'
            else:
                lab_name = request_opts.get("lab_name")

        except ValidationError as error:
            return make_json_response(data={}, msg=f"Option Validation Error: {str(error)}", status_code=409)

        store_aws = request_opts.get("store_aws", False)

        result = controller_gcg(json_data=json_data, store_aws=store_aws, lab_name=lab_name, name=name)

        if isinstance(result, ControllerResult):
            if return_type == "text":

                return make_text_response(result.data, result.msg, result.status)

            elif return_type == "json":
                return make_json_response(result.data, result.msg, result.status)

            elif return_type == "list":
                return make_json_response(result.data.split("\n"), result.msg, result.status)

        return make_json_response(None, "Unsupported Template Type", 400)
