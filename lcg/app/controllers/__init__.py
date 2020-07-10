import json


class ControllerResult:
    def __init__(self, data: object, result: bool, msg: str, exception: Exception = None):
        self.result = result
        self.msg = msg
        self.exception = exception
        self.data = data

    @staticmethod
    def new(data: object, result: bool, msg: str, exception: Exception = None):
        return ControllerResult(data, result, msg, exception)

    def to_json(self):
        return json.dumps({
            "result": self.result,
            "msg": self.msg,
            "data": self.data,
            "exception": str(self.exception)

        })
