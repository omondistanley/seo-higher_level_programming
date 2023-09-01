#!/usr/bin/python3
""" A rectangle class that inherits from the base class. """

from models.base import Base

class Rectangle(Base):
    """ Initialization of the variables and calling the id
        attribute from the Base suoer class. """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def width(self):
        """ Getter property for the width """
        return self.__width
    """ The setter property for the width """
    def width(self, val):
        self.__width = val
        return self.__width
    """ The getter property for the height """
    def height(self):
        return self.__height
    """ The setter property for the height """
    def height(self, val):
        self.__height = val
        return self.__height
    """ The getter property for x """
    def x(self):
        return self.__X
    """ The setter property for x """
    def x(self, val):
        self.__x = val
        return self.__x
    """ The getter propety for y """
    def y(self):
        return self.__y
    """ The setter property for y """
    def y(self, val):
        self.__y = val
        return self.__y
