import datetime as dt
from email.policy import default
from typing import Collection
import sqlalchemy as db
from models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr


# tu cemo sad stavit jednu klasu, i onda cemo iz te klase nasljedjivati druge s drugim svojstvima
# zato ovoj klasi ne dajemo da extenda Base ali i ApplianceBase, vec ce ostale children klase to extendati
class ApplianceBase:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    manufacturer = db.Column(db.String)
    active = db.Column(db.Boolean, default=False)

    # ovo je nacin kako namjestiti sql foreign key !
    @declared_attr
    def room_id(cls):
        # rooms se odnosi na __tablename__
        return db.Column(db.Integer, db.ForeignKey('rooms.id'))

    def __repr__(self):
        return self.name


class TV(ApplianceBase, Base):
    __tablename__ = "televisions"
    #primari key uvijek zadati, kao i __tablename__

    channel = db.Column(db.Integer, nullable=True, default=1)

    volume = db.Column(db.Integer, default=0)

    # rooms se odnosi na tablename
    # RELATIONSHIP
    # relationship nam daje mogucnost da pristupuimo objektu koji je u drugoj bazi,
    # foreuign key bi funkcionirao ali samo bi te keyeve dijelili jedno medju drugim bazama, ovako mozemo pristupiti i ostalim podatcima u drugoj bazi, npr drugim columnima
    # relationship upotpunjuje komunikaciju medju dvije tablice, tako mozemo do ostalih informacija doci a ne samo do primary_key


    # ova strana gdje nam je foreign key, tu ovaj relationship onda mora imati back_populates = ""
    # Room se odnosi na ime klase, a tv_devices se odnosi na naziv atributa u Room klasi
    room = relationship("Room", back_populates="tv_devices")


class Refrigerator(ApplianceBase, Base):
    __tablename__ = "refrigerators"

    temperature = db.Column(db.Float, default=4.0)

    room = relationship("Room", back_populates="refrigerators")


class Speakers(ApplianceBase, Base):
    __tablename__ = "speakers"

    volume = db.Column(db.Integer, default=0)
    playlist_playing = db.Column(db.Integer, default="default_playlist_playing")  
    eq_settings = db.Column(db.Float, default="flat")

    room = relationship("Room", back_populates="speakers")
