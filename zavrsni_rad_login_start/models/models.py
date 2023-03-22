import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    is_admin= db.Column(db.Boolean, default=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return self.name






class Plants(Base):
    __tablename__= "plants"  # naziv tablice u samoj bazi podataka

    id = db.Column(db.Integer, primary_key=True) # koji tip podataka ce biti u stupcu
    name = db.Column(db.String, nullable=False)
    photo_path = db.Column(db.String)

    def __repr__(self) -> str:
        return self.name
    


class Pots(Base):
    __tablename__= "pots"  

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, nullable=False)
    plant_inside = db.Column(db.String)

    def __repr__(self) -> str:
        return self.name