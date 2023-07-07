#!/usr/bin/python3
"""
    A script that changes the name of a state object in the database.
    Change the name of the object on id=2
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Script takes in 3 arguments and connect the script to a localhost
    # using engine obj
    engine = create_engine('mysql+mysqldb://{}:{}localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    # create a session class bound to the engine object
    Session = sessionmaker(bind=engine)
    # create an instance of the session class used to change the object at
    # id 2.
    state = session.query(State).filter(id == 2).first()
    # Update the name to new Mexico.
    state.name = 'New Mexico'

    # Commit the change of the session to the database,
    session.commit()
