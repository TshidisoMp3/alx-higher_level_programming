#!/usr/bin/python3

for numbs1 in range(0, 10):
    for numbs2 in range(numbs1 + 1, 10):
        if numbs1 == 8 and numbs2 == 9:
            print("{}{}".format(numbs1, numbs2))
        else:
            print("{}{}".format(numbs1, numbs2), end=", ")
