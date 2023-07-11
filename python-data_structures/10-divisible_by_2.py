#!/usr/bin/python3
"""
    A function that finds all the multiples of 2 in a
    list. The function returns a list with true or false,
    depending on whether the integer at the same position in
    the original list as a multiple of 2 and should be of the
    same size as the original list. Which means the ones that
    are divisible by 2 should evaluate to true then added to the
    list and the rest evaluate to false before being added. """


def divisible_by_2(my_list=[]):
    list = []
    for value in my_list:
        if value % 2 == 0:
            list.append(True)
        else:
            return list
