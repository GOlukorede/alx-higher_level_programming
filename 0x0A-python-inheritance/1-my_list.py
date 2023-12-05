#!/usr/bin/python3
"""A Module that inherits from list superclass"""


class MyList(list):
    """A class MyList that inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
