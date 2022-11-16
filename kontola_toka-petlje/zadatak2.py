# unesi cijeli broj

broj = int(input("koliko ti se svidja Python od 1 do 5: "))

if broj == 1:
    print("1")
elif broj == 2:
    print("2")
elif broj == 3:
    print("3")
elif broj == 4:
    print("4")
elif broj == 5:
    print("5")
else:
    print("krivi unos")


#################
grades = [1, 2, 3, 4, 5]
broj2 = input("drugi dio: - koliko ti se svidja Python od 1 do 5: ")
for i in grades:
    if i == broj2:
        print(f"nasa ocjena je: {i}")
    else:
        print("krivi unos")

#primjer s ploce

grades1 = {
    "1": "Python vam se uopce ne svidja",
    "2": "Python vam se bas i ne svidja",
    "3": "Python vam se svidja tako - tako",
    "4": "Python vam se vidja",
    "5": "Python vam se bas jako svidja"
}

ocjena1 = input("Unesite ocjenu")
for key, value in grades1.items():
    if ocjena1 == key:
        print(value)

if ocjena1 not in grades1.keys():
    print("krivi unos")  



#################
if ocjena1 not in grades1.keys():
    print("Krivi unos")
else:
    print(grades1.ocjena1)