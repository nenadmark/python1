import datetime as dt
import sqlalchemy as db
from models.base import Base
from sqlalchemy.orm import relationship

class Room(Base):
    __tablename__ = "rooms"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    floor = db.Column(db.Integer, nullable=False)

    # TV se odnosi na ime klase
    # ovo je veza one to many
    tv_devices = relationship("TV")
    refrigerators = relationship("Refrigerator")
    lights = relationship("Lights")
    speakers = relationship("Speakers")

    def __repr__(self):
        return self.name
 