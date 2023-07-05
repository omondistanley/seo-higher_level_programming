#!/usr/bin/python3
"""
    Script listing all the states starting with letter N
    from the database. 
"""

from MySQLdb import mysql
database = mysql

if __name__ = "__main__";
    import argv
    username = argv[1]
    password = argv[2]
    database = argv[3]

    database = msq.connect(host="localhost", port= 3306,
            user="username", pwd="password", db ="database")
    
    cursor = db.cursor()
    query = SELECT * FROM states WHERE names LIKE 'N%'
                ORDER BY states.id ASC
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    
    cursor.close()
    database.close()

    
