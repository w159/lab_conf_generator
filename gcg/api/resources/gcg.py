from flask_restful import Resource, request
from gcg.api.controllers.config import controller_gcg, GeneratorTask, ControllerResult
from gcg.utils import make_json_response, make_text_response


class GCGResource(Resource):

    @staticmethod
    def post():

        json_data = request.json
        url_params = request.args

        # Extracts URL params
        return_type = url_params.get("return_type", "json")
        name = url_params.get("name")
        store_aws = url_params.get("store_aws", False)
        lab_name = url_params.get("lab_name")

        # Extracts API Options


        task = GeneratorTask.new(data=json_data, name=name)

        result = controller_gcg(task=task, store_aws=bool(store_aws), lab_name=lab_name)
        #
        if isinstance(result, ControllerResult):
            if return_type == "text":

                return make_text_response(result.data, result.msg, result.status)

            elif return_type == "json":
                return make_json_response(result.data, result.msg, result.status)

            elif return_type == "list":
                return make_json_response(result.data.split("\n"), result.msg, result.status)

        return make_json_response(None, "Unsupported node_type", 400)
