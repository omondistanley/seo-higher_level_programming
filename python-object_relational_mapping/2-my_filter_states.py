#!/usr/bin/python3
"""
    A script that reeturns the states whose names are the same
    as the one provided by the user.
"""

import MySQLdb
from sys import argv

if __name__ = "__main__":
    # the arguments username, password, database and state name
    # searched are taken in as command line arguments.
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    # connect the module to a local host at port 3306
    db =MySQLdb.connect(host='localhost', port=3306, user=username
                        password=password, database=database,
                        stateName=stateName)

