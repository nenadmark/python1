import datetime as dt
import os
import time

def pokreni_sat():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        trenutno_vrijeme = dt.datetime.now()
        formatirano = trenutno_vrijeme.strftime("%A, %d.%m.%Y %H:%M:%S")
        print("TIME: ", formatirano)
        time.sleep(1)

pokreni_sat()

