
#!/usr/bin/python3

class Square:
    """This is representation of a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """The class constructor.

        Args:
            position (:obj:'tuple'): The position of the square.
            size (int): The size of the square.

        """

        self.__position = position

        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Args:
        Returns:
            int: The value of the square size.
        
        """

        return self.__size ** 2

    @property
    def size(self):
        """The size(self) property.

        Since the size is private, the setter has an arg(value)
        that changes the value of the size.

        """

        return self._size(self)

    @size.setter
    def size (self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property 
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(n, int) for n in value) or not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """This prints the square in a formated manner.

        Returns:
            formatted square using "#".

        """

        if self.__size == 0:
            print()

        for i in range(self.__position[1]):
            print()

        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


    def __str__(self):
        """Behaves same as my_print."""

        if self.__size == 0:
            return ""

        lines = []

        for i in range(self.__position[1]):
            lines.append("")

        for i in range(self.__size):
            line = " " * self.__position[0] + "#" * self.__size
            lines.append(line)

        return "\n".join(lines)
