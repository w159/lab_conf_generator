import requests
import json


class LCGClient:

    def __init__(self, host='127.0.0.1', port=5002):
        self._host = host
        self._port = str(port)
        self._endpoint = '/api/v1/lcg/config/base'

        self._url = f'http://{self._host}:{self._port}{self._endpoint}'

    def gen_base_config(self, data):
        resp = requests.post(
            url=f'{self._url}?template_type=ios_base_node',
            headers={'Content-Type': "application/json"},
            data=json.dumps(data)
        )
        return resp.text


def main():
    data = {
        "hostname": "R4-CORE",
        "domain": "bits.local",
        "interfaces": [
            {
                "link_id": "lo0",
                "description": "MGMT Interface",
                "ipv4_addrs": [
                    {
                        "address": "10.0.0.4",
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

    client = LCGClient(host='127.0.0.1', port=5002)
    client.gen_base_config(data)


if __name__ == "__main__":
    main()
