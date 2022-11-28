# napisati krizic kruzic

import os

polje_na_ploci = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
igrac = 1
status = -1
broj_poteza = 0

def provjeri_status():

    if polje_na_ploci[1] == polje_na_ploci[2] == polje_na_ploci[3]:
        return 1
    elif polje_na_ploci[4] == polje_na_ploci[5] == polje_na_ploci[6]:
        return 1
    elif polje_na_ploci[7] == polje_na_ploci[8] == polje_na_ploci[9]:
        return 1
    elif polje_na_ploci[1] == polje_na_ploci[4] == polje_na_ploci[7]:
        return 1
    elif polje_na_ploci[2] == polje_na_ploci[5] == polje_na_ploci[8]:
        return 1
    elif polje_na_ploci[3] == polje_na_ploci[6] == polje_na_ploci[9]:
        return 1
    elif polje_na_ploci[1] == polje_na_ploci[5] == polje_na_ploci[9]:
        return 1
    elif polje_na_ploci[3] == polje_na_ploci[5] == polje_na_ploci[7]:
        return 1
    #elif broj_poteza == 9:
        #return 0
    elif (
        polje_na_ploci[1] != 1 and polje_na_ploci[2] != 2 and      polje_na_ploci[3] != 3 and polje_na_ploci[4] != 4 and polje_na_ploci[5] != 5 and polje_na_ploci[6] != 6 and polje_na_ploci[7] != 7 and polje_na_ploci[8] != 8 and polje_na_ploci[9] != 9):
        return 0
    else:
        return -1


def provjeri_potez(potez_igraca):
    if potez_igraca not in polje_na_ploci or potez_igraca == 0:
        return False
    else:
        return True


def iscrtaj_plocu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('\n\n\t ALGEBRA')
    print('\n\tKrizic Kruzic\n\n')

    print('IGRAC 1 (X)  -  IGRAC 2 (O)' ) 
    print()

    print('\t     |     |     ' )
    print('\t ' ,polje_na_ploci[1] ,' | ' ,polje_na_ploci[2] ,' |  ' ,polje_na_ploci[3] )

    print('\t_____|_____|_____' )
    print('\t     |     |     ' )

    print('\t ' ,polje_na_ploci[4] ,' | ' ,polje_na_ploci[5] ,' |  ' ,polje_na_ploci[6] )

    print('\t_____|_____|_____' )
    print('\t     |     |     ' )

    print('\t ' ,polje_na_ploci[7] ,' | ' ,polje_na_ploci[8] ,' |  ' ,polje_na_ploci[9] )

    print('\t     |     |     ' )
iscrtaj_plocu()

while status == -1:
    #iscrtaj_plocu()
    if igrac == 1:
        oznaka_igraca = "X"
    else:
        oznaka_igraca = "O"

    potez_igraca = int(input(f"IGRAČ {oznaka_igraca} Unesi broj: "))
    potez_ispravan = provjeri_potez(potez_igraca)

    if potez_ispravan:
        #broj_poteza += 1
        polje_na_ploci[potez_igraca] = oznaka_igraca
        status = provjeri_status()
        iscrtaj_plocu()
        
        if status == 0:
            print("Neriješeno!")
        elif status == 1:
            print(f"Pobijedio je igrac sa oznakom {oznaka_igraca}")

        igrac *= -1
    else:
        print("Krivi unos")
        continue
