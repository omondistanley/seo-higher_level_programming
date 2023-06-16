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
        """ Method to initialize the size attributes """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    # @property to retrive the size attribute.
    def size(self):
        return self._size

    # @property to set the size attribute to a given value.
    def size(self, value):
        self._size = value
        """ Size must be an integer and greater than zero. """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    # the method to give the area, after the area is set by the setter value
    def area(self):
        """ Method that gives the area of the square by multiplying the
            size. """
        area = self.__size * self.__size
        return area
