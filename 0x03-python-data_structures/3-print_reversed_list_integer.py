#!/usr/bin/python3

if __name__ == "__main__":

    def print_reversed_list_integer(my_list=[]):
        """
        Prints the list in reversed order
        """
        reversed = my_list[::-1]
        for item in reversed:
            print("{:d}".format(item))
