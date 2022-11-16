# DRUGI ZADATAK
# napisati program koji provjerava pripada li unesena rijec vrsti rijeci palindrom
#palindrom je rijec koja se jednako pise i cita s lijeva na desno i vice versa

#BONUS ZADATAK: nakon sto se unese rijec koja je palindrom, pitati korisnika zeli li unijeti novu rijec ili ne 

while True:
    word_in = input("PALINDROM - Unesite rijec: ").lower()
    word_backwards = word_in [::-1]
    if word_in == word_backwards:
        print(f"Rijec {word_in} je Palindrom!")
        nova_igra = input("Zelis li ponoviti igru? (y/n): ").lower()
        if nova_igra in ["y", "yes"]:
            continue
        else:
            break
    else:
        print(f"Rijec {word_in} nije Palindrom!")
        continue



# DRUGI ZADATAK
### PRIMJER S PLOCE
rijec = input("PALINDROM - 2 - Unesite rijec: ").lower()
rijec_kao_lista = []
# umjesto ove for petlje mozemo staviti:
# lista_rijeci = list(rijec)
for slovo in rijec:
    rijec_kao_lista.append(slovo)

kopirana_lista = rijec_kao_lista.copy()
rijec_kao_lista.reverse()

if kopirana_lista == rijec_kao_lista:
    print(f"Riječ {rijec} je palindrom.")
else:
    print(f"Riječ {rijec} nije palindrom.")
print(":"*100)


# doraditi ovaj program iz zadatak1.py da unosimo rijeci sve dok se ne unese rijec koja je palindrom