#!/usr/bin/python3
"""
    A script listing all states from the database
    hbtn_0e_0_usa taking 3 arguments; mysql username, mysql
    password, database name. Must use the MySQLdb module and
    results must be sorted in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__";

    # the arguments, username, password and database name and
    # in order.
    # the argumetns are read from the command line

    username = argv[1]
    password = argv[2]
    database = argv[3]

    # connect to a MySQL server running on a localhost port 3306
    
    db = MySQLdb.connect(host = 'localhost', port = 3306,
            user = username, pwd = password, db = database)
    cursor = db.cursor()
    
    """
        select everything, from states database/file and ordered by
        state id in ascending order cursor executes the select, from
        and order by statements/ queries.
    """
    
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    """ gets all rows from a cursor object """
    
    rows = cursor.fetchall()
    
    """ iterates through and prints out all the rows, then close the
    cursor and database objects. """
    for row in rows:
        print(row)

    cursor.close()
    db.close()

    
