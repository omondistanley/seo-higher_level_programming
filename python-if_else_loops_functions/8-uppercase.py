#!/usr/bin/python3
def uppercase(str):
    for i in str:
        chr = ord(i)
        if ord(i) >= 97 and ord(i) < 123:
            char = ord(i) - 32
        print("{:i}".format(char), end="")
    print()
