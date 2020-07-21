import unittest
from lcg.schemas import (
    BaseNode,
    BaseInterface,
    IPv4Addr
)


class MyTestCase(unittest.TestCase):
    def test_schema_base_node_case_1(self):
        data = {
            "node_type": "",
            "hostname": "",
            "template_type": "",
            "domain": ""
        }
        schema = BaseNode()
        results = schema.validate(data)
        self.assertIsInstance(results, dict)

    def test_schema_base_node_case_2(self):
        """
        Test for BaseNode for missing required parameters
        """
        data = {
            "node_type": "",

        }
        schema = BaseNode()
        results = schema.validate(data)

        self.assertIsInstance(results, dict)
        self.assertEqual(len(results), 4)

    def test_schema_base_interface_case_1(self):
        data = {
            "link_id": "Gi0/0",
            "dot1q": "100",
            "is_mgmt": True,
            "description": "Test Link",
            "bandwidth": "100",

        }
        schema = BaseInterface()
        results = schema.validate(data)
        self.assertIsInstance(results, dict)

    def test_schema_base_interface_case_2(self):
        """
        Test BaseInteface for missing required parameters
        """
        data = {
            "dot1q": "100",
            "is_mgmt": True,
            "description": "Test Link",
            "bandwidth": "100",

        }
        schema = BaseInterface()
        results = schema.validate(data)
        self.assertIsInstance(results, dict)
        self.assertEqual(len(results), 1)

    def test_schema_ipv4_addr_case_1(self):
        data = {
            "address": "192.168.1.1",
            "netmask": "255.255.255.0",

        }
        schema = IPv4Addr()
        results = schema.validate(data)
        self.assertIsInstance(results, dict)

    def test_schema_ipv4_addr_case_2(self):
        """
        Test IPV4Addr with bad netmask and ipv4 address
        """
        data = {
            "address": "192.168.1.260",
            "netmask": "255.255.255.260",

        }
        schema = IPv4Addr()

        with self.assertRaises(ValueError):
            schema.validate(data)


if __name__ == '__main__':
    unittest.main()
