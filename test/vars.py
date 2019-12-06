data_ios_vpls = {
    "efps": [
        {
            "link_id": "GigabitEthernet1",
            "instance_id": "10",
            "encapsulation": {
                "encap_type": "DOT1Q",
                "c_tag": 200
            }
        },
        {
            "link_id": "GigabitEthernet2",
            "instance_id": "10",
            "encapsulation": {
                "encap_type": "DOT1Q",
                "c_tag": 300
            }
        }
    ],
    "vfis": [
        {
            "name": "CE1_VPLS",
            "vfi_id": 100,
            "vfi_peers": [
                {
                    "remote_addr": "10.0.0.1"
                },
                {
                    "remote_addr": "10.0.0.5"
                }
            ]
        }
    ],
    "bridge_domains": [
        {
            "id": 100,
            "members": [
                {
                    "member_type": "ac",
                    "link_id": "GigabitEthernet1",
                    "instance_id": 100
                },
                {
                    "member_type": "vfi",
                    "vfi_name": "CE1_VPLS"
                }
            ]
        }
    ]
}

data_ios_bgp_policy = {
    "node_type": "ios",
    "policy_name": "L3VPN_CE1",
    "send_community_both": True,
    "orf_bidir": True,
    "soft_reconfiguration": True,
    "maximum_prefix": 50,
    "route_map_in": "L3VPN_CE1_IN",
    "route_map_out": "L3VPN_CE1_OUT",
    "site_of_origin": "100:01"
}

data_ios_base_node = {
            "hostname": "BITS-TEST",
            "management": {
                "link_id": "loopback0",
                "ip_address": "10.0.0.1",
                "netmask": "255.255.255.255"
            },
            "interfaces": [
                {
                    "link_id": "GigabitEthernet1",
                    "description": "Link to CSR2-PE",
                    "ip_address": "10.1.2.1",
                    "netmask": "255.255.255.252"
                },
                {
                    "link_id": "GigabitEthernet2",
                    "description": "Link to CSR3-PE",
                    "ip_address": "10.1.3.1",
                    "netmask": "255.255.255.252"
                }
            ]
        }
