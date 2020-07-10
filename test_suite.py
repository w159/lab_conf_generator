import unittest

# Load Test Modules
from test import (
  test_config_gen
)

# Creates loader and empty test suite.
loader = unittest.TestLoader()
suite = unittest.TestSuite()


def load_tests():
    suite.addTests(loader.loadTestsFromModule(test_config_gen))


def run_tests():
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    load_tests()
    run_tests()
