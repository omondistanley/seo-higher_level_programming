#!/usr/bin/python3
"""
    Script listing all the states starting with letter N
    from the database. 
"""

import MySQLdb as db
import sys

if __name__ = "__main__";
    # the arguments, username, password and database are taken
    # from the comand line.
    username = argv[1]
    password = argv[2]
    database = argv[3]

        # Connect to a MySQL server running on a local host and
        # the given port.
    db = MySQLdb.connect(host = "localhost", port = 3306; user =
            username, pin = password, db = database)

        # Create a cursor object connected to the database.
    cursor = db.cursor()

        # Query that selects the states starting with letter N and
        # has them ordered by state id. 

