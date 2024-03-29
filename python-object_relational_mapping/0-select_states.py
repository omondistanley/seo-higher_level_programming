#!/usr/bin/python3
"""
    A script that lists all states in ascending order
    according to the state.id
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # the arguments, username, password and database name
    # arguments are read from the command line args
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # create a database object that connects to MySQL and a
    # localhost and port 3306.

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, password=password,
                         db=database)
    # create a cursor object connected to the database.
    cursor = db.cursor()
    # executing a query with selecting from the states and is
    # ordered by the state id in ascending order
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    # fetch all rows for printing after the query.
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
