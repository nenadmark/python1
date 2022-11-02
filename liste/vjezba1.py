# lista u kojoj ce biti svaki treci broj izmedju 1 i 30

list1 = []
for i in range (1, 30, 3):
    list1.append(i)
print("1. - Zadatak:: ", list1)


# kreirati listu na temelju liste iz pretkohnog zadatka tako da vrijednost svakog elementa uvecamo za dvostruko

list2 = list1.copy()
list2_2 = []
for i in list2:
    double = i * 2
    list2_2.append(double)
print("2. - Zadatak:: ", list2_2)


# napisati program koji izpisuje zbroj svakih elemenata iz liste u drugom zadatku
list3 = list2_2.copy()
sum = sum(list3)
print("3. - Zadatak:: ", sum)

#primjer s ploce
zbroj = 0
for i in list3:
    zbroj += i
print("3. - Zadatak:: ", zbroj)


# napisati program koji kod korisnika trazi unos jednog broja koji zeli izbaciti iz liste it zadatka 3, te onda ispisati uneseni broj te ispisati novo stanje liste.
print("4. - Zadatak:: ", list3)
broj = int(input("Unesite broj: "))
list3.remove(broj)
print(list3)