#!/usr/bin/python3

def no_c(my_string):
    final = ""
    for item in my_string:
        if item == 'C' or item == 'c':
            continue
        else:
            final = final + item
    return final
