#!/usr/bin/python3

"""
Model a rectangle.
"""

class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """
    print_symbol = '#'
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
	"""Check if rects are equal area.
	
	args:
		rect_1 (obj): instance of Rectangle.
		rect_2 (obj): instance of Rectangle.
	
	Return:
		The biggest rect else rect_1.
	"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of a Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of a Rectangle")
        if rect_1.area() > rect_2.area():
            return (rect_1)
        elif rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
	"""Set rectangle attributes to be equal"""
        if (size):
            temp = size
            cls.__width = temp
            cls.__height = size
        return (cls(size, size))

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of a rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a retangle."""
        type(self).number_of_instances -= 1
        print("Bye Rectangle...")
