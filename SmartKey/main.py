from collections import UserList
import tkinter as tk
from gui import LoginForm, UsersList

if __name__=="__main__":
    root= tk.Tk()
    root.title("SmartKey")
    root.geometry("450x800")

    login_form = LoginForm(root)

    #users_list = UsersList(root)

    root.mainloop()