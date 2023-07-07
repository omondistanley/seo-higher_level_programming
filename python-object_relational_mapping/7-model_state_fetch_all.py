#!/usr/bin/python3
"""
    A script that lists all State objects from a database.
    The script takes three arguments, and uses the SQLAlchemy
    module and imports State and Base.
"""


import SQLAlchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # the arguments are taken in from the command line
    # Connect the script to the localhost at port.
    db = SQLAlchemy.connect(host='localhost', port=3306,
                            user=argv[1],password=argv[2],
                            database=argv[3])

    cursor = db.connect()
    
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
    # engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
    #                       .format(argv[1], argv[2], argv[3]))
    # Create a session class that is bound to the engine obj
    # Session = sessionmaker(bind=engine)
    # Create an instance of the the Session class that quaries all
    # inherited state objects and orders them by state id.
    # session = Session()
    # iterate through the results after query and print the state name&id.
    # for state in session.query(State).order_by(State.id):
    #   print('{}: {}'.format(state.id, state.name))
