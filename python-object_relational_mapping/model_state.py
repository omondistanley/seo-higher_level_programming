#!/usr/bin/python3
"""
    A class that contains the definition of a state and an
    instance base. The class inherits from Base, links to
    MySQL table, the class has an id attribute that represents
    a column of an auto generated unique integer that is the
    primary key. The class also has a name attribute representing
    a column of a string with max of 128 characters.
    Both attributes aren't null.
"""


# import the sqlachemy, and from the sqlalchemy, import
# declarative base. 
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base():



class State(Base):
    # set the module it script is imported.
    if __name__ = "__states__":
        # the id attribute represents a column set to a non-null 
        # integer and is the primary key(primary key set to true)
        id = Column(Integer, primary_key = True)
        # The class attribute represents a column with a string of
        # with 128 maximum characters and can't be null.
        class = Column(sqlalchemy.String(128), nullable = False)
