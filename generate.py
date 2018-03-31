"""This runs the script to create a rotations.cfg file that
can be copied to the end of your server.cfg"""


def load(path):
    """This loads all of the information found in rotation.json
    into a python object"""
    return None


def create_command_string(command, command_information, default_attributes):
    """This takes creates the command string that will go in the .cfg

    Arguments:
    command: a python dictionary of the command to create and its value.
        This is found in
            rotations.profiles.__profile__name.map[index].<command>
    command_information: a python dictionary of the information of the command.
        This is found in
            rotations.commands.<command>
    default_attributes: a python dictionary of the default attributes
        of every command.
        This is found in
            rotations.commands.default_attributes
    """
    return None


def create_map_line(index, shorthand, commands):
    """This creates the string correstponding to a map.

    index: The index of where we are in the rotation
    shorthand: the shorthand of the rotation profile we are working with
    commands: a list of python dictionaries containing the priority of
        the command and the command string.
    """
    return None


def create_file(path):
    """ This creates rotations.cfg which you can append to your server.cfg
    Note it will OVERWRITE andy rotations.cfg already in the folder
    specificed by path"""
    pass


def append_line(file):
    """This takes in a python file object and appends a line to it"""
    pass


def main():
    """This is simply the main function that wraps everythign else"""
    pass


if __name__ == "__main__":
    main()
else:
    raise NotImplementedError(
        "This script is not meant to be imported as a module")
