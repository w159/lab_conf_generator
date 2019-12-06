import unittest

from lcg.controllers.config_gen import ConfigGenerator
from test.vars import data_ios_vpls


# os.chdir("..")

class MyTestCase(unittest.TestCase):

    def test_ios_base_config(self):
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

        config_generator = ConfigGenerator()
        config_generator.set_template("ios_base_node")
        config_generator.set_output_file("../output/test_ios_base_node.txt")
        config_generator.set_facts(data_ios_base_node)

        config_generator.write()

    def test_ios_bgp_policy(self):
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

        # schema = IOSBGPPolicySchema()

        config_generator = ConfigGenerator(template_type="ios_bgp_policy",
                                           facts=data_ios_bgp_policy,
                                           output_file="../output/test_ios_bgp_policy.txt")

        config_generator.write()

    def test_ios_vpls(self):
        config_gen = ConfigGenerator(facts=data_ios_vpls,
                                     template_type="ios_vfi_vpls",
                                     output_file="../output/test_ios_vpls"
                                     )
        result = config_gen.to_stdout()
        print(result)
        self.assertIsInstance(result, str)

        vfi_count = len(config_gen.facts.get("vfis"))
        self.assertEquals(vfi_count, 1)



if __name__ == '__main__':
    unittest.main()
