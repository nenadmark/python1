# trazimo unos cijelog broja i provjeravamo dali je broj prost ili ne

num = int(input("unesi broj: "))
#if num % num == 0 and num % 1 == 0:
    #print("broj je prost!")
#else:
    #print("broj nije prost")
"""
isprime = True # tu dodajemo flag
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            isprime = False
            break
    if isprime:
        print(f"Broj {num} je prost.")
    else:
        print(f"Broj {num} nije prost.")
else:
    print("Boj nije veci od 1.")
"""



if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f"Broj {num} nije prost.")
            break
    else:
        print(f"Broj {num} je prost.")




"""
for i in range (2, 5):
    print(i)
else:
    print("tu sam")
"""
# kod for else, else ce se izbjeci ako imamo break ( ako se cijeli for izvrsava ne zavrsavano u else)
# ako uvijet nije bio ispunjen za nijedan broj u nasem foru onda imamo else
# else se ne izvrsava ako imamo break u foru. te ako je on uzvrsen uspjesno
