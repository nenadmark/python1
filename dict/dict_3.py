from cmath import inf


prog_jez = {
    "naziv": "python",
    "tezina": "srednje",
    "verzija": 3.11,
    "godina_nastanka": 1994
}

print(prog_jez["naziv"])
#print(prog_jez("godina_nastanka"))

prog_jez.pop("naziv")
print(prog_jez)

info = {
    "autor": "Guido Van Rossum",
    "znacajke": ["fleksibilnost", "citljivost", "primjena"],
    "naziv": "python3"
}


print("::::::::::::::::::::::::::::::::::::::::::::::::")

# ako zelimo extendati jednu listu na drugu, TU NE KORISTIMO EXTEND NEGO UPDATE ! 

# ako u originalnom dictu imamo isti kljuc sa starom vrijednosti, sto znaci da novi dict ima novu vrijednost tog keya, nakon update-a prvi dict ce imati novu vrijednost uz taj key

# ako postoji element s istim keyem azurira mu vrijednost


prog_jez.update(info)
print(prog_jez)

print("::::::::::::::::::::::::::::::::::::::::::::::::")

info_2 = info
print(info_2)

info_2["naziv"] = "Python3.11"
print(info)
#print(info_2)

print("::::::::::::::::::::::::::::::::::::::::::::::::")
# COPY FUNKCIJA , radi kopiju originalnog dicta
#info3.copy(info)
#print(info3)

# CLEAR funkcija cleara sve iz dictionary-a
#info_2.clear()
#print(info_2)

print("::::::::::::::::::::::::::::::::::::::::::::::::")

print(info)

print(info["znacajke"][2])