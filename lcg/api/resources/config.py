from flask_restful import Resource, request
from lcg.api.controllers.config import controller_ios_base_config, ControllerResult
from lcg.utils import make_json_response, make_text_response


class BaseConfigResource(Resource):

    @staticmethod
    def post():

        json_data = request.json
        args = request.args

        template_type = args.get("template_type")
        return_type = args.get("return_type", "text")

        result = None
        json_data['template_type'] = template_type

        if template_type == "ios_base_node":
            result = controller_ios_base_config(json_data)

        if isinstance(result, ControllerResult):
            if return_type == "text":
                return make_text_response(result.data, result.msg, result.status)

            elif return_type == "json":
                return make_json_response(result.data, result.msg, result.status)

            elif return_type == "list":
                return make_json_response(result.data.split("\n"), result.msg, result.status)

        return make_json_response(None, "Unsupported node_type", 400)
