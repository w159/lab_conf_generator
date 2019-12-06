data_ios_vpls = {
    "EFPS": [
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
