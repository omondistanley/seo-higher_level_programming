#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        copiedList = my_list.copy()
    if idx < 0:
        return (copiedList)
    elif idx >= my_list:
        return (copiedList)
    else:
        copiedList[idx] = element
        return (copiedList)
        return (my_list)
