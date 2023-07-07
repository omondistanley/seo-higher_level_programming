#!/usr/bin/python3
"""
    A script that prints all City objects from the database and
    takes 3 arguments and must use the SQLAlchemy module. Import
    the State and Base, results must be in ascending order.
"""



from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # The arguments are taken in from the command line connect
    # the script to the localhost at port.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    # Create a session class that is bound to the engine obj
    Session = sessionmaker(bind=engine)
    # Create an instance of the session class that queries all
    # inherited state objects and orders them state id.
    session = Session()
    # Use the instance session to query to for the cities and
    # arrange in order
    states = session.query(State, City.id, City).filter(
            City.state.id == State.id).order_by(City.id)
    # Iterate through the rows in the states
    for row in states:
        print(f"{row.State.name}: ({row.id} {row.City.name}")
    # Close the session.
    session.close()
