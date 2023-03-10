import tkinter as tk
from tkinter import ttk
import sqlalchemy as db

from gui.gui import LoginForm
from gui.plants import PlantsFrame
from gui.pots import PotsFrame

#print("bla")

# tu kreiramo glavnu stvar 
if __name__=="__main__":

    db_engine = db.create_engine("sqlite:///plants_pots.sqlite", echo=True)
    Base.metadata.create_all(db_engine, checkfirst=True)

    Session = sessionmaker(bind=db_engine)
    session = Session()










    # ovdje kreiramo root, parenta za tkinter
    root= tk.Tk()
    root.title("Login App")

    login_form = LoginForm(root)
    # TU INSTANCIRAMO FORMU IZ GUI.PY
    # login forma prilikom instanciranja prima root windowa iz gui.py

    notebook = ttk.Notebook(root)
    notebook.grid(row=0, column=0)

                                #(notebook, session)
    plants_frame = PlantsFrame(notebook, session)
    pots_frame = PotsFrame(notebook)


    notebook.add(plants_frame.frame, text="Plants")
    notebook.add(pots_frame.frame, text="Pots")

    # mainloop zapravo u loopu prikazuje sve na ekran
    root.mainloop()

# ako smo pokrenuli skriptu u pythonu, onda python stavlja __name__ kao da je __main__
# ovaj print u ifu ce se pokrenuti samo ako pokrenemo main kao skripu
# POKRECEMO MAIN.PY 
# elemente GUI-a dodajemo u gui.py