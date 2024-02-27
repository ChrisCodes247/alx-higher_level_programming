#!/usr/bin/python3
"""Class square that inherits from Rectangle."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Models a Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor.

        Args:
            size (int): size of the square
            x (int): the x coordinate of the square
            y (int): the y coordinate of the square
            id (int): unique counter for class objects

        """
        super().__init__(id, x, y, width, height)

    def __str__(self):
    """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                             self.width)
