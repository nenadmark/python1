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
#print(lista1[0:60])
print(lista1[0:60:2])
print(lista1[50::2])
#print(lista1[:50:-1])
#print(lista1[:])

# BRISANJE IZ LISTE
lista5 = [1, 2, 3]
#lista_5.clear()

#lista_5.remove(2)  TU BRISEMO PRVU VREIJEDNOST "2" , nakon ovoga lista_5 = [1, 3]


# COPY - bolje koristiti COPY umjesto lista1 = lista5
lista5_1 = lista5.copy()

lista5[0] = 5
#lista1 = lista5
#print(lista1)
print(lista5)


# COUNT 
list10 = [5, 7, 5, 10, 11, 11, 12]
print(list10.count(5))

# INDEX funkcija
print(list10.index(5))

# RAZLIKA IZMEDJU EXTENDA I APPENDA
list11 = [7, 2, 5, 6, 7, 1, 3, 8]
#list10.append(list11)  ## sada je list10 = [5, 7, 5, 10, 11, 11, 12, [7, 2]]
#print(list10[7][1])

#list10.extend(list11) ## sada je list10 = [5, 7, 5, 10, 11, 11, 12, 7, 2]
print(list10)

#INSERT
list10.insert(3, 6)


#POP
#list11 = [7, 2]
list11.pop(1)    
print(list11)

# SORT
list11.sort()
#list11.sort(reverse=True)
print(list11)

# REVERSE
list11.reverse()
print(list11)