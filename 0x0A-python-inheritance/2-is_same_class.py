#!/usr/bin/python3
"""
A Module with a function that checks if an object is an instance of a class
"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class"""
    return type(obj) == a_class
