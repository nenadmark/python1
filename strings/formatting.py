ime = "Pero"
prezime = "Peric"
godine = 20
zanimanje = "Developer"

#Pero ima 20 godina i on je developer

print("BOk", ime)

print("Bok {}. Kako si danas?".format(ime))

print("Bok {} {}. Kako si danas?".format(ime, prezime))



print("{} {} ima {} godina. On je {}".format(ime, prezime, godine, zanimanje))

#najkraci nacin
# F - STRING
print(f"{ime} {prezime} ima {godine} godina. On je {zanimanje}")