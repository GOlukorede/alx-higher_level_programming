#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle
    """

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """retrieves height attribute"""
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value
