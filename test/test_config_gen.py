import unittest

from lcg.controllers.config_gen import ConfigGenerator
# VARs import for various tests.
from test.vars import data_ios_vpls, data_ios_bgp_policy, data_ios_base_node


# os.chdir("..")

class MyTestCase(unittest.TestCase):

    def test_ios_base_config(self):
        config_generator = ConfigGenerator()
        config_generator.set_template("ios_base_node")
        config_generator.set_output_file("../output/test_ios_base_node.txt")
        config_generator.set_facts(data_ios_base_node)

        result = config_generator.to_stdout()

        self.assertIsInstance(result, str)

        self.assertEqual(config_generator.facts.get("hostname"), "BITS-TEST")
        self.assertEqual(config_generator.facts.get("management")["link_id"], "loopback0")

    def test_ios_bgp_policy(self):
        config_generator = ConfigGenerator(template_type="ios_bgp_policy",
                                           facts=data_ios_bgp_policy,
                                           output_file="../output/test_ios_bgp_policy.txt")

        result = config_generator.to_stdout()

        self.assertIsInstance(result, str)

        self.assertEqual(config_generator.facts.get("node_type"), "ios")
        self.assertEqual(config_generator.facts.get("policy_name"), "L3VPN_CE1")

    def test_ios_vpls(self):
        config_gen = ConfigGenerator(facts=data_ios_vpls,
                                     template_type="ios_vfi_vpls",
                                     output_file="../output/test_ios_vpls"
                                     )
        result = config_gen.to_stdout()

        self.assertIsInstance(result, str)

        vfi_count = len(config_gen.facts.get("vfis"))
        efp_count = len(config_gen.facts.get("efps"))

        self.assertEqual(vfi_count, 1)
        self.assertEqual(efp_count, 2)


if __name__ == '__main__':
    unittest.main()
