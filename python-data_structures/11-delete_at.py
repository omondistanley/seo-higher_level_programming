#!/usr/bin/python3
"""
    deleting an item at a given index in a list.
"""


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list.remove(my_list[idx])
        return my_list
