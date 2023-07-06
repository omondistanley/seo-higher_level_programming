#!/usr/bin/python3
"""
    A script that takes arguments from the user and displays
    the state names that are the same as the user input. In
    this case, let the script be SQL injection free.
"""

import MySQLdb
from sys import argv

if __name__ = "__main__":
    # The four arguments taken from the command line: username
    # password, database and the state name searched
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    # Connect the script to a MYSQL server running on a local
    # host at port 3306.
    db = MySQLdb.connect(host='localhost', port=3305, user=username,
                         password=password, databse=databse)

    # Create a cursor object that executes all the SQL queries for
    # the data base after connection to the local host.
    cursor = db.cursor()
    # Use the cursor to  execute an SQL query that selects from the
    # states those whose names are the same as the argument providaed.
    # NOTE: The query should be SQL injection free.
    cursor.execute("SELECT * FROM states WHERE BINARY name = '@%s'"
                   "ORDER BY states.id ASC")
    # fetch all the rows after the query
    rows = cursor.fetchall()
    # iterate through the rows and print out the output.
    for row in rows:
        print(row)

    # Close the cursor object.
    cursor.close()
    db.close()
