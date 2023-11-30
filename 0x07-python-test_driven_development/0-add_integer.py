#!/usr/bin/python3
"""Module to add two integers or floats"""

def add_integer(a, b=98):
    """
    Function to add two integers or floats:

    Parameters:
    a (int or float) First integer or float
    b (int or float) Second integer or float(optional)

    Returns:
    int: (Addition of a and b)

    Raises:
    TypeError: if a is not an integer or float
    TypeError: if b is not an integer or float
    """
    if isinstance(a, (int, float)) is False:
        raise TypeError("a must be an integer or float")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
