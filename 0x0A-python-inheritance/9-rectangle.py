#!/usr/bin/python3
"""Inherits from baseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class to define rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        """Function that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Function that returns the string representation of the rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
