#!/usr/bin/python3
"""
state module
"""
import os

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City


class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

        cities = relationship('City',
                              cascade="all, delete, delete-orphan",
                              backref='state')
    else:
        name = ""
        @property
        def cities(self):
            return [st for st in storage.all(City).values()
                    if
                    st.state_id == self.id]

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
