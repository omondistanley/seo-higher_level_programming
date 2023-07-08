#!/usr/bin/python3
"""
    A class that contains the definition of a City, inherits the base
    class, links to the cities table and has both id and name attributes.
    The id attribute id set to be the primary key. Class also has a state.id
    attribute that is set to be the foreign key.
"""



from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import ForeignKey
from model_state import Base, State

Base = declarative_base()

class City(Base):
   """
   The class links to a MySQL table of cities.
   """
   __tablename__ = 'cities'
   # The id attribute represents a column to a non-null integer and is the
   # primary key. ie. primary key is set to true.
   id = Column(Integer, primary_key=True, nullable=False)
   
   # The name attribute with a string which holds amazimum of 128 characters
   # and can't be null. ie> nullable is set to false
   name = Column(String(128), nullable=False)
   # The state_id attribute repersenting a column of an integer which is a
   # foreign key to the states.id and can't be null
   state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
