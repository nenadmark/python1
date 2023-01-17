from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

engine = create_engine("sqlite:///loginapp.db", echo=True) 
Base.metadata.create_all(engine, checkfirst=True) 

Session = sessionmaker(bind=engine)
session = Session()

def get_user_by_email(email):
    return session.query(User).filter_by(email=email).first()


def login_user(login_email, login_password):
    return session.query(User).filter_by(
        email=login_email, 
        password=login_password
    ).first()
def get_all_users():
    return session.query(User).all()

def delete_user(id):
    user = session.query(User).get(id)
    if user:
        session.delete(user)
        session.commit()