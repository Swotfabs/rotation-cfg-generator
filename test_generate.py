"""These are unittests to test the functions in generate.py"""

from unittest import TestCase
from unittest import main as runTests
import generate


class TestConstructCommandString(TestCase):

    def setUp(self):
        self.command = {"fraglimit": 12}
        self.command_information = {
            "fraglimit":
            {
                "_description": ("If a team reaches this amount "
                                 "of won rounds, it wins the map"),
                "priority": 3,
                "string": "fraglimit \"{}\""
            }
        }
        self.default_attributes = {}
        self.default_value = 12

    def test_basic(self):
        command_string = generate.construct_command_string(
            self.command, self.command_information, self.default_attributes,
            self.default_value)
        self.assertEqual(command_string, "fraglimit 12")

    def test_default_value(self):
        self.command = {"fraglimit"}
        self.default_value = 15
        command_string = generate.construct_command_string(
            self.command, self.command_information, self.default_attributes,
            self.default_value)
        self.assertEqual(command_string, "fraglimit 15")

    def test_mbmode(self):
        self.command = {"map": "mb2_corellia", "mbmode": "0"}
        self.command_information = {
            "map":
            {
                "_description": "Changes the map",
                "priority": 1,
                "string": "map \"{}\""
            },
            "mbmode":
            {
                "_description": ("In conjuntion with g_authenticity changes "
                                 "the mode of the game (Open, Semi-FA, FA)"),
                "_note": "This will be used instead of the map command",
                "priority": 2,
                "string": "mbmode \"{}\" \"{}\""
            }
        }
        self.default = 0
        command_string = generate.construct_command_string(
            self.command, self.command_information, self.default_attributes,
            self.default_value)
        self.assertEquals(command_string, "mbmode 0 mb2_corellia")

    def test_malformed_command(self):
        self.command = "Malformed"
        with self.assertRaises(ValueError) as ve:
            generate.construct_command_string(
                self.command, self.command_information,
                self.default_attributes, self.default_value)

        exception_raised = ve.exception
        self.assertEqual(exception_raised, "command has to be a dictionary")

    def test_malformed_command_information(self):
        self.command_information = "Malformed"
        with self.assertRaises(ValueError) as ve:
            generate.construct_command_string(
                self.command, self.command_information,
                self.default_attributes, self.default_value)

        exception_raised = ve.exception
        self.assertEqual(exception_raised, "command_information has "
                         "to be a dictionary")

    def test_malformed_default_attributes(self):
        self.default_attributes = "Malformed"
        with self.assertRaises(ValueError) as ve:
            generate.construct_command_string(
                self.command, self.command_information,
                self.default_attributes, self.default_value)

        exception_raised = ve.exception
        self.assertEqual(exception_raised, "default_attributes has "
                         "to be a dictionary")

    def test_malformed_default_value(self):
        # This only tests whether the default value is not a string
        # Further testing of other types might be needed
        self.default_value = "Malformed"
        with self.assertRaises(ValueError) as ve:
            generate.construct_command_string(
                self.command, self.command_information,
                self.default_attributes, self.default_value)

        exception_raised = ve.exception
        self.assertEqual(exception_raised, "default_value has "
                         "to be a number")

    def tearDown(self):
        pass


if __name__ == "__main__":
    runTests()
