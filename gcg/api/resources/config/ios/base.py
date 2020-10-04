from flask_restful import Resource, request
from gcg.api.controllers.config import controller_ios_base_config, ControllerResult
from gcg.utils import make_json_response, make_text_response


class ConfigIOSBaseResource(Resource):

    @staticmethod
    def post():

        json_data = request.json
        args = request.args

        return_type = args.get("return_type", "json")

        json_data['template_type'] = 'ios_base_node'

        result = controller_ios_base_config(json_data)

        if isinstance(result, ControllerResult):
            if return_type == "text":

                return make_text_response(result.data, result.msg, result.status)

            elif return_type == "json":
                return make_json_response(result.data, result.msg, result.status)

            elif return_type == "list":
                return make_json_response(result.data.split("\n"), result.msg, result.status)

        return make_json_response(None, "Unsupported node_type", 400)
