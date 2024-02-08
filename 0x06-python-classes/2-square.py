#!/usr/bin/python3

"""Define a class Square"""

class Square:
    """Model a square."""

    def __init__(self, size):
        """Initializes a new square.

        Args:
            size (int): The size of the new square.
        """

        self.__size = size

        if size != type(int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
