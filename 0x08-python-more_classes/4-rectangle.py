#!/usr/bin/python3
"""
A class Rectangle that defines a rectangle
"""


class Rectangle():
    """
    A class that defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Width setter
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Height setter
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        if self.width or self.height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    def __str__(self):
        """
        Returns a string representation of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle = ""
        for column in range(self.height):
            for row in range(self.width):
                rectangle += "#"
            if column < self.height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """
        Return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.width, self.height)
