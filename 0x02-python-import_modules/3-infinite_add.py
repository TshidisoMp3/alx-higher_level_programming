#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    ans = 0
    for d in range(len(sys.argv) - 1):
        ans += int(sys.argv[d + 1])
    print("{}".format(ans))
