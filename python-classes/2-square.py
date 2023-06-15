#!/usr/bin/python3
""" 
    A square class based on 1-square.py with the private instance
    size with instantiation. The size must be an integer and
    greatr than zero.
"""


class Square:
    """ The square class with the instance attribute and the
        initalization of the size attribute. """

    def __init__(size, self):
        """ The size attribute is a present and a private
            attribute, and is initalized to size. """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be >= 0")
