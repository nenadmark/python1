# hello world

def poz():
    print("Hello World")

poz()


def ime(name):
    print("ime je: ", name)    

name = input("Unesi ime: ")
ime(name)

def ispis(arg, arg2):
# def ispis(arg: str)  < tu ako stavimo : i onda str ili int ili nesto drugo, ova funkcija uzima samo string ili int ili nesto drugo
    """
    OVO JE OPIS NASE FUNKCIJE KOJI JE UPISAN OVDJE U DOCSTRING ILITI (""" """)
    """
    print(arg, arg2)
    parametar = "3" # ovo je parametar koji je definiran u funkciji


#ispis("123") # tu je "123" argument ( argument saljemo funkciji kada ju zovemo)
t1 = 1
t2 = 2
ispis(t1, t2)
rez = ispis(t1, t2) # ako ovo vidimo da varijabla zove funkciju, onda znamo da ta funkcija vraca nesto a to je u ovom slucaju NONE (jer nismo definirali raturn u definiciji funkcije)


# funkcija prima dva broja i vraca njihoh zbroj
def zbroj(prvi, drugi):
    return prvi + drugi

rezultat = zbroj(8, 4)
print(rezultat) # print 15

print(":"*50)
def zbroj1(prvi, drugi):
    print(prvi + drugi)

rezultat1 = zbroj1(8, 4)
print(rezultat1)

print(help(ispis))


print(":"*50)
def ispis_imena(a1="Pero"): # ovako dodajemo defaultnu vrijednost argumentu u slucaju da pri pozivanju funkcije ne prosljedjujemo svoj argument
    print(a1)

ispis_imena("aaaaaaaaaaaaaa") # ovako zovemo ovu funkciju ali joj ipak saljemo argument, u ovom slucaju "Pero" argument se override-a s vrijednosti "aaaaaaaaaaaaaa"


def ime_prezime(ime="Pero", prezime="Peric"):
    print(f"Osoba se zove {ime} i preziva {prezime}")

ime_prezime(2) # ako zovemo funkciju koja ima dva defaultna argumenta, a saljemo joj samo jedan. taj prvi ce se ispisati a drugi po defaultu

ime_prezime(ime, "a") # tu sam random skuzio da ako samo stavimo ime argumenta, dobijemo za "ime" ovo > <function ime at 0x0000024B5AC3C5E0> 

ime_prezime(prezime = "Mirkic") # a m,ozemo i direktno slati argument tu ... sto znaci ako imenujemo argument i dodamo mu vrijednost, taj argument dobija tu dodanu vrijednost
# AKO PRI ZVANJU NE NAZIVAMO ARGUMENT KOJI SALJEMO VEC SAMO SALJEMO VRIJEDNOSTI, ONDA SE GLEDA KOJIM REDOSLJEDOM SMO SLALI te VRIJEDNOSTI TE SE ONE TA ASSIGNAJU PO REDU PO ARGUMENTIMA

#ime_prezime(prezime = "Mirkic", "Mirko")
# OVAKO NE MOZEMO ZVATI FUNKCIJU I SLATI JOJ ARGUMENTE , NE MOZEMO KOMBINIRATI POSITIONAL ARGUMENTE I NAME-ane ARGUMENTE
# ZNACI KORISTITI JEDNO ILI DRUGO



# A R G S 
def zbroj_3(*num): # ova funkcija moza primati proizvoljni broj argumenata
    # sve argumente ova funkcija sprema u TUPLE
#def zbroj_3(*args): # OVAK CE SE TAJ ARGUMENT ZVATI UVIJEK
    """
    vraca zbgoj svih predanih argumenata
    Primjer:
    zbroj_3(1)  -> 1
    zbroj_3(1, 2)  -> 3
    zbroj_3(1, 2, 3)   -> 6
    """
    print(num[0])
    print(num[1])
    print(num[2])
    zbroj = 0
    for i in num:
        zbroj += i

    return zbroj

print(zbroj_3(1, 6, 9))




# kada defaultnoj vrijednosti dodamo None, cinimo ovaj argument opcionalnim (znaci da ga mozemo koristiti a i ne moramo)
#def ispis_osobe(ime=None):



# K W A R G S 
# KEYWORD ARGUMENTS : 
# ova funkcija moza primati proizvoljni broj argumenata
# ali argumente ne sprema u tuple vec u dictionary
# kod kwargs ne moramo brinuti o poretku prosljedjivanja argumenata

def ispis_osobe(**kwargs):

    """
    ispis podataka o osobi
    moguci podaci su:
        -ime
        -prezime
        -godina rodjenja
        -mjesto stanovanja
    """

    if "ime3" in kwargs.keys():
        print(f"Osoba se zove {kwargs['ime3']}")
    if "prezime" in kwargs.keys():
        print(f"Osoba se preziva {kwargs['prezime']}")
    if "mjesto_stanovanja" in kwargs.keys():
        print(f"Osoba zivi u {kwargs['mjesto_stanovanja']}")
    if "godina" in kwargs.keys():
        print(f"Osoba je rodjena {kwargs['godina']}")

    print(":"*50)
    print(f"Osoba se zove {kwargs['ime3']} {kwargs['prezime']}, \n{kwargs['ime3']} zivi u {kwargs['mjesto_stanovanja']}, \na rodjen je {kwargs['godina']}")

ispis_osobe(ime3="Pero", prezime="Peric", godina="1995", mjesto_stanovanja="zg")



def ispis_osobe2(ime3, prezime, mjesto_stanovanja, godina):

    if ime3:
        print(f"Osoba se zove {ime3}")
    if prezime:
        print(f"Osoba se preziva {prezime}")
    if mjesto_stanovanja:
        print(f"Osoba zivi u {mjesto_stanovanja}")
    if godina:
        print(f"Osoba je rodjena {godina}")


    print(f"Osoba se zove {ime3} {prezime}, \n{ime3} zivi u {mjesto_stanovanja}, \na rodjen je {godina}")
    
ispis_osobe2(ime3="Pero", prezime="Peric", godina="1995", mjesto_stanovanja="zg")