#!/usr/bin/python3
"""Defines a class Base."""

class Base:
    """Definition of Base.
    
    attributes:
        __nb_objects (int): private class attribute to count objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor.

        args:
            id (int): unique id for each instance.
            self:
        """

        if (id != None):
            self.id = id
        else:
            self.id = Base.__nb_objects + 1
            Base.__nb_objects += 1
