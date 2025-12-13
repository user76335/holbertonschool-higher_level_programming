#!/usr/bin/python3
"""Defines a class Square that handles size and position."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
            position (tuple): The position offset of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size < 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation.

        Args:
            value (int): New size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with validation.

        Args:
            value (tuple): New position.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # at the specified position.

        If size is 0: print empty line.
        """
        if self.__size == 0:
            print("")
            return

        # Vertical offset (position[1])
        for _ in range(self.__position[1]):
            print("")

        # Print each row
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
