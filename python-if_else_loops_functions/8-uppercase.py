#!/usr/bin/python3
def uppercase(str):
    for c in str:
        chr = ord(c)
        if ord(c) >= 97 and ord(c) < 123:
            char = ord(i) - 32
        print("{:c}".format(char), end="")
    print()
