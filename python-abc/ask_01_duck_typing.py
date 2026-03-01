#!/usr/bin/python3
"""
This module defines a Shape abstract class and its subclasses.
It demonstrates Duck Typing through a shape_info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract Base Class for shapes.
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate perimeter.
        """
        pass


class Circle(Shape):
    """
    Circle class inheriting from Shape.
    """

    def __init__(self, radius):
        """
        Initializes Circle with a radius.
        """
        self.radius = radius

    def area(self):
        """
        Returns the area of the circle using math.pi.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Returns the perimeter of the circle using math.pi.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape.
    """

    def __init__(self, width, height):
        """
        Initializes Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints area and perimeter using Duck Typing.
    No type checking is performed here.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
