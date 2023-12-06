#!/usr/bin/python3
"""Inheris from baseGeometry"""
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


class Square(Rectangle):
    """Class that calculates the area of a square"""

    def __init__(self, size):
        """Instantiates the size"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Function that returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        """Function that returns the string representation of the square"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
