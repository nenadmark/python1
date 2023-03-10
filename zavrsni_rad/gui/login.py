import tkinter as tk
from tkinter import messagebox

from sqlalchemy import delete
from crud import login_user, get_all_users, delete_user


class UsersList:
    def __init__(self, root):
        self.root = root
        self.listbox = tk.Listbox(self.root)
        self.listbox.grid(row=3, column=0, padx=10, pady=10)
        self.load_users()

        self.user_to_delete = None

    def load_users(self):
        users = get_all_users()

        for i, user in enumerate(users):
            frame = tk.Frame(self.listbox)
            frame.grid(row=i, column=0)
            user_label = tk.Label(frame, text=user.name)
            user_label.grid(row=i, column=0)
            delete_button = tk.Button(frame, text="delete", command=lambda: self.on_delete(user)) 
            #chekiraj lambda funbkcije, za kako proslijediti commandu funkciju
            delete_button.grid(row=i, column=1)
            self.listbox.insert(i, frame)

    #lambda funkcija
    # anonimne funkcije, funkcija koja se poziva samo na jednom mjestu
    # lambda funkcija nema svoje ime, zove se samo tamo gdje smo ju zvali 
    def on_delete(self, user):
        delete_user(user.id) # brise iz baze
        print("Korisnik obrisan iz baze.")


# ako je gui malo kompliciraniji onda bolje da slazemo ovo sve u klasu
class LoginForm:
    def __init__(self, root):
        self.root = root

        self.email_label = tk.Label(self.root, text="Email:", font=("Arial", 15))
        self.email_label.grid(row=0, column=0, padx=10, pady=10)

        self.email_entry = tk.Entry(self.root)
        self.email_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = tk.Label(root, text="Password:", font=("Arial", 15))
        self.password_label.grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = tk.Button(root, text="Login", command=self.on_login)  # login buttoin namjestiti da bude disabled sve dok ne upisem osifru ili username
        self.login_button.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        """self.login_label = tk.Label(root, text="login", )
        self.login_label.grid(row=3, column=1, padx=10, pady=10, columnspan=2)"""
    
    def on_login(self):
        email_login = self.email_entry.get()
        password_login = self.password_entry.get()
        user = login_user(email_login, password_login)

        if user:
            if user.is_admin:
                users_list = UsersList(self.root)
            else:
                messagebox.showinfo("Success.", f"Welcome {user.name}")
        else:
            messagebox.showerror("Fail.", f"Wrong email or password")





