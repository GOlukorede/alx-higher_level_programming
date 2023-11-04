#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        reversed = my_list[::-1]
        for item in reversed:
            print("{:d}".format(item))
