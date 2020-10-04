from flask_restful import Resource, request
from gcg.api.controllers.config import controller_gcg, GeneratorTask, ControllerResult
from gcg.utils import make_json_response, make_text_response


class GCGResource(Resource):

    @staticmethod
    def post():

        json_data = request.json
        args = request.args

        return_type = args.get("return_type", "json")
        name = args.get("name")
        store_aws = args.get("store_aws", False)

        task = GeneratorTask.new(data=json_data, name=name)

        result = controller_gcg(task=task, store_aws=bool(store_aws))
        #
        if isinstance(result, ControllerResult):
            if return_type == "text":

                return make_text_response(result.data, result.msg, result.status)

            elif return_type == "json":
                return make_json_response(result.data, result.msg, result.status)

            elif return_type == "list":
                return make_json_response(result.data.split("\n"), result.msg, result.status)

        return make_json_response(None, "Unsupported node_type", 400)
