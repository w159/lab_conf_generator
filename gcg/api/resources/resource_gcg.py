import http.client as http_status_codes
from datetime import datetime
from distutils.util import strtobool
from flask_restful import Resource, request
from gcg.api.controllers.controller_gcg import controller_gcg_v2, ControllerResult
from gcg.exceptions import GCGValidationError
from gcg.schemas import schema_request
from gcg.utils import make_json_response, make_text_response


class GCGResource(Resource):

    @staticmethod
    def post():
        request_schema = schema_request.GCGAPIOpts()

        # Extract Header Info
        AWS_ACCESS_KEY = request.headers['X-Api-Key']
        AWS_SECRET_KEY = request.headers['X-Api-Secret']
        USER_AGENT = request.headers['User-Agent']

        # Extracts URL params
        url_params = request.args

        return_type = url_params.get("return_type", "json")
        store_aws = bool(strtobool(url_params.get("store_aws", 'false')))
        template_type = url_params.get("template_type")
        name = url_params.get("name", f'GCG_API_{str(datetime.now().strftime("%m_%d_%Y_%H_%M_%S"))}')
        lab_name = url_params.get("lab_name", f'GCG_API_{str(datetime.now().strftime("%m_%d_%Y"))}')

        # Extracts JSON Body

        json_data = request.json

        # Generate Config
        try:
            result = controller_gcg_v2(
                data=json_data,
                store_aws=store_aws,
                store_local=False,
                template_type=template_type,
                lab_name=lab_name,
                name=name,
            )

            if isinstance(result, ControllerResult):
                if return_type == "text":
                    return make_text_response(
                        data=result.data,
                        msg="Success",
                        status_code=http_status_codes.OK
                    )
                else:
                    return make_json_response(
                        data=result.data,
                        msg="Success",
                        status_code=http_status_codes.OK
                    )
            else:
                return

        except GCGValidationError as err:
            return make_json_response(
                data={},
                msg=f"Validation Error: {str(err)}",
                status_code=http_status_codes.CONFLICT
            )


