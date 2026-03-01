#!/usr/bin/python3
"""
#Resul Shafili
#8-rectangle.py
I created class Reactangle and worked some integer values
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class for Rectangle which one is inherited by BaseGeometry
    """
    def __init__(self, width, height):
        """
        this function gives integer values only
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
