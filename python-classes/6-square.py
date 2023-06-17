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
        self.size = size
        self.position = position

    def area(self):
        # calculates and returns the area of the square.
        area = self.size * self.size
        return area

    def size(self):
        # the size property
        return self.size

    def size(self, value=0):
        # checks if the value is an integer and grater than 0 to be set
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be => 0")
            else:
                self.size = value
        else:
            raise TypeError("size must be an integer")

    def position(self):
        # the position property
        return self.position

    def position(self, value):
        # check if the value is a tuple of integers greater than 0 and set to
        # the being the position
        if (type(value) is not tuple or len(value) != 2 or
                type(value[0]) != int or type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.position = value

    def my_print(self):
        i, j = 0, 0
        if self.size == 0:
            print()
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
