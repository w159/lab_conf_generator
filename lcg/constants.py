from lcg.models.ios_bgp import IOSBGPSessionSchema, IOSBGPPolicySchema
from lcg.models.ios_base_node import IOSNodeSchema
from lcg.models.te_tunnels import IOSTETunnelSchema, IOSExplicitPath

MAP_TEMPLATE_FILES = {
    "ios_base_node": {
        "template_file": "ios_base_config.j2",
        "schema": IOSNodeSchema()
    },
    "te_tunnels": {
        "template_file": "ios_te_tunnel.j2",
        "schema": IOSTETunnelSchema()
    },
    "ios_bgp_policy": {
        "template_file": "ios_bgp_policy.j2",
        "schema": IOSBGPPolicySchema()
    },
    "ios_bgp_session": {
        "template_file": "ios_bgp_session.j2",
        "schema": IOSBGPSessionSchema()
    }
}