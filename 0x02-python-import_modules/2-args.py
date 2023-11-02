#!/usr/bin/python3
import sys

if __name__ == "__main__": 
    argc = len(sys.argv) - 1
    argv = sys.argv[1:]

    if (argc == 0):
      print("{} arguments.".format(argc))
    elif (argc > 0):
      print("{} argument:".format(argc))
      for i in range(argc):
        print("{}: {}".format(i + 1, argv[i]))
