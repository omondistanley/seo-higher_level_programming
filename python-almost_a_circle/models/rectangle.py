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
    def width(self, val):
        """ Setter property for the width attribute. """
        self.__width = val
        return self.__width
    def height(self):
        """ Getter property for the height """
        return self.__height
    def height(self, val):
        """ Setter property for the height """
        self.__height = val
        return self.__height
    def x(self):
        """ Getter property for x """
        return self.__x
    def x(self, val):
        """ Setter property for the x attribute """
        self.__x = val
        return self.__x
    def y(self):
        """ Getter property for the y attribute """
        return self.__y
    def y(self, val):
        """ Setter property for the y attribute """
        self.__y = val
        return self.__y
