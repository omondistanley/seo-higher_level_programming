#!/usr/bin/python3
"""
    A script that lists all the state objects from the database.
    The script should take three arguments, uses SQLAlchemy and
    must import state and base.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # the arguments are taken in from the command line.
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Connect the script to the localhost server and port 3306.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))
    # Create a session class that is bound to the engine object.
    Session = sessionmaker(bind=engine)

    # Create a an instance of the session class that queries all
    # the inherited state objects and orders them by state id.
    instance_of_Session = Session()
    stateResults = instance_of_Session.query(State).ORDER BY(states.id)

    # Iterate through the state results after query and print the state
    # name and id
    for state in stateResults:
        print("{}{}".format(state.id, state.name))
