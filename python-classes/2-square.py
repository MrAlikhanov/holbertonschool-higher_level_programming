#!/usr/bin/python3
"""
This module defines a Square class with size validation.
It ensures that the size is a positive integer before instantiation.
"""


class Square:
    """
    A class that defines a square by its size.

    Attributes:
        __size (int): The side length of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
