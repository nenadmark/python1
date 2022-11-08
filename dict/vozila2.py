vozila = [
    {
        "id": "1",
        "tip": "Kamion",
        "proizvodjac": "Iveco",
        "registarska_oznaka": "OS 001 ZZ",
        "godina_prve_registracije": "2015",
        "cijena_eur": "45.000,00 €"
    },
        {
        "id": "2",
        "tip": "Kamion",
        "proizvodjac": "Iveco",
        "registarska_oznaka": "OS 002 ZZ",
        "godina_prve_registracije": "2015",
        "cijena_eur": "47.000,00 €"
    },
        {
        "id": "3",
        "tip": "Tegljač",
        "proizvodjac": "MAN",
        "registarska_oznaka": "RI 001 ZZ",
        "godina_prve_registracije": "2018",
        "cijena_eur": "78.000,00 €"
    },
        {
        "id": "4",
        "tip": "Tegljač",
        "proizvodjac": "MAN",
        "registarska_oznaka": "RI 002 ZZ",
        "godina_prve_registracije": "2020",
        "cijena_eur": "98.000,00 €"
    },
        {
        "id": "5",
        "tip": "Kombi",
        "proizvodjac": "Mercedes Benz",
        "registarska_oznaka": "ST 001 ZZ",
        "godina_prve_registracije": "2013",
        "cijena_eur": "12.000,00 €"
    },
        {
        "id": "6",
        "tip": "Kombi",
        "proizvodjac": "Volkswagen",
        "registarska_oznaka": "ST 002 ZZ",
        "godina_prve_registracije": "2021",
        "cijena_eur": "35.000,00 €"
    },
        {
        "id": "7",
        "tip": "Dostavno vozilo",
        "proizvodjac": "Volkswagen",
        "registarska_oznaka": "ZG 001 ZZ",
        "godina_prve_registracije": "2010",
        "cijena_eur": "9.000,00 €"
    },
        {
        "id": "8",
        "tip": "Dostavno vozilo",
        "proizvodjac": "Volkswagen",
        "registarska_oznaka": "ZG 002 ZZ",
        "godina_prve_registracije": "2010",
        "cijena_eur": "9.300,00 €"
    },
]

print(f"ID  TIP    Proizvođač    Registarska Oznaka    Godina prve registracije    Cijena u EUR")
print("________________________________________________________________________________________")
for i, value in enumerate(vozila):
    print(f"{vozila[i]['id']}    {vozila[i]['tip']}      {vozila[i]['proizvodjac']}      {vozila[i]['registarska_oznaka']}     {vozila[i]['godina_prve_registracije']}     {vozila[i]['cijena_eur']}")