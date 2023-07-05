#!/usr/bin/python3
"""
    A script that lists all the states starting with
    N in theie names and ordered by the state id in
    ascending order.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # the arguments and they're being read in from the
    # command line as command line arguments.
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # connecting the module to a local MySQL server running
    # on port 3306.
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, password=password,
                         database=database)
    # create a cursor object
    cursor = db.cursor()
    # execute a query that selects from the database states
    # whose names start with N and returns in ascending order
    query1 = "SELECT * FROM states WHERE BINARY name LIKE 'N%' "
    query2 = "ORDER BY states."
    query = query1 + query2
    cursor.execute(query)
    # fetch all rows for printing after the query.
    rows = cursor.fetchall()
    # iterate through the rows while printing them out.
    for row in rows:
        print(row)

    # close the cursor and db objects.
    cursor.close()
    db.close()
