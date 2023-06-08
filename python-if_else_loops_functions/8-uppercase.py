#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) < 123:
            char = ord(str[i]) - 32
        print("{:str[i]}".format(char), end="")
    print()
