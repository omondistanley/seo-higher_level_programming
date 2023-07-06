#!/usr/bin/python3
"""
    A script that lists all the cities from the states
    list and database, the script should run on a local
    host server running through port 3306.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # The arguments are taken in from the command line 
    # arguments.
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Connecting the script to the local hose server running
    # on port 3306.
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, password=password,
                         database=database)
    
    # Create a cursor object for executing the queries.
    cursor = db.cursor()
    # Usinng the cursor's execute function, execute a query
    # that returns the cities ordered in ascending order by
    # the id of the cities.
    cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")

    # Fetch all rows after the query
    rows = cursor.fetchall()

    # Iterate through the rows then print out the outcome.
    for row in rows:
        print(row)

    # close the cursor object.
    cursor.close()
    db.close()

