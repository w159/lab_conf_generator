import json
from functools import wraps

from flask import Flask, jsonify, render_template, Response
from flask_restful import Api
from mongoengine import connect

from gcg.api.models import BaseConfigDocument
from gcg.api.resources import (
    ConfigIOSBaseResource,
    ConfigLinuxNetplanBasicResource,
    GCGResource
)
from gcg.env import DB_HOST, DB_PORT, DB
from gcg.constants import STATUS_200_SUCCESS, JSON_RESPONSE_HEADERS
from gcg.utils import APIResponse

# ---- Flask Config ----
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

api = Api(app)

connect(db=DB, host=DB_HOST, port=DB_PORT)

# --- API Registration ---

api.add_resource(ConfigIOSBaseResource, "/api/v1/lcg/config/ios/base")
api.add_resource(GCGResource, "/api/v1/gcg")
api.add_resource(ConfigLinuxNetplanBasicResource, "/api/v1/lcg/config/linux/netplan")


# --- Routes ---
@app.route("/")
def index():
    return render_template("index.jinja2")


@app.route("/grid")
def grid():
    return render_template("grid.j2")


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
