#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """Prints first and last name.

    Args:
        first_name (str)
        last_name (str)

    Returns:
        formatted output
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("Last_name must be a string")

    result = print("My name is {} {}".format(first_name, last_name))
    return (result)
