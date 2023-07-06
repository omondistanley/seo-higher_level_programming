#!/usr/bin/python3
"""
    A script that takes an argument and returns
    values in the states table where the name
    matches the argument provided.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # the script takes four arguments read in from
    # the command line as command line arguments.
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    # Connect the module to a local host serve that
    # is at port 3306
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, password=password,
                         database=database)
    # Create a cursor object for the db that executes the
    # SQL queries.
    cursor = db.cursor()
    # execute a query that selects from the states those
    # whose names are the same as the argument provided.
    cursor.execute("SELECT * FROM states WHERE name == stateName"
                   "ORDER BY states.id")
    # fetch all rows for printing after the query.
    rows = cursor.fetchall()
    # iterate through the rows, and print each out.
    for row in rows:
        print(row)

    # Close the cursor object and the db.
    cursor.close()
    db.close()
