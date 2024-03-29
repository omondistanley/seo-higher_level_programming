#!/usr/bin/python3
"""
    A script that takes an argument from the user and
    lists all the city in the state whose name matches
    the argument provided.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # The script takes in four arguments read in from the
    # command line
    username = argv[1]
    password = argv[2]
    database = argv[3]
    stateName = argv[4]

    # Connect the module to a local host server that running
    # on port 3306.
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, password=password,
                         database=database)
    # Create a cursor object that executes the SQL queries.
    cursor = db.cursor()
    # Using the cursor's execute function, select from the list
    # the states whose names match the argument provided and return
    # their cities.
    queryExecuted = cursor.execute("SELECT cities.id, cities.name, states.name\
                   FROM cities JOIN states ON cities.state_id = states.id\
                   WHERE states.name = '{}'\
                   ORDER BY cities.id ASC".format(stateName))
    # Fetch all rows after executing the query.
    rows = cursor.fetchall()
    # create an array
    final = []
    # iterate through the results from the execution of the query,
    # adding them to the array.
    # for i in range(queryExecuted):
    #  final.append(rows[i][0])
    #  print(', '.join(final))
    print(", ".join(row[1] for row in rows))

    # Close the cursor object.
    cursor.close()
    db.close()
