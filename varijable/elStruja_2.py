#ako je snaga mikrovalne 1.3kw, cijena struje za 1kw je 0.95kn

#koliko kuna, mjesecno kosta uporaba mikrovalne ako se koristi 2 sata dnevno

t = 2 #h
P = int(input("Unesi snagu el. uredjaja: "))
cijena = int(input("Unesi cijenu el. energije: "))

mjesecna_uporaba = t * 30
mjesecna_potrosnja = mjesecna_uporaba * P
mjesecni_trosak = mjesecna_potrosnja * cijena 

print("mjesecna potrosnja je: ", mjesecna_potrosnja)
print("mjesecni trosak je: ", mjesecni_trosak)
print("mjesecni trosak s pdv-om je: ",mjesecni_trosak * 1.25)