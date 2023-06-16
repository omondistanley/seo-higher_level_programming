#!/usr/bin/python3
"""
    A class defining a square with a private instance attribute of
    size, which must hava a setter and getter proprty and be an int
    greater than 0.
"""


class Square:
    """ The square class based on hte earlier comments. """

    def __init__(self, size=0):
        """ Initializes the size to being a private attribute. """
        self.size = size

    def area(self):
        area = self.size * self.size
        return area

    def size(self):
        return self.__size

    def size(self, value):
        if type(value) == int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """ Prints out the square with the character '#' """
        i, j = (0, 0)
        if self.size == 0:
            print()
        else:
            while i < self.size:
                while j < self.size:
                    print("#", end="")
                    j = j + 1
                print()
                i = i + 1
                j = 0
