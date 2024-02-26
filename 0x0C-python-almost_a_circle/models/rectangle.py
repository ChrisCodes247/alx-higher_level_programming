#!/usr/bin/python3
"""Model a rectangle."""

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
        super().__init__.(id)

        @property
        """width getter method."""
        def width(self):
            return (self.__width)

        @property
        """height getter"""
        def height(self):
            return (self.__height)

        @property
        """x getter method."""
        def x(self):
            return (self.__x)

        @property
        """y getter."""
        def y(self):
            return (self.__y)

        @width.setter
        """Width setter.

        Args:
            value (int): width will be set to this value
        """
        def width(self, value):
            self.__width = value

        @height.setter
        """height setter.

        Args:
            value (int): height will be set to this value
        """

        def height(self, value):
            self.__height = value

        @x.setter
        """x setter.

        Args:
            value (int): x will be set to this value
        """

        def x(self, value):
            self.__x = value

        @y.setter
        """y setter.

        Args:
            value (int): y will be set to this value
        """

        def y(self, value):
            self.__y = value
