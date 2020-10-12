import unittest

# Load Test Modules
from test import (
    test_task,
    test_genesis
)

# Creates loader and empty test suite.
loader = unittest.TestLoader()
suite = unittest.TestSuite()


def load_tests():
    suite.addTests(loader.loadTestsFromModule(test_task))
    suite.addTests(loader.loadTestsFromModule(test_genesis))


def run_tests():
    runner = unittest.TextTestRunner(verbosity=1)
    runner.run(suite)


if __name__ == "__main__":
    load_tests()
    run_tests()
