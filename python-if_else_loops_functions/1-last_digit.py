#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstDigit = abs(number) % 10
if number < 0:
    lstDigit = -lstDigit
if lstDigit > 5:
    print(f"Last digit of {number} is {lstDigit} and is greater than 5")
elif lstDigit == 0:
    print(f"Last digit of {number} is {lstDigit} and is 0")
elif lstDigit < 6:
    print(f"Last digit of {number} is {lstDigit} and is less than 6 and not 0")
