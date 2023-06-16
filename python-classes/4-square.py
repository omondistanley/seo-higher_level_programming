#!/usr/bin/python3
"""
    A class defining a square base on the 3-square.py with the private
    intstance attributw size. The attribute should have an attribute to
    retrieve it, a property to set it, instantiation, and a method that
    retruns the area.
"""


class Square:
    """ A class fulfilling the requirements. """

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """ Method that gives the area of the square """
        area = self.__size * self.__size
        return area

    # @property to retrive the size attribute.
    def size(self):
        return self.__size

    # @property to set the size attribute to a given value.
    def size(self, value):
        self.__size = value
        """ Size must be an integer and greater than zero. """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
