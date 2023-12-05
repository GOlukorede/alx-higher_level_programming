#!/usr/bin/python3
"""A function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """A function that returns the list of available attributes and 
       methods of an object
       Args:  obj (object): The object to lookup
    """
    return dir(obj)