#!/usr/bin/python3
"""
This module defines a Square class with size and position validation.
It allows for printing the square at a specific coordinate location.
"""


class Square:
    """
    A class that defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square.
            position (tuple): The (x, y) coordinates for the square's offset.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the private size attribute.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size attribute with type and value validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieves the private position attribute.

        Returns:
            tuple: The current position coordinates.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets position with tuple of 2 positive integers validation.

        Args:
            value (tuple): The (x, y) coordinates.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates and returns the area of the current square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the # character and position offsets.
        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
            return

        # Handle vertical offset (y coordinate)
        if self.__position[1] > 0:
            for y in range(self.__position[1]):
                print("")

        # Handle horizontal offset (x coordinate) and hashtags
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
