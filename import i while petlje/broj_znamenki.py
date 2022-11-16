# program trazi unos cijelog broja i ispisuje koliko uneseni broj ima znamenki

num_in = int(input("Unesi cijeli broj"))
lenght = len(str(num_in))
print(lenght)


broj_znamenki = 0
while num_in > 0:
    num_in = num_in // 10
    broj_znamenki +=1
print(broj_znamenki)