"""
    Database Definition for SCaMPy
    db.py
    Version 0.1
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///scanns.db', echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()
