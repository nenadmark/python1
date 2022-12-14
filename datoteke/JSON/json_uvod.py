from ast import Pass
import json
from re import A

korisnik = {
    "ime": "Pero",
    "prezime": "Peric",
    "adresa": "ilica01",
    "telefon": "123123123",
    "omiljene_boje": ["crvena", "plava"]
}
#print(json.dump(korisnik))





"""
with open("user.json", "w") as file_writer:
    korisnik_str = json.dumps(korisnik)
    file_writer.write(korisnik_str)
    
"""

with open("\datoteke\JSON\user.json", "w") as file_writer:
    json.dump(korisnik, file_writer)
