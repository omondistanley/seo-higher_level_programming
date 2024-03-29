#!/usr/bin/python3
"""
    A script that prints the first state object from the database
    and uses SQLAlchemy, imports State and is linked to a MYSQL server
    on a localhost. Script prints nothing if states is empty.
"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # The arguments are taken in from the command line
    # Connect the script to a MySQL server on a localhost using the
    # engine object.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    # Create a session class bound to the engine obj.
    Session = sessionmaker(bind=engine)

    # Create an instance of the session class that queries all the
    # inherited state objects and order them by state id.
    session = Session()

    state = session.query(State).order_by(State.id).first()
    # Check if the row from the result is empty, print nothing
    # Else, fetch one row, and print the state id and name out.
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
