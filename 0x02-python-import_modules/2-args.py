#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count_arg = len(argv) - 1
    if count_arg == 0:
        print("0 arguments.")
    elif count_arg == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count_arg))

    for i in range(count_arg):
        print("{:d}: {}".format(i + 1, argv[i + 1]))
