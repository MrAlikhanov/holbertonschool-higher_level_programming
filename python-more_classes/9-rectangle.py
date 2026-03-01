#!/usr/bin/python3
"""
This module defines a Rectangle class with a class method to create squares.
"""


class Rectangle:
    """
    A class that defines a rectangle and tracks its lifecycle.

    Attributes:
        number_of_instances (int): Shared counter for active instances.
        print_symbol (any): Symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new instance and increments the counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width with type and value validation."""
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
        """Sets height with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        rect = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(rect)

    def __repr__(self):
        """Returns string for recreation via eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Decrements counter and prints deletion message."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles based on their area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size.

        Args:
            size (int): The dimension for both sides of the new rectangle.

        Returns:
            Rectangle: A new instance of the class.
        """
        return cls(size, size)
