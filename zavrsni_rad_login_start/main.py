import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlalchemy as db

#from gui.login import LoginForm
from gui.plants import PlantsFrame
from gui.pots import PotsFrame

from models.models import Base
from models.crud_login import login_user

from sqlalchemy.orm import sessionmaker



class Login(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)

        self.root = root

        username_label = tk.Label(self, text="Username:")
        password_label = tk.Label(self, text="Password:")
        self.email_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self)
        submit = tk.Button(self, text="Login", command=self.login)

        username_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.email_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=10)
        password_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.password_entry.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
        submit.grid(row=2, column=1, sticky="e", padx=10, pady=10)

    def login(self):
        # if username and password are valid:
        email_login = self.email_entry.get()
        password_login = self.password_entry.get()
        user = login_user(email_login, password_login)

        if user:
            if user.is_admin:
                #users_list = UsersList(self.root)
                print("OK LOGIN")
                self.withdraw()
                self.root.deiconify()
                messagebox.showinfo("Success.", f"Welcome {user.name}")
            else:
                messagebox.showinfo("Error.", f"Wrong email or password")
        else:
            messagebox.showerror("Error.", f"Wrong email or password")

        #self.withdraw()
        #self.root.deiconify()

def main():
    root = tk.Tk()
    root.withdraw()
    root.resizable(False, False)
    root.configure(height=500, width=500)
    root.geometry("900x600")
    #root.config(bg="skyblue")

    root.title("PyPlant")

    db_engine = db.create_engine("sqlite:///plants_pots.sqlite", echo=True)
    Base.metadata.create_all(db_engine, checkfirst=True)

    Session = sessionmaker(bind=db_engine)
    session = Session()

    login_window =  Login(root)

    notebook = ttk.Notebook(root)
    notebook.grid(row=0, column=0)

    plants_frame = PlantsFrame(notebook, session)
    pots_frame = PotsFrame(notebook)

    notebook.add(plants_frame.frame, text="Plants")
    notebook.add(pots_frame.frame, text="Pots")

    root.mainloop()

if __name__ == "__main__":
    main()
