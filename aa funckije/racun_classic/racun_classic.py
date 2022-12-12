racun_1 = {
    "receipt_number": "R-1-2022-12-06",
    "receipt_date": "06.12.2022",
    "items": {
        "laptop": 2500.99,
        "keyboard": 199.99,
        "mouse": 149.99,
        },
    "tax": 0.25
}

racun_2 = {
    "receipt_number": "R-1-2022-12-06",
    "receipt_date": "06.12.2022",
    "items": {
        "laptop": 2500.99,
        "keyboard": 199.99,
        "mouse": 149.99,
        },
    "tax": 0.25
}

def total_bill(racun):
    items1 = racun["items"]
    #total_notax = 0
    total_notax = sum(items1.values())
    #for cijena in items.values():
        #total_notax += cijena
    
    total_tax = total_notax * (1 + racun_1["tax"])

    return total_tax


def kreiranje_racuna():
    broj_racuna = input("Unesite broj racuna: ")
    datum_izdavanja = input("Unesite datum izdavanja racuna: ")
    stavke = {}
    while True:
        naziv_stavke = input("Unesite naziv stavke: ")
        cijena_stavke = float(input("Unesite cijenu stavke: "))
        stavke[naziv_stavke] = cijena_stavke
        nastavak = input("Želite li unijeti jos stavki (y/n)").lower()
        if nastavak in ["y", "yes"]:
            continue
        else:
            break
    pdv = 0.25

    return {
        "receipt_number": broj_racuna,
        "receipt_date": datum_izdavanja,
        "items": stavke,
        "tax": 0.25
    }

total_finished_1 = total_bill(racun_1)
print(total_finished_1)