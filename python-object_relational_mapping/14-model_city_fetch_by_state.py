#!/usr/bin/python3
"""
    A script that prints all City objects from the database and
    takes 3 arguments and must use the SQLAlchemy module. Import
    the State and Base, results must be in ascending order.
"""



from sys import argv
from model_state import Base, State
from model_city import City
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
    cities_list = session.query(State).order_by(City.id).all()
    # Iterate through the list of cities and print by state
    for city in cities_list:
        state = session.query(State).filter_by(State.id == city.state.id).first()
        print(f"{row.State.name}: ({row.id} {row.City.name}")
    # Close the session.
    session.close()
