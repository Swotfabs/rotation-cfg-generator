"""This runs the script to create a rotations.cfg file that
can be copied to the end of your server.cfg"""


def load(path):
    """This loads all of the information found in rotation.json
    into a python object"""
    return None


def construct_command_string(command, command_information,
                             default_value):
    """This takes creates the string that represents a command and returns it.
    The string is just the command and the values, it does not
        have the ; that separates them.

    Arguments:
    command: a python dictionary of the command to create and its value.
        This is found in
            [profiles.json] profiles.__profile__name.map[index].<command>
        Ex: {"fraglimit": 12}
    command_information: a python dictionary of the information of the command.
        This is found in
            [command_information.json] commands.__command__
    default_value
        The default value of the command, if it has one.
        This is found in
            [defaults.json] defaults.commands.__command__
    """
    try:
        command.keys()
    except AttributeError as e:
        if "'keys'" in str(e):
            raise TypeError("command has to be a dictionary")
        else:
            raise

    if 'mbmode' in command.keys():
        # mbmode is special
        return command_information['mbmode']['string'].format(
            command['mbmode'], command['map'])

    if len(command.keys()) > 1:
        raise TypeError("Too many commands, {}".format(
            [key for key in command.keys()]))

    command_name, command_value = list(command.items())[0]
    if not command_value:
        command_value = default_value
    try:
        return command_information[command_name]['string'].format(
            command_value)
    except Exception:
        raise TypeError("command_information has to be a dictionary")


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
