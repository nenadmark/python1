# napisite aplikaciju koja trazi unos podataka:
# ime, prezime, telefon, adresa

# svakog korisnika zapisujemo u novi redak datoteke adresar.txt
# nakon svakog unosa pitati korisnika zelimo li novi unos ili zavrsiti program

"""
#                                  w - write
file_writer = open("datoteke\\adresar.txt", "w")
brojac = 0

while True:
    ime = input("Name: ")
    prezime = input("Last Name: ")
    broj = input("Number: ")
    adresa = input("Adress: ")
    brojac += 1

    file_writer.write(f"{ime};{prezime};{broj};{adresa} \n")

    user_q = input("Input new user (y) or exit (n) ?").lower()
    if user_q == "y":
        continue
    else:
        break

file_writer.close()
"""



# otvaranje datoteke u prvom i drugom primjeru na stari nacin


"""
#                                  a - append
file_writer = open("datoteke\\adresar.txt", "a")
brojac = 0

while True:
    ime = input("Name: ")
    prezime = input("Last Name: ")
    broj = input("Number: ")
    adresa = input("Adress: ")
    brojac += 1

    file_writer.write(f"{ime};{prezime};{broj};{adresa} \n")

    user_q = input("Input new user (y) or exit (n) ?").lower()
    if user_q == "y":
        continue
    else:
        break

file_writer.close()
"""




# WITH, otvaramo datoteku na noviji nacin 
# with kada koristimo ne treba nam close na kraju
"""
file_writer = open("datoteke\\adresar.txt", "a")
brojac = 0

while True:
    ime = input("Name: ")
    prezime = input("Last Name: ")
    broj = input("Number: ")
    adresa = input("Adress: ")
    brojac += 1




    # with "THIS" as "THIS":
        # radi ovo tu 
    #                                  a - append
    with open("datoteke\\adresar.txt", "a") as file_writer:
        file_writer.write(f"{ime};{prezime};{broj};{adresa} \n")




    user_q = input("Input new user (y) or exit (n) ?").lower()
    if user_q == "y":
        continue
    else:
        break
"""



# zelimo iz adresar.txt uzimati podatke i spremati red po red u nas list baza_podataka
database = []

class Korisnik:
    def __init__(self, name, last_name, number, adress):
      self.name = name
      self.last_name = last_name
      self.number = number
      self.adress = adress

    def __repr__(self) -> str:
        return f"{self.name} {self.last_name} {self.number} {self.adress}"

"""
with open("datoteke\\adresar.txt", "r") as file_reader:
    content = file_reader.read() # tu imamo samo string sada
users = content.split("\n")
print(users)
"""

with open("datoteke\\adresar.txt", "r") as file_reader:
    for line in file_reader:
        line = line.rstrip().split(";") # na kraju svakog reda smo imali \n pa s ovime micemo s kraja stringa whitespace

        user = Korisnik(
            name = line[0],
            last_name = line[1],
            number = line[2],
            adress = line[3],
        )
        database.append(user)

print(database)