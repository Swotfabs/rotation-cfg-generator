"""Run all of the unittests
"""

import unittest
import tests.test_command_string as test_command_string

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_command_string))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
