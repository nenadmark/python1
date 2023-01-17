import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__= "users"  # naziv tablice u samoj bazi podataka

    id = db.Column(db.Integer, primary_key=True) # koji tip podataka ce biti u stupcu
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False) #unique=True)
    is_admin= db.Column(db.Boolean, default=False)
    pin = db.Column(db.String, nullable=False)

    def __repr__(self) -> str:
        return self.name

#### ovo je sve prvi defaultni korak kada radimo s bazama