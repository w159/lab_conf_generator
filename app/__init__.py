import json
from functools import wraps

from flask import Flask, jsonify, render_template, Response, request
from flask_restful import Api
from mongoengine import connect

from app.models.model_base_config import BaseConfigDocument
from app.models.request import APIRequest
from config import DB_HOST, DB_PORT, DB
from lcg.controllers.config_gen import ConfigGenerator
from .constants import STATUS_200_SUCCESS, JSON_RESPONSE_HEADERS, TEXT_RESPONSE_HEADERS
from .db import ConfigRecord, is_config_present
from .utils import APIResponse

# ---- Flask Config ----
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

api = Api(app)

connect(db=DB, host=DB_HOST, port=DB_PORT)


# --- Routes ---
@app.route("/")
def index():
    return render_template("index.jinja2")


# --- Routes ---
@app.route("/grid")
def grid():
    return render_template("grid.j2")


@app.route("/api/v1/lcg/config", methods=['POST', 'GET'])
def add_node():
    request_schema = APIRequest()

    if request.method == "POST":  # Executes if the incoming request is a POST request

        json_data = request.json
        results = request_schema.validate(json_data)
        if len(results) > 0: # Validates if there are any schema validation errors
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

    return render_template("add_node.j2")


@app.route("/api/v1/nodes")
def get_nodes():
    db_nodes = BaseConfigDocument.objects().exclude("id")
    nodes = []
    for node in db_nodes:
        nodes.append(node.to_json())

    return Response(response=json.dumps(nodes), headers=JSON_RESPONSE_HEADERS)


@app.route("/api/v1/node/<hostname>")
def get_node(hostname):
    node_data = BaseConfigDocument.objects(hostname=hostname).exclude("id").first()
    if node_data:
        return Response(response=json.dumps(node_data.to_json()), headers=JSON_RESPONSE_HEADERS)


@app.route("/app/login")
def api_login():
    # TODO: Implement login logic, return JWT token to requester.
    return APIResponse(data=jsonify({"token": None}), status=STATUS_200_SUCCESS)


@app.route("/app/logout")
def api_logout():
    # TODO: Implement logic for logging the requester out.
    return APIResponse(data=jsonify({"data": "index Hit"}), status=STATUS_200_SUCCESS)


@app.route("/app/register")
def api_register():
    # TODO: Implement logic for registering users that will utilize the API.
    return APIResponse(data=jsonify({"data": "index Hit"}), status=STATUS_200_SUCCESS)


# --- Helper Funcs and Decorators ---
def token_required(f):
    """
    Use this decorator to protect API calls
    :param f:
    :return:
    """

    @wraps
    def decorated(*args, **kwargs):
        # TODO: Implement JWT authentication logic
        return f(*args, **kwargs)

    return decorated
