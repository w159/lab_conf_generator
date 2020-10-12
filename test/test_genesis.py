import unittest
from unittest.mock import  patch
from gcg.core import Genesis, Task, GenesisResults

from test.vars import data_task


# os.chdir("..")

class MyTestCase(unittest.TestCase):

    def test_case_1(self):
        """
        Basic Unit test for the Genesis Object
        """

        genesis = Genesis()

        self.assertIsInstance(genesis, Genesis)
        self.assertIsInstance(genesis.tasks, list)

    def test_case_2(self):
        """
        Tests the Genesis.generate_config_from_task() method.

        """
        genesis = Genesis()

        genesis_result = genesis.generate_config_from_task(
            task=Task(
                data=data_task,
                template_type='ios_base_node',
                name="test_task",
                description="my test task"
            )
        )
        self.assertIsInstance(genesis_result, GenesisResults)
        self.assertEqual(len(genesis_result.task_completed), 1)
        self.assertEqual(len(genesis_result.task_remaining), 0)

        task = genesis_result.task_completed.pop()
        self.assertIsInstance(task.rendered_data, str)
        self.assertEqual(task.is_complete, True)

    def test_case_3(self):
        """
        Tests the Genesis.generate() method.

        """
        genesis = Genesis()

        task = Task(
            data=data_task,
            template_type='ios_base_node',
            name="test_task",
            description="my test task"
        )

        genesis.add_task(task)

        genesis_results = genesis.generate()
        self.assertIsInstance(genesis_results, GenesisResults)
        self.assertEqual(len(genesis.task_completed), 1)
        self.assertEqual(len(genesis_results.task_completed), 1)
        self.assertEqual(len(genesis.task_remaining), 0)
        self.assertEqual(len(genesis_results.task_remaining), 0)

    @patch('gcg.core.boto3.client')
    @patch('gcg.core.open')
    @patch('gcg.core.os')
    def test_case_4(self, client_mock, open_mock, os_mock):
        """
        Tests Genesis.generate_config_from_task(store_aws=True)

        Validates that the method of storing to AWS S3 works.


        """
        genesis = Genesis()

        task = Task(
            data=data_task,
            template_type='ios_base_node',
            name="gcg_unit_test",
            description="my test task"
        )

        genesis_results = genesis.generate_config_from_task(
            task=task,
            lab_name="GCG_UNIT_TEST",
            store_aws=True
        )

        self.assertIsInstance(genesis_results, GenesisResults)
        self.assertEqual(len(genesis_results.task_completed), 1)

    @patch('gcg.core.open')
    def test_case_5(self, mock):
        """
        Tests Genesis.generate_config_from_task(store_local=True)

        Validates that the method of storing locally works.
        """
        genesis = Genesis()

        task = Task(
            data=data_task,
            template_type='ios_base_node',
            name="gcg_unit_test",
            description="my test task"
        )

        genesis_results = genesis.generate_config_from_task(
            task=task,
            lab_name="GCG_UNIT_TEST",
            store_local=True
        )

        self.assertIsInstance(genesis_results, GenesisResults)
        self.assertEqual(len(genesis_results.task_completed), 1)


if __name__ == '__main__':
    unittest.main()
