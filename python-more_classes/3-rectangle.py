#!/usr/bin/python3
"""
This module defines a Rectangle class with area and perimeter methods.
It ensures that the rectangle can calculate its own metrics.
"""


class Rectangle:
    """
    A class that defines a rectangle by its width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        Args:
            width (int): The horizontal dimension.
            height (int): The vertical dimension.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with integer and positive validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with integer and positive validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The product of width and height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.

        Returns:
            int: The sum of all sides, or 0 if a dimension is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
