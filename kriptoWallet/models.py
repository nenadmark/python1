import sqlalchemy as db
import datetime as dt
from sqlalchemy.ext.declarative import declarative_base

# 
# 1. Koji mi podaci trebaju u bazi?
# 2. Koji su to tipovi podataka?
# 3. Zadovoljavaju li prva dva koraka sve sto trebamo u zadatku, ako ne prodji opet 


Base = declarative_base()


class CryptoBalance(Base):
    __tablename__ = "crypto_balance"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False) # ne smije biti prazno ako stavimo false
    shortcode = db.Column(db.String, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_date = db.DateTime(db.Float, nullable=False, default=dt.datetime.now)

    def __repr__(self):
        return self.name