#!/usr/bin/python3
"""
    A script that adds State object to a database, and takes in three
    arguments. The script must use the module SQLAlchemy and import
    State and Base.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ = "__main__":
    """
        Script takes in 3 arguments, inserts a new state object and
        prints the new states.id after creation.
    """

