#!/usr/bin/python3
"""
A base class with a private attribute and a constructor!
"""
import json

class Base(object):
    """The prrivate attrivute initalized to 0 """

    __nb_objects = 0

    """ Constructor """
    def __init__(self, id=none):

