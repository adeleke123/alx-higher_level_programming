#!/usr/bin/python3


def say_my_name(first_name, last_name=""):
    """
    Args: Prints My name is <first name> <last name>.
        :param last_name: <first name> (must be strings),
        :param first_name: <last name> (must be strings).

    Raises:
    TypeError - if not a string.
    """
    if type(first_name) != str:
        raise TypeError("first name must be a string")
    if type(last_name) != str:
        raise TypeError("last name must be a string")
    print("My name is {} {}".format(first_name, last_name))
