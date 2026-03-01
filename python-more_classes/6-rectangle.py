#!/usr/bin/python3
"""
This module defines a Rectangle class that tracks the number of instances.
It provides a shared counter for all created Rectangle objects.
"""


class Rectangle:
    """
    A class that defines a rectangle and tracks how many exist.

    Attributes:
        number_of_instances (int): The number of active Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance and increments the counter.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the private width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with integer and positive validation."""
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
        """Sets height with integer and positive validation."""
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
        """Returns a string representation for recreate via eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Decrements the counter and prints a message upon deletion.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
