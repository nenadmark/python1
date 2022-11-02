lista1 = []
#print(type(lista1))

# APPEND
for i in range (1, 101):
    lista1.append(i)
#print(lista1)

#print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

lista2 = []
for i in range (0, 201, 2):
    lista2.append(i)
#print(lista2)

print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

# lista s brojevima od 100 do 0
lista3 = []
for i in range (100, 1, -10):
    lista3.append(i)
#print(lista3)


print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

# SLICE [START:STOP:STEP]
print(lista1[0:60])
print(lista1[0:60:2])
print(lista1[50::2])
print(lista1[:50:-1])
print(lista1[:])

# BRISANJE IZ LISTE
lista5 = [1, 2, 3]
#lista_5.clear()

#lista_5.remove()


# COPY - bolje koristiti COPY umjesto lista1 = lista5
lista5_1 = lista5.copy()

lista5[0] = 5
#lista1 = lista5
print(lista1)
print(lista5)



