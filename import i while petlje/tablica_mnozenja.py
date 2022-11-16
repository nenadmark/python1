# napisi program koji ispisuje tablicu mnozenja
# korisnik moze unijeti do kojeg broja zeli ispis tablice.

num = int(input("Unesi broj: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        print(i * j, end=" ")
    print()