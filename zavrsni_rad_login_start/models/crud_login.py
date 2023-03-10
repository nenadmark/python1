from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker # session objekt radi upite prema nasoj bazi
# sessionmaker kreira sesion koji ce raditi upite prema bazi

from models.models import Base, User

engine = create_engine("sqlite:///loginapp.db", echo=True) # baza ce nam se zvati loginapp.db
#echo , kad god sqlalchemy izvrsava neku naredbu prema bazi, echo ce nam u terminalu vracati logove 


Base.metadata.create_all(engine, checkfirst=True) 
# kreira sve tablice iz baze 
# nad kojom bazi podataka radim, od koje baze kreiramo tablice ? 
# checkfirst, prije nego sqlalchemy odradi table naredbe, taj checkfirst kaze prije nego izvrsavas createtable naredbe provjeri dali imamo tablicu, tek ako imamo kreiraj sve table


Session = sessionmaker(bind=engine)
session = Session()
# sessionu govorimo da radi s nasom engine bazom ( vidi gore engine )

#### ovo je sve prvi defaultni korak kada radimo s bazama
#### ovo je sve prvi defaultni korak kada radimo s bazama



# nasa funkcija gdje dohvacamo
def get_user_by_email(email):
    # session nam se spaja s sqlalchemy na User objekt koji govori da se spaja na "user" bazu ( u modely.py smo se u objektu User spojili na "user" bazu )
    return session.query(User).filter_by(email=email).first()


# ovom _login_user funkciji dajemo usernam i password iz tkintera
def login_user(login_email, login_password):
    return session.query(User).filter_by(
        email=login_email, 
        password=login_password
    ).first()
    # filter_by vraca listu zapisa u bazi
    # first() hvata prvog usera iz liste, a posto je email jedinstven, uvijuek cemo izvuci iz baze jednog usera ili niti jednog
    # first() je tu samo da nam vrati prvi rezultat ( bio to user ili ne )

def get_all_users():
    return session.query(User).all()

def delete_user(id):
    # get funkcija je shortcut od filter_by
    # user = session.query(User).filter_by(id=id).first()
    # get koristimo samo kada dohvacamo po primarnom kljucu
    user = session.query(User).get(id)
    if user:
        session.delete(user)
        session.commit()


## pyplant dio za komunikaciju s bazama

