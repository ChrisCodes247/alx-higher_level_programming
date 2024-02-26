#!/usr/bin/python3
"""Model a rectangle."""
from models.base import Base

class Rectangle(Base):
    """Modles a rectangle and inherits from base class.

    Attributes:
        None
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor.

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int)
            y (int)
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property 
        def width(self):
            """Set/get the width of the Rectangle."""
            return (self.__width)

        @property
        def height(self):
            """Set/get the height of the Rectangle."""
            return (self.__height)

        @property
        def x(self):
            """Set/get the x of the Rectangle."""
            return (self.__x)

        @property
        def y(self):
            """Set/get the y of the Rectangle."""
            return (self.__y)

        @width.setter
        def width(self, value):
            self.__width = value

        @height.setter       
        def height(self, value):
            self.__height = value

        @x.setter       
        def x(self, value):
            self.__x = value

        @y.setter
        def y(self, value):
            self.__y = value
