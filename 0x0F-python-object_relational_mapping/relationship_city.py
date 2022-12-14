#!/usr/bin/python3
"""City class model"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """City class"""
    __tablename__ = 'cities'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True,
                nullable=False
                )
    name = Column(String(128),
                  nullable=False
                  )
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False
                      )
