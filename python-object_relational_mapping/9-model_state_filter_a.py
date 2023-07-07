#!/usr/bin/python3
"""
    A script that lists all the state objects that contain letter 'a'
    from the database.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Script takes three arguments from the command line and is
        connected to a local MySQL server, and results are in ASC.
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    # Create a sessionmaker class bound to the engine object,
    Session = sessionmaaker(bind=engine)
    # Create an instance of session class that queries the state objs.
    session = Session()
    # The query checks and filters with those with letter a
    states = session.query(State).filter(State.name.contains('a'))

    for state in states:
        print("{}: {}".format(state.id, state.name))
