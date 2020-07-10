import json
import os

from flask import Response, jsonify
from flask_restful import Resource, request
from lcg.app.models import APIRequest
from lcg.app.utils import make_file_path
from lcg.controllers.config_gen import ConfigGenerator
from lcg.constants import MAP_TEMPLATE_TYPES
from lcg.app.db import ConfigRecord, is_config_present
from lcg.app.constants import JSON_RESPONSE_HEADERS, TEXT_RESPONSE_HEADERS
from lcg.app.utils import make_json_response


class ConfigResource(Resource):

    def get(self):
        """
        Returns an Empty Data Schema to be Utilized new configruations
        """
        schema = None
        args = request.args

        types = MAP_TEMPLATE_TYPES.keys()

        if args.get("node_type") == "ios_rtr":
            path = make_file_path(__file__, "json_models/ios_rtr_base_config.json")

            with open(path, "r") as f:
                schema = json.load(f)
        if schema:
            return jsonify(schema)
        else:
            return make_json_response(
                data={},
                status_code=400,
                msg=f"Invalid Params, Missing 'node_type' Key, Valid Values: {list(types)}"
            )

    def post(self):
        request_schema = APIRequest()

        json_data = request.json

        results = request_schema.validate(json_data)
        if len(results) > 0:  # Validates if there are any schema validation errors
            raise Exception(f'ERROR: Invalid Request: {results}')

        cg = ConfigGenerator()

        req_data = json_data.get("data")
        req_opts = json_data.get("opts")

        cg.set_template(req_data.get("node_type"))
        cg.set_facts(req_data)

        config = cg.render()

        if req_opts.get("store"):
            opt_lab_name = req_opts.get("lab_name")
            opt_dev_name = req_opts.get("dev_name")
            opt_update = req_opts.get("update", False)

            if is_config_present(opt_dev_name, opt_lab_name):
                document = ConfigRecord.objects(dev_name=opt_dev_name, lab_name=opt_lab_name).first()
                document.delete()
                doc = ConfigRecord(data=config, dev_name=opt_dev_name, lab_name=opt_lab_name)
                doc.save()
                if not opt_update:
                    return Response(
                        response=json.dumps(
                            {"is_stored": False, "msg": f"{opt_dev_name} already present in lab: {opt_lab_name}"}),
                        headers=JSON_RESPONSE_HEADERS,
                        status=400

                    )

                return Response(
                    response=json.dumps(
                        {"is_stored": True, "msg": f'{opt_dev_name} in lab "{opt_lab_name}" successfully updated'}),
                    headers=JSON_RESPONSE_HEADERS,
                    status=200
                )

            document = ConfigRecord(
                data=config,
                lab_name=opt_lab_name,
                dev_name=opt_dev_name
            )
            try:

                document.save()
                return Response(
                    response=json.dumps({"is_stored": True, "data": config}),
                    headers=JSON_RESPONSE_HEADERS,
                    status=201)

            except Exception:
                raise

        return Response(response=config, headers=TEXT_RESPONSE_HEADERS)

    def put(self):
        pass

    def delete(self):
        pass

    def patch(self):
        pass
