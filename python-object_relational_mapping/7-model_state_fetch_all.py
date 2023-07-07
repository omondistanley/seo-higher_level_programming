#!/usr/bin/python3
"""
    A script that lists all the state objects from the database.
    The script should take three arguments, uses SQLAlchemy and
    must import state and base.
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    import SQLAlchemy
    # the arguments are taken in from the command line.
    username = argv[1]
    password = argv[2]
    database = argv[3]


