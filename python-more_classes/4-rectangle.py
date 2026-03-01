#!/usr/bin/python3
"""
This module defines a Rectangle class with an eval-ready representation.
"""


class Rectangle:
    """
    A class that defines a rectangle by its width and height.
    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the private width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns a string representation of the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rect = [("#" * self.__width) for _ in range(self.__height)]
        return "\n".join(rect)

    def __repr__(self):
        """
        Returns a string representation of the rectangle to be used by eval().
        Format: Rectangle(width, height)
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
