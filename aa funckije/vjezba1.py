import datetime

def greetings():
    now = datetime.datetime.now().hour
    if now < 10:
        print("Dobro jutro!")
    elif 10 <= now < 17:
        print("Dobar dan!")
    else:
        print("Dobar dan!")
greetings()