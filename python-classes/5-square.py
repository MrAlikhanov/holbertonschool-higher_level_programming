#!/usr/bin/python3
"""
This module defines a Square class that can print its visual representation.
It builds on previous tasks to add a public printing method.
"""


class Square:
    """
    A class that defines a square by its size and provides a print method.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the private size attribute of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size attribute with strict type and value validation.

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

    def area(self):
        """
        Calculates and returns the area of the current square.

        Returns:
            int: The area (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square in the stdout using the # character.
        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
