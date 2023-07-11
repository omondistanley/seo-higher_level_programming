#!/usr/bin/python3
"""
    A class that defines a square based on 5-square.py class.
"""


class Square:
    """ The square class with size, position and area. """
    def __init__(self, size=0, position=(0, 0)):
        # Initialize and make the size and position private
        self._size = size
        self._position = position

    def area(self):
        # Calculates and returms the area of the square.
        return self._size * self._size
    
    def size(self):
        # gets the size property of the square.
        return self._size

    def size(self, value=0):
        # sets the size to a given integer greater than 0
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be => 0")
            else:
                self._size = value
        else:
            raise TypeError("size must be an integer")

    def position(self):
        # gets the position property of the square.
        return self._positon

    def position(self, value):
        # sets the position property. Check if value is a
        # tuple of ints >=0.
        if len(value) != 2 or not isinstance(value, tuple) or\
                not all(isinstance(val, int) or\
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2\
                     positive integers")
        else:
        self._position = value

    def my_print(self):
        # method that prints out the square details.
        if self._size == 0:
            print()
        else:
            for i in range(slef._position[1]):
                print()
            for i in range(self._size):
                print(" " * self._position[0] + '#' *self._size)
