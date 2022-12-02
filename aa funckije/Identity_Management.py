#funkcionalnosti programa:
# - predefinirani administrator sustava koji moze dodati nove korisnike u sustav, azurirati i brisati postojece
# - svaki korisnik ima: ime, prezime, korisnicko ime (UserName) i zaporku (Password)
# - zaporka (Password) mora imati minimalno 10 znakova
# - korisnicko ime (UserName) mora biti jedinstveno

# - Uspjesna prijava na ekranu ispisuje: "Dobro došli, {ime} {prezime}"
# - moje smjernice: admin moze ispisati, editati i dodati ili brisati usere

#INPUT - login trazi username prvo pa onda password. 
# ako postoji par onda je login uspjesan 

import os
import time

user_list = {
    1: {'name': 'Nenad', 'lastname': 'Marković', 'UserName': 'nenadnenad', 'Password': 'mojasifra123'},
    2: {'name': 'Josip', 'lastname': 'Josipović', 'UserName': 'jos467', 'Password': 'josip123'},
    3: {'name': 'Ante', 'lastname': 'Antić', 'UserName': 'ante1', 'Password': 'ante234234'},
    4: {'name': 'Zoran', 'lastname': 'Zokić', 'UserName': 'zoka234876', 'Password': 'aaa09802134'},
    5: {'name': 'Ivan', 'lastname': 'Ivanović', 'UserName': 'ivan999ivan', 'Password': 'ivanivanivan333'},

    }

def screen_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def user_input():
    user_input_name = input("Input new user: Name: ")
    user_input_lastname = input("Input new user: Last Name: ")
    user_input_username = input("Input new user: Username: ")
    user_input_password = input("Input new user: Password: ")
    
    user_list_length = len(user_list) + 1
    print(user_list_length)
    user_list[user_list_length] = {
        'name': user_input_name,
        'lastname': user_input_lastname,
        'UserName': user_input_username,
        'Password': user_input_password
    }
    print("User added successfuly.")
    time.sleep(2)
    screen_clear()
    main_menu()

def user_delete():
    print(f"Choose the index of user you wish to delete.")
    user_idex_delete = int(input(": "))
    if user_idex_delete in user_list:
        user_list.pop(user_idex_delete)
        print(f"User [{user_idex_delete}] is deleted.")
    else:
        print("Index is not available.")
    time.sleep(2)
    screen_clear()    
    main_menu()

def display_users():
    print("#   Name     Last Name     User Name     Password")
    for i in user_list:
        print(f"{i} : {user_list[i]['name']}    {user_list[i]['lastname']}    {user_list[i]['UserName']}    {user_list[i]['Password']} ")
    main_menu()
    
def user_edit():
    print(f"Choose the index of user you wish to edit.")
    user_idex_edit = int(input(": "))
    user_edit_name = input("Input new value for 'Name': ")
    user_edit_lastname = input("Input new value for 'Last Name': ")
    user_edit_username = input("Input new value for 'User Name': ")
    user_edit_password = input("Input new value for 'Password': ")

    if user_edit_name != "":
        user_list[user_idex_edit]['name'] = user_edit_name
        print(f"User [{user_idex_edit}] has new 'Name' value")
    if user_edit_lastname != "":
        user_list[user_idex_edit]['lastname'] = user_edit_lastname
        print(f"User [{user_idex_edit}] has new 'Last Name' value")
    if user_edit_username != "":
        user_list[user_idex_edit]['UserName'] = user_edit_username
        print(f"User [{user_idex_edit}] has new 'User Name' value")
    if user_edit_password != "":
        user_list[user_idex_edit]['Password'] = user_edit_password
        print(f"User [{user_idex_edit}] has new 'Password' value")
    
    time.sleep(2)
    screen_clear()
    main_menu()

def main_menu():
    admin_user = False
    if admin_user == False:
        print("login: ")
        login_username = input("USERNAME: ")
        login_password = input("PASSWORD: ")
        if login_username == "admin" and login_password == "0000":
            print(f"User '{login_username}' logged in.")
            admin_user = True
        else:
            print(f"User '{login_username}' logged in.")
            admin_user = False

    print("*"*50)
    print("Choose your option: ")
    print("1 - (admin) Input new user")
    print("2 - Show users")
    print("3 - (admin) Edit user")
    print("4 - (admin) Delete user")
    print("5 - Exit")
    print("*"*50)

    key_options = input(": ")
    print("*"*50)
    if key_options == "1" and admin_user:
        user_input()
    elif key_options == "2":
        display_users()
    elif key_options == "3" and admin_user:
        user_edit()
    elif key_options == "4" and admin_user:
        user_delete()
    elif key_options == "5":
        exit()
    else:
        print("Invalid input")
        screen_clear()
        main_menu()
main_menu()