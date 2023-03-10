import requests
import xmltodict
import tkinter as tk
#from tkinter import PhotoImage
#from PIL import ImageTk, Image


response = requests.get("https://vrijeme.hr/hrvatska_n.xml")
response_dict = xmltodict.parse(response.content)

response_temp = response_dict["Hrvatska"]["Grad"][-3]["Podatci"]["Temp"]
inside_temp = "21"

response_humidity = response_dict["Hrvatska"]["Grad"][-3]["Podatci"]["Vlaga"]
inside_humidity = "40"

response_pressure = response_dict["Hrvatska"]["Grad"][-3]["Podatci"]["Tlak"]
inside_pressure = "1022"

response_wind = response_dict["Hrvatska"]["Grad"][-3]["Podatci"]["VjetarBrzina"]
response_report = response_dict["Hrvatska"]["Grad"][-3]["Podatci"]["Vrijeme"]

class MeteoFrame:
    def __init__(self, parent):
        self.frame = tk.Frame(parent)

        self.create_temp_readings()
        self.create_humidity_readings()
        self.create_pressure_readings()
        self.create_wind_info()
        self.create_report()
        #self.picture_info()
       
    def create_temp_readings(self):
        self.inside_temp_label = tk.Label(self.frame, text=f"Inside temperature: {inside_temp}° C")
        self.inside_temp_label.grid(row=0, column=0, padx=5, pady=5)

        self.outside_temp_label = tk.Label(self.frame, text=f"Outside temperature: {response_temp}° C")
        self.outside_temp_label.grid(row=1, column=0, padx=5, pady=15)


    def create_humidity_readings(self):
        self.inside_humidity_label = tk.Label(self.frame, text=f"Inside humidity: {inside_humidity} %")
        self.inside_humidity_label.grid(row=2, column=0, padx=5, pady=5)

        self.outside_humidity_label = tk.Label(self.frame, text=f"Outside humidity: {response_humidity} %")
        self.outside_humidity_label.grid(row=3, column=0, padx=5, pady=15)

    
    def create_pressure_readings(self):
        self.inside_pressure_label = tk.Label(self.frame, text=f"Inside pressure: {inside_pressure} hPa")
        self.inside_pressure_label.grid(row=4, column=0, padx=5, pady=5)

        self.outside_pressure_label = tk.Label(self.frame, text=f"Outside pressure: {response_pressure} hPa")
        self.outside_pressure_label.grid(row=5, column=0, padx=5, pady=15)

    def create_wind_info(self):
        self.wind_info_text = tk.Label(self.frame, text=f"Brzina vjetra: {response_wind} m/s")
        self.wind_info_text.grid(row=6, column=0, padx=20, pady=20)
    
    def create_report(self):
        self.report_text = tk.Label(self.frame, text=f"Prognoza: {response_report} !")
        self.report_text.grid(row=7, column=0, padx=20, pady=20)

    #def picture_info(self):
        #photo = ImageTk.PhotoImage(Image.open('images\shorts.png'))
        #self.picture_info = tk.Label(self.frame, image=photo)
        #self.picture_info.grid(row=8, column=0, padx=20, pady=20)






