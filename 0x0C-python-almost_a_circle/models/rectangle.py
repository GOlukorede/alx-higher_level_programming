#!/usr/bin/python3
"""The Rectangle module"""
from models.base import Base

class Rectangle(Base):
    """The Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self):
        """Gets the value of width"""
        return self.__width

    @property
    def height(self):
        """Gets the value of height"""
        return self.__height

    @property
    def x(self):
        """Gets the value of x"""
        return self.__x

    @property
    def y(self):
        """Gets the value of y"""
        return self.__y

    @width.setter
    def width(self, value):
        """Set the  value of width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the  value of height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """Set the  value of x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """Set the  value of y"""
        self.__y = value
