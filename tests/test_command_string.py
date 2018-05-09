"""These are unittests to test the functions in generate.py"""

from unittest import TestCase
import generate_cfg


class TestConstructCommandString(TestCase):

    def setUp(self):
        self.command = {"fraglimit": 12}
        self.command_information = {
            "fraglimit":
            {
                "_description": ("If a team reaches this amount "
                                 "of won rounds, it wins the map"),
                "priority": 3,
                "string": "fraglimit {}"
            }
        }
        self.mbmode_information = {
            "map":
            {
                "_description": "Changes the map",
                "priority": 1,
                "string": "map {}"
            },
            "mbmode":
            {
                "_description": ("In conjuntion with g_authenticity changes "
                                 "the mode of the game (Open, Semi-FA, FA)"),
                "_note": "This will be used instead of the map command",
                "priority": 2,
                "string": "mbmode {} {}"
            }
        }
        self.default_value = 12

    def test_basic(self):
        command_string = generate_cfg.construct_command_string(
            self.command, self.command_information, self.default_value)
        self.assertEqual(command_string, "fraglimit 12")

    def test_default_value(self):
        self.command = {"fraglimit": None}
        self.default_value = 15
        command_string = generate_cfg.construct_command_string(
            self.command, self.command_information, self.default_value)
        self.assertEqual(command_string, "fraglimit 15")

    def test_mbmode(self):
        self.command = {"map": "mb2_corellia", "mbmode": 0}
        self.command_information = self.mbmode_information
        self.default_value = {"map": "mb2_corellia", "mbmode": 0}
        command_string = generate_cfg.construct_command_string(
            self.command, self.command_information, self.default_value)
        self.assertEqual(command_string, "mbmode 0 mb2_corellia")

    def test_mbmode_default_mode(self):
        self.command = {"map": "mb2_corellia", "mbmode": None}
        self.command_information = self.mbmode_information
        self.default_value = {"map": "mb2_corellia", "mbmode": 0}
        command_string = generate_cfg.construct_command_string(
            self.command, self.command_information, self.default_value)
        self.assertEqual(command_string, "mbmode 0 mb2_corellia")

    def test_mbmode_default_map(self):
        self.command = {"map": None, "mbmode": 0}
        self.command_information = self.mbmode_information
        self.default_value = {"map": "mb2_corellia", "mbmode": 0}
        command_string = generate_cfg.construct_command_string(
            self.command, self.command_information, self.default_value)
        self.assertEqual(command_string, "mbmode 0 mb2_corellia")

    def test_mbmode_default_both(self):
        self.command = {"map": None, "mbmode": None}
        self.command_information = self.mbmode_information
        self.default_value = {"map": "mb2_corellia", "mbmode": 0}
        command_string = generate_cfg.construct_command_string(
            self.command, self.command_information, self.default_value)
        self.assertEqual(command_string, "mbmode 0 mb2_corellia")

    def test_mbmode_no_map(self):
        self.command = {"mbmode": 0}
        self.command_information = self.mbmode_information
        self.default_value = {"map": "mb2_corellia", "mbmode": 0}
        with self.assertRaises(ValueError) as ve:
            generate_cfg.construct_command_string(
                self.command, self.command_information, self.default_value)

        exception_raised = ve.exception
        self.assertEqual(str(exception_raised),
                         "mbmode needs a map")

    def test_malformed_command(self):
        self.command = "Malformed"
        with self.assertRaises(TypeError) as ve:
            generate_cfg.construct_command_string(
                self.command, self.command_information, self.default_value)

        exception_raised = ve.exception
        self.assertEqual(str(exception_raised),
                         "command has to be a dictionary")

    def test_malformed_command_information(self):
        self.command_information = "Malformed"
        with self.assertRaises(TypeError) as ve:
            generate_cfg.construct_command_string(
                self.command, self.command_information, self.default_value)

        exception_raised = ve.exception
        self.assertEqual(str(exception_raised), "command_information has "
                         "to be a dictionary")

    def test_too_many_commands(self):
        self.command = {"roundlimit": 12, "fraglimit": 15}
        with self.assertRaises(TypeError) as ve:
            generate_cfg.construct_command_string(
                self.command, self.command_information, self.default_value)

        exception_raised = ve.exception
        self.assertIn("Too many commands", str(exception_raised))

    def tearDown(self):
        pass


if __name__ == "__main__":
    """This script can not be run directly as it requires something from its
    parent directory
    """
    pass
