#!/usr/bin/python3

def fizzbuzz():
    for numbs in range(1, 101):
        if numbs % 3 == 0 and numbs % 5 == 0:
            print("FizzBuzz ", end="")
        elif numbs % 3 == 0:
            print("Fizz ", end="")
        elif numbs % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(numbs), end="")
