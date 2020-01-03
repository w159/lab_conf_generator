import json
from flask import Response, jsonify
from app.constants import JSON_RESPONSE_HEADERS
import json

from flask import Response

JSON_RESPONSE_HEADERS = {'content-type': 'application/json; charset=utf-8'}


class APIResponse:
    """
    This class is an JSON Response object that will be return the API requestors.

    """

    def __init__(self, *args, **kwargs):
        self.data = kwargs.get("data")
        self.msg = kwargs.get("msg")
        self.exception = kwargs.get("exception")
        self.status = kwargs.get("status")

    def __call__(self, *args, **kwargs):
        response = {"response": kwargs.get("data"), "msg": kwargs.get("msg"), "exception": kwargs.get("exception"), }

        return Response(json.dumps(response), headers=JSON_RESPONSE_HEADERS, status=self.status)


def make_json_response(data: dict, msg, status_code, headers=None):
    if not headers:
        headers = JSON_RESPONSE_HEADERS

    return Response(response=json.dumps({"data": data, "msg": msg}), status=status_code, headers=headers)
