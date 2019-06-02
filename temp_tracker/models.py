"""
Temperature Tracker Database model
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

BASE = declarative_base()


class Temperature(BASE):
    __tablename__ = 'temperature'

    id = Column(Integer, primary_key=True)
    created_at = Column(Integer)
    city = Column(String(128))
    temperature = Column(Integer)

