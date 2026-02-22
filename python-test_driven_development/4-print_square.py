#!/usr/bin/python3
"""
This module contains a function that prints a square with #.
"""


def print_square(size):
    """
    Prints a square with the character #.
    Size is the length of the side of the square.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        if isinstance(size, float):
            size = int(size)
        else:
            raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
