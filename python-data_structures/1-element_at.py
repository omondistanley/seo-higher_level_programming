#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        print("None")
    elif idx >= len(my_list):
        print("None")
    else:
        print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)
