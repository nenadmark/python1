# ponudi funkcionalnosti smart kuce
#
# Baze: 

import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import tkinter as tk
from tkinter import ttk

from models.base import Base
from models.appliance import TV, Refrigerator, Speakers, Lights
from gui.appliances import ApplianceFrame
from gui.lights import LightsFrame
from gui.sounds import SoundsFrame
from models.Meteo.meteo import MeteoFrame



if __name__ == "__main__":
    db_engine = db.create_engine("sqlite:///SmartHome.sqlite", echo=True)
    Base.metadata.create_all(db_engine, checkfirst=True)

    Session = sessionmaker(bind=db_engine)
    session = Session()

    #print(session.query(Room).first())

    root = tk.Tk()
    root.title("SmartHome")
    root.geometry("650x450")

    notebook = ttk.Notebook(root)
    notebook.grid(row=0, column=0)

    appliance_frame = ApplianceFrame(notebook, session)
    lights_frame = LightsFrame(notebook)
    sounds_frame = SoundsFrame(notebook)
    meteo_frame = MeteoFrame(notebook)

    notebook.add(appliance_frame.frame, text="Appliances")
    notebook.add(lights_frame.frame, text="Lights")
    notebook.add(sounds_frame.frame, text="Sounds")
    notebook.add(meteo_frame.frame, text="Weather")

    root.mainloop()