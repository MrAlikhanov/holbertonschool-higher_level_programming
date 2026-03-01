#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of, or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from, a class.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        True if the object is an instance or inherited from a_class;
        otherwise False.
    """
    return isinstance(obj, a_class)
