#!/usr/bin/python3
"""
     lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
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
    for res in session.query(State).order_by(State.id).all():
        print("{}: {}".format(res.id, res.name))
    session.close()
