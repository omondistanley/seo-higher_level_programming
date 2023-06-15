#!/usr/bin/python3
"""
    A square class based on 1-square.py with the private instance
    size with instantiation. The size must be an integer and
    greatr than zero.
"""


class Square:
    """ The square class with the instance attribute and the
        initalization of the size attribute. """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be >= 0")
        else:
            """ If the above condtions are met, the the square's
            size is set to size. """
            self.__size = size
