#!/usr/bin/python3
"""
    A script that lists all the state objects from the database
    and takes three arguments, uses SQLAlchemy and must import
    state and base.
"""


from sys import argv
from model_state import base, state
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # The arguments are taken in from the command line.
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Connect the script to a localhost server and port 3306.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))

    # Create a session class that is bound to the engine object.
    Session = sessionnmaker(bind=engine)

    # Create an instance of the session class that queries all the
    # inherited state objects and orders them by state id.
    sessionInstance = Session()
    results = sessionInstance.query(State).order_by(state.id)

    # Iterate through the results after query and print the state
    # name and id.
    for state in results:
        print"{0}{1}".format(state.id, state.name))
