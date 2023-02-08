# ponudi funkcionalnosti smart kuce
#
# Baze: 

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models.appliance import TV, Refrigerator, Speakers
from models.room import Room


if __name__ == "__main__":
    db_engine = db.create_engine("sqlite:///SmartHome.db", echo=True)
    Base.metadata.create_all(db_engine, checkfirst=True)

    Session = sessionmaker(bind=db_engine)
    session = Session()

    print(session.query(Room).first())