#!/usr/bin/python3
"""
A module that contains class BaseGeometry
"""


class BaseGeometry:
    """A class that raises an exception when called"""""
    def area(self):
        """Function that raises an exception when called"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Function that validates an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
