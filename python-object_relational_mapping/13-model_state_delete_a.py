#!/usr/bin/python3
"""
    A script that deletes all the State objects with a name containing letter
    'a' from the database.
"""


from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # the script takes three arguments, is connected to a MySQL server running
    # on a localhost and isn't execturable when imported.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost{}'
                           .format(argv[1], argv[2], argv[3]))
    #Create a session class
    Session = sessionmaker(bind=engine)
    # Use an instance of the session class to query the State objects, filtering
    # those with letter 'a'
    session = Session()
    deleted_states = session.query(State).filter(State.name.contains('a'))

    # iterate through the deleted states and using the delete function delete
    # each of the states.
    for state in deleted_states:
        session.delete(state)

    # Commit the changes done during the session.
    session.commit()
