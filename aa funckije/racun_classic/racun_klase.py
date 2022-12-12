import datetime as dt
from time import strptime
# izrada racun_classic.py ali tu cemo koristiti klase ! 

class Stavka:
    def __init__(self, naziv, cijena):
        self.naziv = naziv
        self.cijena = cijena

    def __repr__(self) -> str:
        # skoro isto kao i __str__
        return self.naziv

class Racun(Stavka):
    def __init__(self, trenutak_izdavanja=None, lista_stavki=None):
        if lista_stavki is None:
            lista_stavki = []
        self.lista_stavki = lista_stavki
        if trenutak_izdavanja:
            self.datum_vrijeme_izdavanja = trenutak_izdavanja
        else:
            self.datum_vrijeme_izdavanja = dt.datetime.now()
        self.broj_racuna = self.generiraj_br_racuna()
        self.pdv = 0.25
        self.ukupan_iznos = self.izracunaj_ukupan_iznos()

    def __str__(self) -> str:
        return self.broj_racuna
    
    def generiraj_br_racuna(self):
        # br_racuna = R-2022-12-11-00 (ovo zadnje su sekunde)
        datum_str = self.datum_vrijeme_izdavanja.strftime("%Y-%m-%d-%S")
        return f"R-{datum_str}"

    def izracunaj_ukupan_iznos(self):
        zbroj = 0
        for i in self.lista_stavki:
            zbroj += i.cijena
        return zbroj * (1 + self.pdv)

    def ispisi_racun(self):
        formatirani_datum = self.datum_vrijeme_izdavanja.strftime("%m.%d.%Y %H:%M:%S")

        print(f"Račun br. {self.broj_racuna}")
        print(f"Datum izdavanja: {formatirani_datum}")
        print("Stavke: ")
        for i, stavka in enumerate(self.lista_stavki):
            print(f"\t {i+1}. {stavka.naziv} \t {stavka.cijena} kn")
        print(f"Ukupan iznos: {self.ukupan_iznos:.2f} kn")
        print("/*\*"*20)
                
mis = Stavka("Miš", 99.99)
tipkovnica = Stavka("tipkovnica", 149.99)
monitor = Stavka("Monitor 28", 2499.99)

racun1 = Racun(lista_stavki=[mis, tipkovnica, monitor])

#print(racun1.ispisi_racun())

jucer = dt.datetime(year=2022, month=12, day=11, hour=15, minute=30, second=45)
racun_jucer = Racun(trenutak_izdavanja=jucer, lista_stavki=[tipkovnica])
#print(racun_jucer.ispisi_racun())



# ispisivanje sljedecih racuna:
# 5 racuna za prethodnih 5 dana
# 1 racun za danasnji dan
# 5 racuna za iducih 5 dana
pocetni_datum = dt.datetime.now() - dt.timedelta(days=5)
datumi = []
for i in range(0, 11):
    datum = pocetni_datum + dt.timedelta(days=i)
    datumi.append(datum)

    edited_racun = Racun(trenutak_izdavanja=datum, lista_stavki=[mis, tipkovnica, monitor])
    #print(edited_racun.ispisi_racun())



# unosenje custom datuma za izradu nasih racuna
# OVAJ TRY I EXCEPT PONOVI ! 
# try izvodi varijablu jedin ako je input u ovom slucaju dobar
# ako nije : 
# except se izvodi ! 

datum_korisnik = input("Unesite datum i vrijeme racuna: ")
try:
    custom_date = dt.datetime.strptime(datum_korisnik, "%d.%m.%Y %H:%M:%S")
except:
    print("Datum je u pogresnom formatu.")


#TRY EXCEPT PRIMJER ZASTO NIJE DOBAR ! (((ALI OVISI O SLUCAJU)))
# zelimo greske 
try:
    lista1 = [1,2]
    rijecnik_1 = {"a": 1}

    print(lista1[3]) #ovaj faila pa cijeli try faila, kasnije onda ne znamo gjde je greska bila 
    print(rijecnik_1["b"])

except:
    print("dogodila se greska")

#ali mozemo mu zadati tocno koje greske nam javlja 
# javljat ce nam prvu gresku koja se dogodila, javi except koji javlja gresku i nista vise u try bloku se ne izvrsava ! 

#except IndexError:
    #print("pristup elementu liste koji ne postoji.")

#except KeyError:
    #print("pristup kljucu liste koji ne postoji.")
