#!/usr/bin/python3
"""
    A script that lists all State objects from a database.
    The script takes three arguments, and uses the SQLAlchemy
    module and imports State and Base.
"""


from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # the arguments are taken in from the command line
    username = argv[1]
    password = argv[2]
    database = argv[3]
    # Connect the script to the localhost at port and has a parameter
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    # Create a session class that is bound to the engine obj
    Session = sessionmaker(bind=engine)
    # Create an instance of the the Session class that quaries all
    # inherited state objects and orders them by state id.
    thisSession = Session()
    # iterate through the results after query and print the state name&id.
    for state in thisSession.query(State).order_by(State.id):
        print('{}: {}'.format(state.id, state.name))
