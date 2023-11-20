#!/usr/bin/python3

def safe_print_division(a, b):
    div = 0
    result = None
    try:
        div = int(a / b)
        result = "{:.1f}".format(div)
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {:d}".format(div))
        return result
