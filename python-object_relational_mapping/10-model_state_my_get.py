#!/usr/bin/python3
"""
    A script that prints the State object with the name passed
    as an  argument by the user.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # The arguments are taken in from the command line
    # Connect the script to the localhost at port 3306
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    # Create a session class that is bound to the engine
    Session = sessionmaker(bind=engine)
    # Create an instance of a session class that queries the state objs.
    session = Session()
    # The query checks and gives the state with the same name as
    # the argument provided.
    states = session.query(State).filter(State.name == argv[4]).first()
    # Check if the state is found, if not print not found
    if states is None:
        print("Not found")
    else:
        print(states.id)
