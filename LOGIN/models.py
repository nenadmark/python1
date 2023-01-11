import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__= "users" # naziv tablice u samoj bazi podataka

    id = db.Column(db.Integer, primary_key=True) # koji tip podataka ce biti u stupcu