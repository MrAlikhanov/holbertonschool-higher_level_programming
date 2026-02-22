#!/usr/bin/python3
"""
This module contains a function that adds two numbers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    Raises a TypeError if a or b are not integers or floats.
    Casts floats to integers before adding.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
