data_ios_vpls = {
    "EFPS": [
        {
            "link_id": "GigabitEthernet1",
            "instance_id": "10",
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
            "vfi_peers": [
                {
                    "remote_addr": "10.0.0.1"
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
                    "type": "vfi",
                    "vfi_name": "CE1_VPLS"
                }
            ]
        }
    ]
}
