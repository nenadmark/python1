import tkinter as tk
from tkinter import messagebox

from sqlalchemy import delete
from models.crud_login import login_user, get_all_users, delete_user


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
                #users_list = UsersList(self.root)
                print("OK LOGIN")
            else:
                messagebox.showinfo("Success.", f"Welcome {user.name}")
        else:
            messagebox.showerror("Fail.", f"Wrong email or password")