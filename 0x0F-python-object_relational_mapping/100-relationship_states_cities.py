#!/usr/bin/python3
"""
    creates the State “California” with the City “San Francisco” from
    the database hbtn_0e_100_usa
"""
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_city import City
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            pool_pre_ping=True
            ),
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    new_state = State(name='California')
    session.add(new_state)
    new_state.cities.append(City(name='San Fransisco'))
    session.commit()

    session.close()
