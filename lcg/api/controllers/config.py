from lcg.api.controllers import validate_params
from lcg.generators import ConfigGenerator
from lcg.schemas import IOSNodeSchema
from lcg.api.controllers import ControllerResult


def _process(template_type, params) -> ConfigGenerator:
    res = validate_params(IOSNodeSchema, params)
    if res.status != 200:
        return res

    cg = ConfigGenerator()


    cg.generate(params)

    return cg


def controller_ios_base_config(params):
    res = validate_params(IOSNodeSchema, params)
    if res.status != 200:
        return res

    cg = _process("ios_base_node", params)

    return ControllerResult(data=cg.results, result=True, msg=f"Success", status=200)


def controller_cumulux_vx_base_config(params):
    pass
