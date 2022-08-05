#!/usr/bin/python3
"""
    lists all State objects that contain the letter a from the database
    hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import sys

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            pool_pre_ping=True
            ),
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    for result in session.query(State).filter(State.name.like('%a%'))\
                         .order_by(State.id).all():
        print("{}: {}".format(result.id, result.name))
    session.close()