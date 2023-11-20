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
        if result is None:
            print("Inside result: {}".format(None))
        else:
            print("Inside result: {:.1f}".format(div))
        return result
