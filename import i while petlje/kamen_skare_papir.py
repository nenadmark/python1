import random
# paper wins rock
# scissors wins paper
# stone wins scissors

pc_num = random.randint(1, 3)
pc_kamen = False
pc_skare = False
pc_papir = False
if pc_num == 1:
    pc_kamen = True
elif pc_num == 2:
    pc_skare = True
elif pc_num == 3:
    pc_papir = True

print("pc_kamen", pc_kamen)
print("pc_skare", pc_skare)
print("pc_papir", pc_papir)

me_num = int(input("1 - KAMEN\n2 - SKARE\n3 - PAPIR\nUnesi svoj korak:"))
me_kamen = False
me_skare = False
me_papir = False

if me_num == 1:
    me_kamen = True
elif me_num == 2:
    me_skare = True
elif me_num == 3:
    me_papir = True

if me_kamen:
    if pc_kamen:
        print("Tie!")
    elif pc_skare:
        print("Human Wins!")
    elif pc_papir:
        print("PC Wins with paper!")
elif me_skare:
    if pc_kamen:
        print("PC Wins with stone!")
    if pc_skare:
        print("Tie!")
    elif pc_papir:
        print("Human Wins!")
elif me_papir:
    if pc_kamen:
        print("Human Wins!")
    if pc_skare:
        print("PC Wins with scissors!")
    elif pc_papir:
        print("Tie!")


