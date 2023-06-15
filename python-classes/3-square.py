#!/usr/bin/python3
"""
    A square class based on the 2-square.py with a private
    instance attribute of size inistantiated to be an int
    greater than 0. The class also has the private instance
    method that returns the current area of the square.
"""


class Square:
    """ The square class based on the above comments. """

    def __init__(self, size=0):
        """ Initializes the size, to size after ensuring its
        an integer and greater than zero. """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            """ If the size meets the above conditions, then
            the square's size is set to size. """
            self.__size = size

    def area(self):
        area = (self._size * self._size)
        return area
