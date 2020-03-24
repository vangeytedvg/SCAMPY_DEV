from database.linkdb import MailBox
from database.db import Session, engine, Base
# Generate database schema


def makedb():
    print("Making the database")
    Base.metadata.create_all(engine)

