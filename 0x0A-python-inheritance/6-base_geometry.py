#!/usr/bin/python3
"""
A module that contains class BaseGeometry
"""


class BaseGeometry:
    """A class that raises an exception when called"""""
    def area(self):
        """Function that raises an exception when called"""
        raise Exception("area() is not implemented")
