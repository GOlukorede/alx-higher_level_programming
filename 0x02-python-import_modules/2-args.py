#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    # Function to add two numbers
    argc = len(sys.argv) - 1
    argv = sys.argv[1:]

    if (argc == 0):
        print("{} arguments.".format(argc))
    elif (argc == 1):
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, argv[0]))
    else:
        print("{} arguments:".format(argc))
        for i in range(argc):
            print("{}: {}".format(i + 1, argv[i]))
