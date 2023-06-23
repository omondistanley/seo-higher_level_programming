#!/usr/bin/python3
""" The add tuple class, adding two integers in the two
    tuples, the tuples must have integers and if smaller
    than 2, use 0 for each missing integer and the first
    two if the tuple if bigger than the two tuples. """

def add_tuple(tuple_a=(), tuple_b=()):
    # check the length of the tuples:
    # 1. If the length is 0 set each element to 0
    if len(tuple_a) == 0:
        firstElement, secondElement = (0, 0)
    # 2. if the length is 1 then set an element to the
    #   value.
    elif len(tuple_a) == 1:
        firstElement = tuple_a[0]
        secondElement = 0
    # 3. if the length is 2 or greater set the values to
    # be the elements.
    else:
        firstElement = tuple_a[0]
        secondElement = tuple_a[1]
    # second tuple.
    if len(tuple_b) == 2:
        thirdElement = tuple_b[0]
        fourthElement = tuple_b[1]
    elif len(tuple_b) == 1:
        thirdElement = tuple_b[0]
        fourthElement = 0
    else:
        thirdElement, fourthElement = (0, 0)
    # add the elements in the tuples to come up with a new
    # tuple
    firstSum = firstElement + thirdElement
    secondSum = secondElement + fourthElement
    sumTuple = (firstSum, secondSum)
    return sumTuple


