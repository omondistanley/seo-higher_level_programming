#!/usr/bin/python3
"""
    This module defines a square class.
    The square class has the following attributes:
        * size: The size of the square.
        * position: The position of the square.
        The square class has the following methods:
            * area(): Returns the area of the square.
            * size(): Returns the size of the square.
            * size(value): Sets the size of the square.
            * position(): Returns the position of the square.
            * position(value): Sets the position of the square.
            * my_print(): Prints the square
"""


class Square:
    """ The square class with size, position and area. """

    def __init__(self, size=0, position=(0, 0)):
    """ Initialize and make the size and position private """
        self._size = size
        self._position = position

    def area(self):
        return self._size * self._size
    
    def size(self):
        return self._size

    def size(self, value=0):
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be => 0")
            else:
                self._size = value
        else:
            raise TypeError("size must be an integer")

    def position(self):
        return self._positon

    def position(self, value):
        if len(value) != 2 or not isinstance(value, tuple) or\
                not all(isinstance(val, int) or\
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2\
                     positive integers")
        else:
        self._position = value

    def my_print(self):
        if self._size == 0:
            print()
        else:
            for i in range(self._position[1]):
                print()
            for i in range(self._size):
                print(" " * self._position[0] + '#' * self._size)
