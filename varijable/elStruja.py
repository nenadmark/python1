P = 1.3 #kW
t = 2 #h

cijena = 0.56 #HRK po satu

mjesecna_uporaba = t * 30

mjesecna_potrosnja = mjesecna_uporaba * P

mjesecni_trosak = mjesecna_potrosnja * cijena 

print("mjesecna potrosnja", mjesecna_potrosnja)
print("mjesecni trosak", mjesecni_trosak)
print("mjesecni trosak s pdv-om",mjesecni_trosak * 1.25)