#!/usr/bin/python3
"""
    A script that lists all the state objects from the database.
    The script should take three arguments, uses SQLAlchemy and
    must import state and base.
"""

import SQLAlchemy
from sys import argv

if __name__ == "__main__":
    # the arguments are taken in from the command line.
    username = argv[1]
    password = argv[2]
    database = argv[3]


