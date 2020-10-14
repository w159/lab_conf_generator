data_ios_vpls = {
    "efps": [
        {
            "link_id": "GigabitEthernet1",
            "instance_id": "10",
            "bridge_domain": "100",
            "encapsulation": {
                "encap_type": "DOT1Q",
                "c_tag": 200
            }
        }
    ],
    "vfis": [
        {
            "name": "CE1_VPLS",
            "vfi_id": 100,
            "bridge_domain": 100,
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

data_task_empty = {

    "data": {
    }

}

data_task = {

    "hostname": "R1-CORE",
    "domain": "bits.local",
    "interfaces": [
        {
            "link_id": "lo0",
            "description": "MGMT Interface",
            "ipv4_addrs": [
                {
                    "address": "10.0.0.1",
                    "netmask": "255.255.255.255"
                }
            ]
        },
        {
            "link_id": "Gi1",
            "bandwidth": "100",
            "description": "CSR2",
            "mpls": {
                "ldp": True
            },
            "ospf": {
                "p_id": "1",
                "area_id": "100",
                "network_type": "point-to-point",
                "auth": {
                    "is_null": True
                }
            },
            "ipv4_addrs": [
                {
                    "address": "10.2.4.2",
                    "netmask": "255.255.255.252"
                }
            ],
            "ipv6_addrs": [
                {
                    "ipv6_address": "2001:2:4::2/64"
                }
            ]
        },
        {
            "link_id": "Gi2",
            "bandwidth": "50",
            "description": "CSR3",
            "mpls": {
                "ldp": True
            },
            "ospf": {
                "p_id": "1",
                "area_id": "100",
                "network_type": "point-to-point",
                "auth": {
                    "is_null": True
                }
            },
            "ipv4_addrs": [
                {
                    "address": "10.3.4.2",
                    "netmask": "255.255.255.252"
                }
            ],
            "ipv6_addrs": [
                {
                    "ipv6_address": "2001:3:4::2/64"
                }
            ]
        },
        {
            "link_id": "Gi3",
            "bandwidth": "100",
            "description": "CSR7",
            "mpls": {
                "ldp": True
            },
            "ospf": {
                "p_id": "1",
                "area_id": "100",
                "auth": {
                    "is_null": True
                }
            },
            "ipv4_addrs": [
                {
                    "address": "10.4.7.1",
                    "netmask": "255.255.255.252"
                }
            ],
            "ipv6_addrs": [
                {
                    "ipv6_address": "2001:4:7::1/64"
                }
            ]
        },
        {
            "link_id": "Gi4",
            "bandwidth": "100",
            "description": "CSR8",
            "mpls": {
                "ldp": True
            },
            "ospf": {
                "p_id": "1",
                "area_id": "100",
                "auth": {
                    "is_null": True
                }
            },
            "ipv4_addrs": [
                {
                    "address": "10.4.8.1",
                    "netmask": "255.255.255.252"
                }
            ],
            "ipv6_addrs": [
                {
                    "ipv6_address": "2001:4:8::1/64"
                }
            ]
        }
    ]
}
