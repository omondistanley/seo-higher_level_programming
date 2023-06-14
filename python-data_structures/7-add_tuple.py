#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) == 0:
        element1, element2 = (0, 0)
    elif len(tuple_a) == 1:
        element1 = tuple_a[0]
        element2 = 0
    else:
        element1 = tuple_a[0]
        element2 = tuple_a[1]
    if len(tuple_b) == 0:
        element3, element4 = (0,0)
    elif len(tuple_b) == 1:
        element3 = tuple_b[0]
        element4 = 0
    else:
        element3 = tuple_b[0]
        element4 = tuple_b[1]
    sumTuple = (element1 + element3, element2 + element4)
    print(sumTuple)
