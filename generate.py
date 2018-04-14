"""This runs the script to create a rotations.cfg file that
can be copied to the end of your server.cfg"""


def load(path):
    """This loads all of the information found in rotation.json
    into a python object"""
    return None


def construct_command_string(command, command_information, default_attributes):
    """This takes creates the string that represents a command and returns it

    Arguments:
    command: a python dictionary of the command to create and its value.
        This is found in
            rotations.profiles.__profile__name.map[index].<command>
        Ex: {"fraglimit": 12}
    command_information: a python dictionary of the information of the command.
        This is found in
            rotations.commands.<command>
    default_attributes: a python dictionary of the default attributes
        of every command.
        This is found in
            rotations.defaults.default_attributes
    """
    return None


def construct_map_line(profile, map_index):
    """This creates the string representing a map and returns it

    profile: What profile we are working with
        This is __profile__name for rotations.profiles.__profile__name
        Example: "large"
    map_index: The index of where we are in the rotation
        This is the index for rotations.profiles.__profile__name.map[index]
    """
    return None


def construct_profile_line(profile):
    """ This creates the line giving the profile information and returns it

    profile: What profile we are working with
        This is __profile__name for rotations.profiles.__profile__name
    """
    return None


def create_file(path):
    """ This creates rotations.cfg which you can append to your server.cfg
    Note it will OVERWRITE and rotations.cfg already in the folder
    specificed by path
    """
    pass


def append_line(file):
    """This takes in a python file object and appends a line to it"""
    pass


def main():
    """This is simply the main function that wraps everythign else"""
    pass


if __name__ == "__main__":
    main()
