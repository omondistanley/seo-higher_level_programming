#!/usr/bin/python3
"""
    A script that lists all the state objects from the database.
    The script should take three arguments, uses SQLAlchemy and
    must import state and base.
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    import SQLAlchemy
    # the arguments are taken in from the command line.
    username = argv[1]
    password = argv[2]
    database = argv[3]

    db = SQLAlchemy.connect(host='localhost', port=3306,
                            user=username, password=password,
                            database=datase)
    # Create a cursor object connected to the database connecting
    # the script to the localhost server.
    cursor = db.cursor()
    # Use the execute function of the cursor to execute a query
    # that returns the results in acending order.
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    # Fetch all rows printing after the query
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor.
    cursor.close()
    db.close()
