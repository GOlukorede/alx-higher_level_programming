#!/usr/bin/python3

if __name__ == "__main__":
    """Function that replaces an element in a list at a specific position without\
modifying the original list"""

    def new_in_list(my_list, idx, element):
        if (idx < 0):
            return my_list
        if (idx > len(my_list)):
            return my_list
        return my_list[:idx] + [element] + my_list[idx + 1:]
