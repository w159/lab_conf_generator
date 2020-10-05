import os

import boto3

from gcg.api.controllers import validate_params
from gcg.generators import ConfigGenerator
from gcg.core import GCG, GeneratorTask
from gcg.schemas import IOSNodeSchema, NetplanSchema
from gcg.api.controllers import ControllerResult
from gcg.maps import MAP_TEMPLATE_TYPES
from gcg.env import AWS_SECRET_KEY, AWS_ACCESS_KEY


def _process(template_type, params) -> ConfigGenerator:
    _schema = MAP_TEMPLATE_TYPES.get(template_type).get('schema')

    res = validate_params(_schema, params)
    if res.status != 200:
        return res

    cg = ConfigGenerator()

    cg.generate(params)

    return cg


def controller_gcg(task: GeneratorTask, store_aws=False, **kwargs):
    config_gen = GCG()
    config_gen.add_task(task)
    config_gen.generate(
        store_aws=store_aws,
        aws_access_key=kwargs.get("aws_access_key"),
        aws_secret_key=kwargs.get("aws_secret_key"),
        lab_name=kwargs.get("lab_name")
    )

    return ControllerResult(data=task.rendered_data, result=True, msg="Successful", status=200)


def controller_ios_base_config(params):
    cg = _process("ios_base_node", params)

    return ControllerResult(data=cg.results, result=True, msg=f"Success", status=200)


def controller_linux_netplan_base(params):
    cg = _process("linux_netplan_base", params)

    return ControllerResult(data=cg.results, result=True, msg=f"Success", status=200)


def controller_cumulux_vx_base_config(params):
    pass
