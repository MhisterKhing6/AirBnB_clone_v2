#!/usr/bin/python3
"""
user module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """
    User class
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    place = relationship("Place",
                         cascade='all, delete, delete-orphan',
                         backref='user')
    reviews = relationship("Review",
                           cascade='all, delete, delete-orphan',
                           backref='user')

    def __init__(self, *args, **kwargs):
        """Overriding constructor"""
        super().__init__(*args, **kwargs)
