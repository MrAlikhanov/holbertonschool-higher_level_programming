#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
It includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    A subclass of the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending sorted order.
        Assumes all elements in the list are integers.
        """
        print(sorted(self))
