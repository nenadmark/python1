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