osoba = {
    "ime": "Ivica",
    "prezime": "Ivicevic",
    "grad": "Zagreb"
}

# pristup
#print(osoba["ime"])


# dodavanje novog keya
osoba["datum"] = "01.01.0101"
#print(osoba)


# pristup i mijenjanje vrijednosti
osoba["ime"] = "ANA"
#print(osoba)


#GET - trazi key value kao prvi parametar, ako ga nema onda mozemo prosljediti drugi parametar koji vraca u slucaju da prvi ne postoji
print(osoba.get("imee", "grad"))


#svakako mozemo iterirati kroz dict, pristupiti i keyu i valuesu
for i in osoba:
    print(f"{i} = {osoba[i]}")


#prolazak po KEYEVIMA
for i in osoba.keys():
    print(i)


#prolazak po VALUESIMA
for i in osoba.values():
    print(i)


#prolazak po PAROVIMA
for i in osoba.items():
    print(i)

    #NE KORISTI SE BAS OVAKO:
    #pristup KEYU u tom PARU
    print(i[0])

    #pristup VALUE u tom PARU
    print(i[1])

# KORISTI SE VISE OVAKO:
for key, value in osoba.items():
    print(i)

    #pristup KEYU u tom PARU
    print(key)

    #pristup VALUE u tom PARU
    print(value)