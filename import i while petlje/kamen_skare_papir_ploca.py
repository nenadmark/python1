## primjer s ploce puno je kraci ! 
import random 
odabir_racunala = random.randint(1, 3)
print("1 - PAPIR")
print("2 - KAMEN")
print("3 - SKARE")

while True:
    odabir_korisnika = int(input("Unesite jednu od mogucih opcija: "))
    if odabir_korisnika in [1, 2, 3]:
        break

if odabir_korisnika == odabir_racunala:
    print("NERIJESENO, odabrali ste isto sto i racunalo!")
elif odabir_korisnika == 1 and odabir_racunala == 2 or odabir_korisnika == 2 and odabir_racunala == 3 or odabir_korisnika == 3 and odabir_racunala == 1:
    print(f"Pobjedili ste. Racunalo je odabralo {odabir_racunala}")
else:
    print(f"Izgubili ste. Racunalo je odabralo {odabir_racunala}")