import unittest

from gcg.core import Task, GCGValidationError
from marshmallow import Schema
from test.vars import (
    data_task
)


class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        """
        Basic Unit test for gcg.core.Task object.

        """

        task = Task(
            data=data_task,
            template_type='ios_base_node',
            name="test_task",
            description="my test task"
        )

        self.assertIsInstance(task, Task)

        # Test object public properties
        self.assertEqual(task.data, data_task)
        self.assertEqual(task.template_type, 'ios_base_node')
        self.assertEqual(task.name, 'test_task')
        self.assertEqual(task.description, 'my test task')
        self.assertEqual(task.is_complete, False)

        # test object private properties
        self.assertIsInstance(task._schema, Schema)

        # Exceptions or Errors
        with self.assertRaises(GCGValidationError):
            Task(
                name='bad_task',
                template_type='bad_type',
                data={}
            )



    def test_case_2(self):
        """
        Tests methods associated with the Task object.

        """
        task = Task(
            data=data_task,
            template_type='ios_base_node',
            name="test_task",
            description="my test task"
        )

        # Method Tests
        self.assertTrue(task.validate())
        self.assertTrue(task.validate_data(data_task))

        self.assertIsInstance(task.list_template_types(), list)

if __name__ == '__main__':
    unittest.main()
