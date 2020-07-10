from lcg.models.ios_base_node import IOSNodeSchema
from lcg.models.ios_bgp import IOSBGPSessionSchema, IOSBGPPolicySchema
from lcg.models.ios_evpn import IOSEVPNSchema
from lcg.models.ios_vpls import IOSVPLSSchema
from lcg.models.te_tunnels import IOSTETunnelSchema, IOSExplicitPathSchema
import os

MAP_TEMPLATE_TYPES = {
    "ios_base_node": {
        "template_file": "ios/base_config.j2",
        "schema": IOSNodeSchema()
    },
    "ios_rtr": {
        "template_file": "ios/base_config.j2",
        "schema": IOSNodeSchema()
    },
    "ios_te_tunnels": {
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
    },
    "ios_explicit_path": {
        "template_file": "ios_explicit_path.j2",
        "schema": IOSExplicitPathSchema()
    },
    "ios_vpls": {
        "template_file": "ios_vpls.j2",
        "schema": IOSVPLSSchema(),
    },
    "ios_evpn": {
        "template_file": "ios_evpn.j2",
        "schema": IOSEVPNSchema()

    },
    "xr_base_config": {
        "template_file": "ios_xr/base_config.j2",
        "schema": IOSNodeSchema()
    }

}
