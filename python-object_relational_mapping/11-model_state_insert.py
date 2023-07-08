#!/usr/bin/python3
"""
    A script that adds State object to a database, and takes in three
    arguments. The script must use the module SQLAlchemy and import
    State and Base.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
        Script takes in 3 arguments, inserts a new state object and
        prints the new states.id after creation.
    """
    # Connect the script to a localhost port using an engine obj.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    # Create a session class that is bound to the engine obj.
    Session = sessionmaker(bind=engine)
    # Create a new instance of the session class that is used for
    # adding the new state.
    session = Session()
    # the state to be added, create a new state obj before addition
    added_state = State(name='Louisiana')
    # add the new state to the session.
    session.add(added_state)
    # Commit the change to the session before proceeding
    session.commit()
    # Print out the id of the added state.
    print(added_state.id)
