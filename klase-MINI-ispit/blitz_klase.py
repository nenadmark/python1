#1 napisati klasu kolegij koja se sastoji od sljedecih atributa:
# naziv
# predavac
# broj sati
class Kolegij:
    def __init__(self, naziv, predavac, sati) -> None:
        self.naziv = naziv
        self.predavac = predavac
        self.sati = sati

#2 dovrsiti klasu predavac koja se sastoji od sljedecih atributa:
# ime
# prezime
# datum zaposlenja

class Predavac:
    def __init__(self, ime, prezime, datum):
        self.ime = ime
        self.prezime = prezime
        self.datum_zaposlenja = datum


#3 instancirati 2 ovjekta tipa predavac i 3 objekta tipa kolegij.
# atribut "predavac" klase kolegij treba biti objekt tipa predavac
predavac1 = Predavac("Fizika", "prof.Fizike", "160")
predavac2 = Predavac("Biologija", "prof.Biologije", "160")

kolegij1 = Kolegij("Fizika", "Marković ", "22.11.1995")
kolegij2 = Kolegij("Engleski", "Marković ", "22.11.2000")
kolegij3 = Kolegij("Talijanski", "Marković ", "22.11.2005")



#4 modificirati klasu oklegij tako da atribut predavac bude lista objekata tipa predavac te instancirati 2 nova objekta tipa kolegij
