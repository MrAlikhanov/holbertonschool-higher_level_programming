#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
This is the second step in building a robust Square class.
"""


class Square:
    """
    A class that defines a square by its size.
    The size is kept private to ensure data encapsulation.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the side of the square.
        """
        self.__size = size
