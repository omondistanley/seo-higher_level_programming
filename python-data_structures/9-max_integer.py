#!/usr/bin/python3
""" A function that finds the biggest integer in a
    list, and if empty return none and assume the
    list contains only integers. """


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        my_list.sort()
        largestInt = my_list[-1]
        return largestInt
