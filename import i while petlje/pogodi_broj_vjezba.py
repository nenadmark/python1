# from bla import *
# from bla2 import *
# OVO NE KORISTITI JER JE ZEZNUTO! 
 

# import random
# random_broj = random.randint(1, 100)
# print(random_broj)


from random import randint
import random



"""
if random_broj < 50:
    print(f"Broj je manji od 50")
    if random_broj < 25:
        print("Broj je manji od 25")
        if random_broj % 2 == 0:
            print(f"Broj je Paran!")
            if random_broj < 12:
                print(f"Broj je Paran i manji od 12!")
            elif random_broj > 12:
                print(f"Broj je Paran i veci od 12 a manji od 25!")
                if random_broj > 20:
                    print("Broj je Paran i veci od 20 a manji od 25!")
                elif random_broj < 20:
                    print("Broj je Paran i veci od 12 a manji od 20!")

            else:
                print(f"Broj je Neparan i veci od 12 a manji od 25!")
                if random_broj < 12:
                    print(f"Broj je Neparan i manje od 12!")
    elif random_broj > 25:
        print(f"Broj je manji od 50 a veci od 25")

else:
    print(f"Broj je veci od 50")
"""


## primjer s ploce, ovo gore si failao jako
#import random
random_broj = randint(1, 100)
broj_pokusaja = 0
max_broj_pokusaja = 9

while broj_pokusaja <= max_broj_pokusaja:
    broj_pokusaja += 1
    broj = int(input("Unesite broj: "))
    if broj == random_broj:
        print(f"Cestitam, pogodili ste broj, {random_broj} iz {broj_pokusaja} pokusaja.")
        break
    elif broj < random_broj:
        print(f"Trazeni broj je veci od {broj}. Ostalo vam je jos {9 - broj_pokusaja} pokusaja.")
    else:
        print(f"Trazeni broj je manji od {broj} Ostalo vam je jos {9 - broj_pokusaja} pokusaja.") 
