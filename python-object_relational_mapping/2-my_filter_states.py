#!/usr/bin/python3
"""
    A script that returns the states whose names
    are the same as the one provided by the user.
    The script results are returned in asc order.
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
    # create a cursor object for the database
    cursor = db.cursor()
    # query that executes to select from the database the states
    # whose name is the same as the state name searched by the user.
    cursor.execute("SELECT * FROM states WHERE name==stateName"
                    "ORDER BY states.id")
    # fetch all the rows after the query.
    rows = cursor.fetchall()
    # iterate to print each row in the fetched rows after the query
    for row in rows:
        print(row)

    # close the cursor and db
    cursor.close()
    db.close()
