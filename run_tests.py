"""Run all of the unittests
"""

import unittest
import tests.test_command_string as test_command_string
import tests.test_map_line as test_map_line

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_command_string))
    suite.addTest(loader.loadTestsFromModule(test_map_line))

    runner = unittest.TextTestRunner(verbosity=3)
    result = runner.run(suite)
