#!/usr/bin/python3
"""
    A script that takes arguments and displays all the
    states whose names match the argument provided, and
    is immune to SQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # The script takes four arguments from the command line
    # as command line arguments.
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    # Connect the module to a local host server running at
    # port 3306.
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, password=password,
                         database=database)
    # Create a cursor object that executes the SQL queries
    cursor = db.cursor()
    # Using the cursor's execute function, execute a query
    # that selects from the states whose names are same as
    # the one provided.
    cursor.execute("SELECT * FROM states WHERE BINARY name = '@%s'"
                   "ORDER BY states.id".format(stateName))
    # fetch all the rows for printing after the query.
    rows = cursor.fetchall()
    # iterate through the rows and print the outcome.
    for row in rows:
        print(row)

    # close the cursor object.
    cursor.close()
    db.close()
