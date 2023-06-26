#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argscon = len(sys.argv) - 1

    if argscon == 0:
        print("0 arguments.")
    elif argscon == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(argscon))
    for q in range(argscon):
        print("{}: {}".format(q + 1, sys.argv[q + 1]))
