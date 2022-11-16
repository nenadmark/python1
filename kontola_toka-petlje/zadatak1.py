# PRVI ZADATAK
# kreirati listu s brojevima od 1 do 30 i ispisati sve brojeve djeljive s 3, 6 i 9

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 , 20 , 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

for i in num:
    if i % 3 == 0:
        print(f"broj {i} je dijeljiv s 3")

    if i % 6 == 0:
        print(f"broj {i} je dijeljiv s 6")

    if i % 9 == 0:
        print(f"broj {i} je dijeljiv s 9")
print(":"*50)

numbers = []
for i in range(1, 31):
    numbers.append(i)

for i in numbers:
    #varijanta gdje provjeravamo je li broj djeljiv s 3 i 6 i 9
    #if i % 3 == 0 and i % 6 == 0 and i % 9 == 0:

    if i % 3 == 0:
        print(f"broj {i} je dijeljiv s 3")
    if i % 6 == 0:
        print(f"broj {i} je dijeljiv s 6")
    if i % 9 == 0:
        print(f"broj {i} je dijeljiv s 9")



# DRUGI ZADATAK
# napisati program koji provjerava pripada li unesena rijec vrsti rijeci palindrom
#palindrom je rijec koja se jednako pise i cita s lijeva na desno i vice versa

# doraditi program da unosimo rijeci sve dok se ne unese rijec koja je palindrom

word_in = input("PALINDROM - Unesite rijec:")
word_backwards = word_in [::-1]

if word_in.lower() == word_backwards.lower():
    print(f"Rijec {word_in} je Palindrom!")
else:
    print(f"Rijec {word_in} nije Palindrom!")
print(":"*100)


# DRUGI ZADATAK
### PRIMJER S PLOCE
rijec = input("PALINDROM - Unesite rijec:").lower()
rijec_kao_lista = []
# umjesto ove for petlje mozemo staviti:
# lista_rijeci = list(rijec)
for slovo in rijec:
    rijec_kao_lista.append(slovo)

kopirana_lista = rijec_kao_lista.copy()
rijec_kao_lista.reverse()

if kopirana_lista == rijec_kao_lista:
    print(f"Riječ {rijec} je palindrom.")
else:
    print(f"Riječ {rijec} nije palindrom.")
print(":"*100)



# TRECI ZADATAK
# program koji provjerava jesu li dvije rijeci anagrami
word1_list = []
word2_list = []
word1 = input("ANAGRAM - Unesi prvu rijec: ").lower()
word2 = input("ANAGRAM - Unesi drugu rijec: ").lower()
word1 = word1.replace(" ", "")
word2 = word2.replace(" ", "")

print(word1)
print(word2)

for i in word1:
    word1_list.append(i)
for i in word2:
    word2_list.append(i)

word1_list.sort()
word2_list.sort()
if word1_list == word2_list:
    print("Anagrams!")
else:
    print("NOT Anagrams!")

print(":"*100)


#TRECI ZADATAK - primjer s ploce:
