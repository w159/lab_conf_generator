import json

from flask import Response, jsonify
from flask_restful import Resource, request
from lcg.api.controllers.config import controller_ios_base_config, ControllerResult
from lcg.utils import make_json_response, make_text_response


class BaseConfigResource(Resource):

    @staticmethod
    def post():

        json_data = request.json
        args = request.args

        node_type = args.get("node_type")

        result = None

        if node_type == "ios_rtr":
            result = controller_ios_base_config(json_data)

        if isinstance(result, ControllerResult):
            return make_text_response(result.data, result.msg, result.status)

        return make_json_response(None, "Supported node_type", 400)
