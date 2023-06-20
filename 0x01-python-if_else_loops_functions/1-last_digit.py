#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

numsd = 0

if number < 0:
    number = number*-1
    numsd = 1
    Tld = number % 10
if numsd == 1:
    number = number*-1
    Tld = Tld*-1
    print(f"The last digit of {number:d} is {Tld:d} and is ", end="")
if Tld > 5:
    print(f"{Tld:d} is greater then 5")
elif Tld == 0:
    print(f"{Tld:d} and is 0")
else:
    print(f"{Tld:d} and is less then 6 and not 0")


