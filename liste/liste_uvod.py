print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

moja_lista = ["Pero", 20, True, "developer", "bla", False]
prazna_lista = []

print(moja_lista)

# lista sa brojevima od 1 do 5
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
brojevi = [1, 2, 3, 4, 5]
print(brojevi[0])
print(brojevi[4])
print(brojevi[-1])

print(len(brojevi))

print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")



osoba1 = ["Pero", "Peric", "Ilica 35", "Zagreb", "100000"]
# ako zelimo ispisati sve elemente iz liste
for i in osoba1:
    print(i)


print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")


# JAKO DOBAR NACIN ZA POMOCI SI OKO INDEXIRANJA I COUNTERA U FOR PETLJI
# 
for index, i in enumerate(osoba1):
    print(index, i)


print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
brojevi_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in brojevi_3:
    print(i)


print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")


