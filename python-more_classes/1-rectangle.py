#!/usr/bin/python3
"""
Class rectangle
"""


class Rectangle:
    """represents Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Creates rectangle object
        Args:
            width (int):
            height (int):
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """This is Getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """This is setter for Width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """This is Getter height."""
        return self.__height

    @height.setter
    def height(self, value):
        """This is setter for Height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
