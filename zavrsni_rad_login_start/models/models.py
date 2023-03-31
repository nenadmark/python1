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
    __tablename__= "plants"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    sort = db.Column(db.String, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Integer, nullable=False)
    p_code = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String)

    def __repr__(self) -> str:
        return self.name
    
class Pots(Base):
    __tablename__= "pots"  

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, nullable=False)
    radius = db.Column(db.Integer, nullable=False)
    p_code = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String)

    def __repr__(self) -> str:
        return self.name