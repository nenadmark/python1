"""
import tkinter as tk
from sqlalchemy.orm import sessionmaker
from models.appliance import TV


class ApplianceFrame:
    def __init__(self, parent, session):
        self.session = session
        self.frame = tk.Frame(parent)
        self.font = ("TimesNewRoman", 15, "bold")

    def create_tv_frame(self):
        #SELECT * FROM televisions;
        tv_devices = self.session.query(TV).all() #za svaki label radimo ispis iz baze podataka putem query-a

#Labeli koje unosimo ručno Name, Room, Manufacturer, Floor
        status_label = tk.Label(self.frame, text = "On/Off", font=self.font)
        status_label.grid(row=0, column=4, padx=10, pady=10)

#ispis iz liste objekata redak po redak za svaki objekt

        for id, tv in enumerate(tv_devices): #enumerate sprema indeks objekta i objekt, npr. 0,b:1,l:2,a
            # label za prikaz imena tv-a
            tv_name_label = tk.Label(self.frame, text=tv.name, font=self.font)
            tv_name_label.grid(row=id + 1, column=0, padx=10, pady=20)
#label za prikaz proizvođača uređaja

            tv_manufacturer_label = tk.Label(self.frame, text=tv.manufacturer)
            tv_manufacturer_label.grid(row=id + 1, column=1, padx=10, pady=20)


#label za prikaz sobe u kojoj je uređaj
            tv_room_label = tk.Label(self.frame, text=tv.manufacturer)
            tv_room_label.grid(row=id + 1, column=2, padx=10, pady=20)


#label za prikaz kata na kojem se nalazi pojedini uređaj ili soba u kojoj je uređaj
            tv_floor_label = tk.Label(self.frame, text=tv.room.floor)
            tv_floor_label.grid(row=id + 1, column=3, padx=10, pady=20)

#skracena of off funkcija i label za active stupac
            on_off = "ON" if tv.active else "OFF"
            tv_status_label = tk.Label(self.frame, text = on_off)
            tv_status_label.grid(row=id + 1, column=4, padx=10, pady=20)
"""

"""
#Ovo je kod prije zajedničkog rješenja

        self.create_living_room_label()
        self.create_living_room_button()
        self.create_bedroom_label()
        self.create_bedroom_button()
        self.create_kitchen_label()
        self.create_kitchen_button()
        self.create_toilet_label()
        self.create_toilet_button()


       
    def create_living_room_label(self):
        self.living_room_label = tk.Label(self.frame, text="Living room")
        self.living_room_label.grid(row=0, column=0, padx=10, pady=10)

    def create_bedroom_label(self):
        self.bedroom_label = tk.Label(self.frame, text="Bedroom")
        self.bedroom_label.grid(row=1, column=0, padx=10, pady=10)

    def create_kitchen_label(self):
        self.kitchen_label = tk.Label(self.frame, text="Kitchen")
        self.kitchen_label.grid(row=2, column=0, padx=10, pady=10)

    def create_toilet_label(self):
        self.toilet_label = tk.Label(self.frame, text="Toilet")
        self.toilet_label.grid(row=3, column=0, padx=10, pady=10)

    def create_living_room_button(self):
        self.living_room_button = tk.Button(self.frame, text="Appliances")
        self.living_room_button.grid(row=0, column=1, padx=10, pady=10)

    def create_bedroom_button(self):
        self.bedroom_button = tk.Button(self.frame, text="Appliances")
        self.bedroom_button.grid(row=1, column=1, padx=10, pady=10)

    def create_kitchen_button(self):
        self.kitchen_button = tk.Button(self.frame, text="Appliances")
        self.kitchen_button.grid(row=2, column=1, padx=10, pady=10)

    def create_toilet_button(self):
        self.toilet_button = tk.Button(self.frame, text="Appliances")
        self.toilet_button.grid(row=3, column=1, padx=10, pady=10)

"""



import tkinter as tk

from models.appliance import TV


class ApplianceFrame:
    def __init__(self, parent, session):
        self.session = session
        self.frame = tk.Frame(parent)
        self.font = ("TimesNewRoman", 15, "bold")
        self.create_tv_frame()
    
    def create_tv_frame(self):
        tv_devices = self.session.query(TV).all()

        name_label = tk.Label(self.frame, text="Name", font=self.font)
        name_label.grid(row=0, column=0, padx=10, pady=20)

        manufacturer_label = tk.Label(self.frame, text="Manufacturer", font=self.font)
        manufacturer_label.grid(row=0, column=1, padx=10, pady=20)

        room_label = tk.Label(self.frame, text="Room", font=self.font)
        room_label.grid(row=0, column=2, padx=10, pady=20)

        floor_label = tk.Label(self.frame, text="Floor", font=self.font)
        floor_label.grid(row=0, column=3, padx=10, pady=20)

        status_label = tk.Label(self.frame, text="On/Off", font=self.font)
        status_label.grid(row=0, column=4, padx=10, pady=20)

        for id, tv in enumerate(tv_devices):
            tv_name_label = tk.Label(self.frame, text=tv.name, font=self.font)
            tv_name_label.grid(row=id + 1, column=0, padx=10, pady=20)

            tv_manufacturer_label = tk.Label(self.frame, text=tv.manufacturer)
            tv_manufacturer_label.grid(row=id + 1, column=1, padx=10, pady=20)

            tv_room_label = tk.Label(self.frame, text=tv.room.name)
            tv_room_label.grid(row=id + 1, column=2, padx=10, pady=20)

            tv_floor_label = tk.Label(self.frame, text=tv.room.floor)
            tv_floor_label.grid(row=id + 1, column=3, padx=10, pady=20)

            on_off = "ON" if tv.active else "OFF"
            tv_status_label = tk.Label(self.frame, text=on_off)
            tv_status_label.grid(row=id + 1, column=4, padx=10, pady=20)