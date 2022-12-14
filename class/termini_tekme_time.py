import datetime as dt
from dateutil.rrule import *
from dateutil.parser import *


# svaka druga srijeda i nedjelja u tekucoj godini

lista_datuma = list(
    rrule(
        WEEKLY,  # ponavljamo datume na tjednoj bazi
        interval=2,    # trebamo svaki drugi interval (svaki drugi tjedan)
        #count=8, # count, koliko instanci datuma zelimo, ako je none onda se generiraju dok se pravilo ponavljanja ne prekrsi(datumski)
        wkst=MO, # pocetak tjedna nam je monday
        byweekday=(WE,SU), # trebamo srijedu i nedjelju
        dtstart=parse("20220101T090000"), #pocetni datum
        until=parse("20221230T090000") #pocetni datum
    )
)
    
  
for i in lista_datuma:
    print(i.strftime("%A, %d.%m.%Y %H:%M:%S"))
