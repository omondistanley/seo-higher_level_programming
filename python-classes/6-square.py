#!/usr/bin/python3
"""
    A class defining a square based on 5-square class with a private
    instance attribute of size with a getter and setter property, a
    private position attribute, private instance method that returns
    the area and a print private instance method.
"""


class Square:
    """ The square class based on the earlier comments. """

    def __init__(self, size=0, position=(0, 0)):
        """ Initalializes the size and position and sets the to
                private. """
        self._size = size
        self._position = position

    def area(self):
        # calculates and returns the area of the square.
        area = self._size * self._size
        return area

    def size(self):
        # the size property
        return self._size

    def size(self, value=0):
        # checks if the value is an integer and grater than 0 to be set
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be => 0")
            else:
                self._size = value
        else:
            raise TypeError("size must be an integer")

    def position(self):
        # the position property
        return self._position

    def position(self, value):
        # check if the value is a tuple of integers greater than 0 and set to
        # the being the position
        if len(value) != 2 or not isinstance(value, tuple) or \
                not all(isinstance(values, int) or \
                not all(values >= 0 for values in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = value

    def my_print(self):
        i, j = 0, 0
        if self._size == 0:
            print()
            for i in range(self._size):
                print(" " * self._position[0], end="")
                print("#" * self._size)
