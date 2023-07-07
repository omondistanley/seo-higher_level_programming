#!/usr/bin/python3
"""
    A script that changes the name of a state object in the database
    Change the name of the object on in=2.
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
    # create a session class bound to the engine object.
    Session = sessionmaker(bind=engine)
    # create an instance of the session class used to change the state
    # object at id=2
    session = Session()
    # Using the instance session, query for the object at second id
    states = session.query(State).filter(id=2).first()
    # create the new state variable.
    states.name = 'New Mexico'
    # commit the changes to the database.
    session.commit()

