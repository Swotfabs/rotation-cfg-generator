"""These are unittests to test the functions in generate.py"""

from unittest import TestCase
from unittest import main as runTests
import generate


class TestConstructCommandString(TestCase):

    def setUp(self):
        self.command = {"fraglimit": 12}
        self.command_information = {
            "_description": ("If a team reaches this amount "
                             "of won rounds, it wins the map"),
            "priority": 3,
            "string": "fraglimit \"{}\"",

            "default_value": 12
        }
        self.default_attributes = {}

    def test_basic(self):
        command_string = generate.construct_command_string(
            self.command, self.command_information, self.default_attributes)
        self.assertEquals(command_string, "fraglimit 12;")

    def test_default_value(self):
        self.command = {"fraglimit"}
        self.command_information.default_value = 15
        command_string = generate.construct_command_string(
            self.command, self.command_information, self.default_attributes)
        self.assertEquals(command_string, "fraglimit 15;")

    def test_malformed_command(self):
        self.command = "Malformed"
        with self.assertRaises(ValueError) as ve:
            generate.construct_command_string(
                self.command, self.command_information,
                self.default_attributes)

        exception_raised = ve.exception
        self.assertEquals(exception_raised, "command has to be a dictionary")

    def test_malformed_command_information(self):
        self.command_information = "Malformed"
        with self.assertRaises(ValueError) as ve:
            generate.construct_command_string(
                self.command, self.command_information,
                self.default_attributes)

        exception_raised = ve.exception
        self.assertEquals(exception_raised, "command_information has "
                                            "to be a dictionary")

    def test_malformed_default_attributes(self):
        self.default_attributes = "Malformed"
        with self.assertRaises(ValueError) as ve:
            generate.construct_command_string(
                self.command, self.command_information,
                self.default_attributes)

        exception_raised = ve.exception
        self.assertEquals(exception_raised, "default_attributes has "
                                            "to be a dictionary")

    def tearDown(self):
        pass


if __name__ == "__main__":
    runTests()
