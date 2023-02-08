
import datetime as dt

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Students(Base):
    __tablename__ = "students"
    
    

class Classes(Base):
    __tablename__ = "classes"



class Professors(Base):
    __tablename__ = "professors"
