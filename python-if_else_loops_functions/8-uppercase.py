#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            chr = ord(str[i]) - 32
        print("{:str[i]}".format(chr), end="")
    print()
