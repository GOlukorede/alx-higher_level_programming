#!/usr/bin/python3

if __name__ == "__main__": 
    import sys

    argc = len(sys.argv) - 1
    argv = sys.argv[1:]
    sum = 0
    for i in range(len(argv)):
        sum = sum + int(argv[i])
    print(sum)
