#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
Tld = abs(number) % 10
if number < 0:
    Tld = -Tld
print(f"Last digit of {number:d} is {Tld:d} and is ", end="")
if Tld > 5:
    print("greater than 5")
elif Tld == 0:
    print("0")
else:
    print("less than 6 and not 0")
