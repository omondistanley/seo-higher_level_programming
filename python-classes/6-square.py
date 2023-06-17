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
        area = self.size * self.size
        return area

    def size(self):
        return self.size

    def size(self, value=0):
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be => 0")
            else:
                self.size = value
        else:
            raise TypeError("size must be an integer")

    def position(self):
        return self.position

    def position(self, value):
        if (type(value) is tuple and len(value) == 2 and
            type(value[0]) == int and type(value[1]) == int
            and value[0] >= 0 and value[1] >= 0):
                self.position = value
        else:
            raise TypeError("position must be a tuple of two integers")

    def my_print(self):
        i, j = 0, 0
        if self.size == 0:
            print()

            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
