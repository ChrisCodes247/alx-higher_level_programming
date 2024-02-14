#!/usr/bin/python3
"""
A function to add two integers.
"""

def add_integer(a, b = 98):
    """Adds two variables which are integers.

    Args:
        a (int)
        b (int)

    Returns: the result of the addition.
    """

    if isinstance (a, str):
        raise TypeError("a must be an integer")
    elif isinstance(b, str):
        raise TypeError("b must be an integer")
    elif isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    elif a == None:
        raise TypeError("a must be an integer")
    elif b == None:
        raise TypeError("b must be an integer")
    else:
        result = a + b
    result = a + b
    return (result)
