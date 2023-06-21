#!/usr/bin/python3
for numbs in range(0, 100):
    if numbs == 99:
        print("{}".format(numbs))
    else:
        print("{:02}".format(numbs), end=", ")
