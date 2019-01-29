#!/usr/bin/python3
"""This is the state class"""
import os
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
        cities: reference to the City objects related to State
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    # For DBStorage
    cities = relationship("City",
                          cascade="all, delete", backref="state")

    # For FileStorage
    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter for amenities of theis placs
            only for file storage"""
            lst = []
            for k, v in models.storage.all(models.City).items():
                if v.place_id == self.id:
                    lst += [v]
            return lst
