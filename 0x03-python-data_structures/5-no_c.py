#!/usr/bin/python3

if __name__ == "__main__":

    def no_c(my_string):
        final = ""
        for item in my_string:
            if item == 'C' or item == 'c':
                continue
            else:
                final = final + item
        return final
