import unittest

from lcg.generators import ConfigGenerator
# VARs import for various tests.
from test.vars import data_ios_vpls, data_ios_bgp_policy, data_ios_base_node


# os.chdir("..")

class MyTestCase(unittest.TestCase):

    def test_ios_base_config(self):
        config_generator = ConfigGenerator()
        config_generator.set_template("ios_base_node")
        config_generator.set_output_file("../output/test_ios_base_node.txt")
        config_generator.set_facts(data_ios_base_node)

        result = config_generator.render()

        self.assertIsInstance(result, str)

        self.assertEqual(config_generator.facts.get("hostname"), "BITS-TEST")
        self.assertEqual(config_generator.facts.get("management")["link_id"], "loopback0")

    def test_ios_bgp_policy(self):
        config_generator = ConfigGenerator(template_type="ios_bgp_policy",
                                           facts=data_ios_bgp_policy,
                                           output_file="../output/test_ios_bgp_policy.txt")

        result = config_generator.render()

        self.assertIsInstance(result, str)

        self.assertEqual(config_generator.facts.get("node_type"), "ios")
        self.assertEqual(config_generator.facts.get("policy_name"), "L3VPN_CE1")

    def test_ios_vpls(self):
        config_gen = ConfigGenerator(facts=data_ios_vpls,
                                     template_type="ios_vpls",
                                     output_file="../output/test_ios_vpls"
                                     )
        result = config_gen.render()


        self.assertIsInstance(result, str)

        vfi_count = len(config_gen.facts.get("vfis"))
        efp_count = len(config_gen.facts.get("efps"))

        self.assertEqual(vfi_count, 1)
        self.assertEqual(efp_count, 1)

    def test_ios_base_config_link_bw(self):
        """
        Test bandwidth Support for IOS devices

        """
        data = {
            "hostname": "BITS-TEST",
            "management": {
                "link_id": "loopback0",
                "ip_address": "10.0.0.1",
                "netmask": "255.255.255.255"
            },
            "interfaces": [
                {
                    "link_id": "GigabitEthernet1",
                    "bandwidth": "100",
                    "description": "Link to CSR2-PE",
                    "ip_address": "10.1.2.1",
                    "netmask": "255.255.255.252"
                },
                {
                    "link_id": "GigabitEthernet2",
                    "bandwidth": "20",
                    "description": "Link to CSR3-PE",
                    "ip_address": "10.1.3.1",
                    "netmask": "255.255.255.252"
                }
            ]
        }

        config_generator = ConfigGenerator()
        config_generator.set_template("ios_base_node")
        config_generator.set_facts(data)
        result = config_generator.render()

        self.assertIsInstance(result, str)

    def test_ios_xr_base_config_link_bw(self):
        """
        Test bandwidth Support for IOS devices

        """
        data = {
            "hostname": "BITS-TEST",
            "management": {
                "link_id": "loopback0",
                "ip_address": "10.0.0.1",
                "netmask": "255.255.255.255"
            },
            "interfaces": [
                {
                    "link_id": "GigabitEthernet0/0/0/0",
                    "bandwidth": "100",
                    "description": "Link to CSR2-PE",
                    "ip_address": "10.1.2.1",
                    "netmask": "255.255.255.252"
                },
                {
                    "link_id": "GigabitEthernet0/0/0/1",
                    "bandwidth": "20",
                    "description": "Link to CSR3-PE",
                    "ip_address": "10.1.3.1",
                    "netmask": "255.255.255.252"
                }
            ]
        }

        config_generator = ConfigGenerator()
        config_generator.set_template("xr_base_config")
        config_generator.set_facts(data)

        result = config_generator.render()

        self.assertIsInstance(result, str)

    def test_ios_base_config_ipv6_address(self):
        data = {
            "hostname": "BITS-TEST",
            "management": {
                "link_id": "loopback0",
                "ip_address": "10.0.0.1",
                "netmask": "255.255.255.255"
            },
            "interfaces": [
                {
                    "link_id": "GigabitEthernet0/0/0/0",
                    "bandwidth": "100",
                    "description": "Link to CSR2-PE",
                    "ip_address": "10.1.2.1",
                    "netmask": "255.255.255.252",
                    "ipv6_addresses": [
                        {
                            "ipv6_address": "2001:fc80:1:2::1/64",

                        },
                        {
                            "ipv6_address": "dhcp"
                        },
                        {
                            "eui_64": "fe80:1:2::/64"
                        },
                        {
                            "link_local": "fe80:1:2::1",
                        },
                        {
                            "anycast": "2001:fc80:1:2::1/64"
                        }
                    ]
                },
                {
                    "link_id": "GigabitEthernet0/0/0/1",
                    "bandwidth": "20",
                    "description": "Link to CSR3-PE",
                    "ip_address": "10.1.3.1",
                    "netmask": "255.255.255.252"
                }
            ]
        }

        config_generator = ConfigGenerator()
        config_generator.set_template("ios_base_node")
        config_generator.set_facts(data)
        result = config_generator.render()
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
