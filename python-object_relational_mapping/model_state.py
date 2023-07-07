#!/usr/bin/python3
"""
    A class that contains the definition of state and sn instance
    base. The class inherits from base, links to MySQL table and has
    two attributes, id and class.
"""

# from the sqlalchemy, import Column, integer, string and declarative
# base.
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    # the class should be mapped to a table named states in the database
    __table__ = 'states'
        # the id attribute representing a column set to a non-null integer
        # and is the primary key(primary key set to true)
        id = Column(Integer, primary_key = True)
        # The class attribute with a string which holds a maximum of 128
        # characters and can't be null(nullable value set to false.)
        name = Column(String(128), nullable = False)
