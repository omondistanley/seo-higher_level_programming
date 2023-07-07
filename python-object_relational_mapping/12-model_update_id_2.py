#!/usr/bin/python3
"""
    A script that changes the name of a state object in the database
    Change the name of the object on in=2.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


