#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if "{:d}".format(value):
            print("{:d}".format(value))
            return True
    except ValueError:
        return False
