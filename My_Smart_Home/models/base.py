import datetime as dt

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

appliances = create_engine("sqlite:///appliance.db", echo=True)
room = create_engine("sqlite:///room.db", echo=True)