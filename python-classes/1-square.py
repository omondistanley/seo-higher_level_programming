#!/usr/bin/python3
"""
    A square class based on the 0-square.py, with a 
    private instance attribute of size, the instantiation
    of size wih no type
"""

class Square:
    """ The square class with the private instance attribute
        and the initialization of the size attribute. """

    def __init__(self, size):
        """ the self is used to limit the size attribute when 
            initialized to the class only. """
        # the private instance attribute is assigned the size.
        self.__size = size
