import unittest
import json
from lcg.core import GCG, GeneratorTask, GCGValidationError
from test.helpers import open_json_file
from marshmallow import Schema

TEST_DATA_DIR = 'data'


class GCGTestCase(unittest.TestCase):

    def test_case_1(self):
        """
        Basic test of the GenesisConfigurationGenerator

        """
        cg = GCG()

        self.assertIsInstance(cg.tasks, list)

    def test_case_2(self):
        """
        Tests the add task functionality

        """
        config_generator = GCG()

        data = open_json_file('r1.json')

        task_1 = GeneratorTask.new(data=data)
        self.assertTrue(config_generator.add_task(task_1))

        with self.assertRaises(TypeError):
            bad_task = object()
            self.assertFalse(config_generator.add_task(bad_task))

        self.assertEqual(len(config_generator.tasks), 1)

    def test_case_3(self):
        """
        Tests the CGC.generate() method.

        """
        config_generator = GCG()

        data = open_json_file('r1.json')

        task_1 = GeneratorTask.new(data=data, name="R1_BASE_CONFIG")
        task_2 = GeneratorTask.new(data=data, name="R1_BASE_CONFIG_2")

        config_generator.add_task(task_1)
        config_generator.add_task(task_2)

        results = config_generator.generate()
        self.assertIsInstance(results, dict)

        for task in config_generator.tasks:
            self.assertTrue(task.is_complete)
            self.assertIsInstance(task.rendered_data, str)


class GeneratorTaskTestCase(unittest.TestCase):
    IOS_CONFIG = {
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

    def test_case_1(self):
        '''
        Test for basic object creation with property validation

        '''

        with open(f'{TEST_DATA_DIR}/r1.json') as file:
            data = json.load(file)
        self.assertIsInstance(data, dict)

        task_1 = GeneratorTask(data=data)

        self.assertIsInstance(task_1, GeneratorTask)
        self.assertEqual(task_1.template_type, 'ios_base_node')
        self.assertIsInstance(task_1._schema, Schema)
        self.assertTrue(".j2" in task_1._template_file_name)

        with self.assertRaises(GCGValidationError):
            del data['template_type']
            GeneratorTask.new(data=data)

    def test_case_2(self):
        """
        Tests creation with GeneratorTask.new() funtion.
        """
        with open(f'{TEST_DATA_DIR}/r1.json') as file:
            data = json.load(file)
        self.assertIsInstance(data, dict)

        task_1 = GeneratorTask.new(data=data)

        self.assertIsInstance(task_1, GeneratorTask)
        self.assertEqual(task_1.template_type, 'ios_base_node')
        self.assertIsInstance(task_1._schema, Schema)
        self.assertTrue(".j2" in task_1._template_file_name)
        self.assertFalse(task_1.is_complete)

    def test_case_3(self):
        """
        Test the GeneratorTask.validate() method for execution.

        """
        with open(f'{TEST_DATA_DIR}/r1.json') as file:
            data = json.load(file)
        self.assertIsInstance(data, dict)

        task_1 = GeneratorTask.new(data=data)
        self.assertTrue(task_1.validate())

        with self.assertRaises(GCGValidationError):
            task_2 = GeneratorTask.new(data={'data': 'bad_data'})

    def test_case_4(self):
        """
        Test the GeneratorTask.template_types returns the correct type.

        """

        self.assertIsInstance(GeneratorTask.template_types(), list)
        self.assertGreater(len(GeneratorTask.template_types()), 1)


if __name__ == '__main__':
    unittest.main()
