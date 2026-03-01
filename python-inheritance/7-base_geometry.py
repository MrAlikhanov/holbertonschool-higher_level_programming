#!/usr/bin/python3
"""
this is base  geometry
"""


class BaseGeometry:
    """
    this class is for geometry
    """
    def area(self):
        """
        This function gives area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        this area validates integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
