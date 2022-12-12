
class Osoba:
    def __init__(self, ime, OIB, adresa=None) -> None:
        self.ime = ime
        self.OIB = OIB
        self.adresa = adresa
        print(f"Kreirana nova osoba {self.ime}")

    def __str__(self) -> str:
        # ako pozovemo ovu klasu u print metodi ovo tu cemo dobiti u ispisu
        return self.ime

        # ovo je nasa metoda koja nam provjerava jel OIB ispravan
    def ispravan_oib(self):
        if len(self.OIB) == 11 and self.OIB.isdigit():
            return True
        return False

    def ispis_podataka(self):
        print(f"Ime: {self.ime}")
        print(f"Prezime: {self.prezime}")
        
        if self.ispravan_oib():
            print(f"OIB je u ispravnom formatu ({self.OIB})")
        else:
            print(f"OIB nije u ispravnom formatu ({self.OIB})")

        if self.adresa:
            print(f"Osoba zivi na adresi: {self.adresa}")
        else:
            print(f"Osoba nema adresu.")


## klasa FizickaOsoba nasljedjuje klasu Osoba
# parent je Osoba
# child je FizickaOsoba
class FizickaOsoba(Osoba):
    def __init__(self, ime, OIB, prezime, adresa=None) -> None:
        super().__init__(ime, OIB, adresa)
        # super().__init__ nam:
        # sa superom kazemo pythonu, ovu metodu koji sam ti naveo nakon supera zovi od parent klase ! 
        # parent klasa nam ima ime, oib, adresa
        
        # NAŠA init metoda u fizickaOsoba poziva super.init od parent klase, tako smo u child klasi dobili sve iz init metode parenta 
        #nakon toga postavljamo i dodatnu varijablu koja je nova u child klasi
        self.prezime = prezime
        print(f"Kreirana nova fizicka osoba. {self.ime}")

    # kada zelimo da child klasa pozove iste metode iz parent klase

    # string reprezentacija ovog naseg objekta, u nasem slucaju vraca ime i prezime
    #def __str__(self) -> str:
        #return f"{self.ime} {self.prezime}"


    #ova metoda nam ispisuje podatke koje imamo (koje joj dolje prosljedjujemo) 
    def ispis_podataka(self):
        print(f"Ime: {self.ime}")
        print(f"Prezime: {self.prezime}")
        
        if self.ispravan_oib():
            print(f"OIB je u ispravnom formatu ({self.OIB})")
        else:
            print(f"OIB nije u ispravnom formatu ({self.OIB})")

        if self.adresa:
            print(f"Osoba zivi na adresi: {self.adresa}")
        else:
            print(f"Osoba nema adresu.")


class Tvrtka(Osoba):
        # konstruktor metoda se zove kada pozoveno novuz instancu ove klase
    def __init__(self, ime, OIB, adresa=None, br_zaposlenih=None, lista_zaposlenika=None, odgovorna_osoba=None) -> None:
        # uvijek vecinom stavljati u init onaj None, te nakon toga radimo provjeru (INACE)
            # if lista_zaposlenika is None:
                # lista_zaposlenika = []
        super().__init__(ime, OIB, adresa)
        self.br_zaposlenih = br_zaposlenih
        self.lista_zaposlenika = lista_zaposlenika
        self.odgovorna_osoba = odgovorna_osoba

        if self.lista_zaposlenika:
            self.br_zaposlenih = len(self.lista_zaposlenika)
        else:
            self.br_zaposlenih = 0

    def ispis_podataka(self):
        print(f"Ime: {self.ime}")
        
        if self.ispravan_oib():
            print(f"OIB je u ispravnom formatu ({self.OIB})")
        else:
            print(f"OIB nije u ispravnom formatu ({self.OIB})")
        if self.adresa:
            print(f"tvrtka je registrirana na adresi {self.adresa}")
        if self.odgovorna_osoba:
            print(f"Odgovorna osoba je {self.odgovorna_osoba}")
        if self.br_zaposlenih:
            print(f"Broj zaposlenih je: {self.br_zaposlenih}")



#osoba = Osoba("Osoba 1", "12345678910")  #ovo je instanciranje objekta iz klase
#fizicka_osoba = FizickaOsoba("Fizička", "01987654321", "Osoba", "ilica 123")  #ovo je instanciranje objekta iz klase

#print(osoba)
#print(fizicka_osoba)

#tvrtka1 = Tvrtka("Tvrtka", "123123", "ilica 1", "nenadnenadanovic") #ovo je instanciranje objekta iz klase
#tvrtka1.ispis_podataka()

#tvrtka1 = Tvrtka("Tvrtka", "123123", "ilica 1", 2, ["prvi Zaposlenik", "drugi", "treci"], "nenadnenadanovic") #ovo je instanciranje objekta iz klase
#tvrtka1.ispis_podataka()





# ISINSTANCE()
# ako zelim provjeriti dali je neki objekt instanca neke klase:
# isinstance(objekt za koji zelimo znati jeli instanca klase, klasa za koju ovo provjeravamo)
#if isinstance(tvrtka1, Tvrtka):
    #print("tvrtka1 je instanca klase Tvrtka")
#else:
    #print("tvrtka1 nije instanca klase Tvrtka")

        

#osoba1 = Osoba("Pero", "Perić", "1234567891", "Ilica 1")
#osoba2 = Osoba("Ivan", "Ivić", "12345678910")

#print(osoba1.ispravan_oib())
#print(osoba2.ispravan_oib())
#print(f"/"*50)
#print(osoba1.ispis_podataka())
#print(osoba2.ispis_podataka())


# child klasa naslijedi sve o parenta, child klasa moze imati nesto svoje, a ako nema neke metode koja parent klasaima, nasljedjuje ih automatski

# ako u child klasi zovemo neku metodu koja je u parentu, python prbvo gleda u klasi samog objekta, ako postoji zove metodu, ako ne postoji ide na parenta gore i onda tamo trazi metodu, ako taj parent nema tu metodu python onda ide jos gore na drugog parenta i trazi tu metodu

# class a 
    #def bla

# class b
    #def bla

# class c
    # def bla

# class c(a,b)
    # ova klasa nasljedjuje stvari po redu kako smo ih nasljedili
    # prvoi gleda i nasljedjuje stvari iz klase a pa onda i klase b


# ZADATAK: 
# instancirati 5 novih osoba te ih spremiti u listu 
# instancirati 1 tvrtku tako da odgovorna osoba bude prva osoba iz liste iznad
# a zaposlenici preostale 4 osoba iz gornje lista 

osobe = []
osoba1 = Osoba("osoba1", "12345678910", "Ilica 1")
osoba2 = Osoba("osoba2", "12345678910", "Ilica 2")
osoba3 = Osoba("osoba3", "12345678910", "Ilica 3")
osoba4 = Osoba("osoba4", "12345678910", "Ilica 4")
osoba5 = Osoba("osoba5", "12345678910", "Ilica 5")
osobe = [osoba1, osoba2, osoba3, osoba4, osoba5]

tvrtka_1 = Tvrtka(
    "tvrtka1",
    "12312312332",
    "Osječka 1",
    2,
    [],
    [osobe[0]])
print(tvrtka_1)



