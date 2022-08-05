#!/usr/bin/python3
"""
    import class Base, sqlalchemy
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State

"""
    city class file
"""


class City(Base):
    """
        creation of City class that inherit of Base
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
