#!/usr/bin/python3
"""
This module defines a Rectangle class with a customizable print symbol.
"""


class Rectangle:
    """
    A class that defines a rectangle by its dimensions and print symbol.

    Attributes:
        number_of_instances (int): Total count of active instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle and increments instance count."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns the rectangle printed with print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        # Use str() on print_symbol to handle non-string types like lists
        line = str(self.print_symbol) * self.__width
        rect = [line for _ in range(self.__height)]
        return "\n".join(rect)

    def __repr__(self):
        """Returns string for eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Decrements instance count and prints deletion message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
