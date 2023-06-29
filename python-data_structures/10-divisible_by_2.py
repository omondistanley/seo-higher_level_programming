#!/usr/bin/python3
"""
    A function that finds all the multiples of 2 in a
    list. The function returns a list with true or false,
    depending on whether the integer at the same position in
    the original list as a multiple of 2 and should be of the
    same size as the original list. """


def divisble_by_2(my_list=[]):
    list = []
    for value in my_list:
        list.append(value % 2 == 0)
    return list
        
