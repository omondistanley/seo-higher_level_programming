#!/usr/bin/python3
"""
    A script that prints the first state object from the database
    and uses SQLAlchemy, imports State and is linked to a MYSQL server
    on a localhost. Script prints nothing if states is empty.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # The arguments are taken in from the command line.
    username = argv[1]
    password = argv[2]
    database = argv[3]
    # Connect the script to a MySQL server on a localhost using the
    # engine object.
    engine = create_engine('mysql+mysql://{}:{}@localhost/{}'
                           .format(username, password, database))
    # Create a session class bound to the engine obj.
    Session = sessionmaker(bind=engine)

    # Create an instance of the session class that queries all the
    # inherited state objects and order them by state id.
    session = Session()
    result = session.query(State).order_by(State.id).first()
    # fetch the first row from the results of the query
    # row = result.first()
    # Check if the row from the result is empty, if so print nothing
    # Else, fetch one row, and print the state id and name out.
    if result is None:
        print("Nothing")
    else:
        print('{}: {}'.format(result.id, result.name))
