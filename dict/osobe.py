# napisati program koji ce od korisnika traiti unos podataka o 5 osoba

#svaka osoba treba imati sljedece podatke:
# ime
# prezime
# spol
# datum rodjenja
# mjesto rodjenja
# zanimanje

# nakon unesenih podataka progream treba ispisati podatke u sljedecem formatu:

# ********************
# OSOBA 1
# Ime: Maja
# Prezime: Majić
# Spol: Ž
# Datum rođenja: 01.01.1991
# Mjesto stanovanja: Osijek

OSOBE = [
    {
        "ime": "",
        "prezime": "",
        "spol": "",
        "datum_rodjenja": "",
        "mjesto_stanovanja": ""
    },
    {
        "ime": "",
        "prezime": "",
        "spol": "",
        "datum_rodjenja": "",
        "mjesto_stanovanja": ""
    },
    {
        "ime": "",
        "prezime": "",
        "spol": "",
        "datum_rodjenja": "",
        "mjesto_stanovanja": ""
    },
    {
        "ime": "",
        "prezime": "",
        "spol": "",
        "datum_rodjenja": "",
        "mjesto_stanovanja": ""
    },
    {
        "ime": "",
        "prezime": "",
        "spol": "",
        "datum_rodjenja": "",
        "mjesto_stanovanja": ""
    },
]
for i in range (0, 5):
    print("UNESI PODATKE ZA OSOBU", i+1)
    OSOBE[i]["ime"] = input("Unesi ime osobe:")
    OSOBE[i]["prezime"] = input("Unesi prezime osobe:")
    OSOBE[i]["spol"] = input("Unesi spol osobe:")
    OSOBE[i]["datum_rodjenja"] = input("Unesi datum rođenja osobe:")
    OSOBE[i]["mjesto_stanovanja"] = input("Unesi Mjesto stanovanja osobe:")

for i in range (0, 5):
    print("*"*20)
    print(f"Ime osobe broj {i+1} je: {OSOBE[i]['ime']}")
    print(f"Prezime osobe broj {i+1} je: {OSOBE[i]['prezime']}")
    print(f"Spol osobe broj {i+1} je: {OSOBE[i]['spol']}")
    print(f"Datum rođenja osobe broj {i+1} je: {OSOBE[i]['datum_rodjenja']}")
    print(f"Mjesto rođenja osobe broj {i+1} je: {OSOBE[i]['mjesto_stanovanja']}")