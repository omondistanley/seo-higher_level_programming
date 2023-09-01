#!/usr/bin/python3
"""
    A base class with a private attribute and a constructor.
"""

import json
import csv
import turtle


class Base():

    """
        Private attribute _nb_objects = 0
    """
    __nb_objects = 0

    """
        Constructor initializingg the id variables etc. The id is a 
        none-null integer.
    """
    def __init__(self, id=None):
        """ Check if the id attribute is not null and set it to be the id attribute! """
        """ If not increase __nb_objects and set it to the id variable.(private) """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
