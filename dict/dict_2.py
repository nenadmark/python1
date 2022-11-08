osoba = {
    "ime": "Ivo",
    "prezime": "Ivic",
    "adresa": {
        "ulica": "Ilica",
        "broj": 1,
        "grad": "Zagreb",
        "postanski_broj": 1000
    },
    "boje": ["crvena", "plava", "zelena"],
    "clanovi_obitelji": [
        {
            "ime": "Ivana",
            "prezime": "Ivic",
            "srodstvo": "supruga"
        },
        {
            "ime": "Ivan",
            "prezime": "Ivic",
            "srodstvo": "sin"
        }
    ]
}
#kako pristupiti
# zelimo dobiti ispois u sljedecem obliku
# IVica Ivic stanuje na sljedecoj adresi:
# Ilica 1, 10000, Zagreb
#Ima 3 omiljene boje, a to su crvena, plava i zelena.

print(f"{osoba['ime']} {osoba['prezime']} stanuje na sljedecoj adresi: \n{osoba['adresa']['ulica']}, {osoba['adresa']['broj']}, {osoba['adresa']['grad']}, {osoba['adresa']['postanski_broj']}. \nIma tri omiljene boje, a to su {osoba['boje'][0]}, {osoba['boje'][1]} i {osoba['boje'][2]}. \nClanovi obitelji su {osoba['clanovi_obitelji'][0]['ime']} {osoba['clanovi_obitelji'][0]['prezime']} - {osoba['clanovi_obitelji'][0]['srodstvo']}, te {osoba['clanovi_obitelji'][1]['ime']} {osoba['clanovi_obitelji'][1]['prezime']} - {osoba['clanovi_obitelji'][1]['srodstvo']}")