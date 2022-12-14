file_reader = open("datoteke\datoteka_uvod.txt", "r") #OPEn prima prvo path i onda access rights koji mogu biti r - read. w- write, a- append

tekst = file_reader.read() # read cita taj file
file_reader.close() # close zatvara taj file 
print(tekst)


file_writer = open("datoteke\ime.txt", "w")
ime = input("Unesite svoje ime: \t")
file_writer.write(ime)
file_reader.close()