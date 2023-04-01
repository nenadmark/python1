import tkinter as tk
#from models.models_1 import Plants

class PlantsFrame:
    def __init__(self, parent, session):
        self.session = session
        self.frame = tk.Frame(parent)
        self.font = ("TimesNewRoman", 10, "bold")
        self.frame.config(bg="skyblue2")

        self.create_plants_frame()

    plant_data = [
    {
        'id': 'PL 1',
        'name': 'Crocatum',
        'sort': 'Piper',
        'humidity': '50',
        'temperature': '22',
        'p_code': 'PT 1',
        'image_path': 'assets\\thumbs\plants\Crocatum_130x130.png'
    },
    {
        'id': 'PL 2',
        'name': 'Deliciosa Variegated',
        'sort': 'Monstera',
        'humidity': '60%',
        'temperature': '23°C',
        'p_code': 'PT 2',
        'image_path': 'assets\\thumbs\plants\Deliciosa_Variegated_130x130.png'
    },
    {
        'id': 'PL 3',
        'name': 'Fernwood Mikado',
        'sort': 'Sansevieria',
        'humidity': '55%',
        'temperature': '21°C',
        'p_code': 'PT 3',
        'image_path': 'assets\\thumbs\plants\Fernwood_Mikado_130x130.png'
    },
    {
        'id': 'PL 4',
        'name': 'McDowell',
        'sort': 'Philodendron',
        'humidity': '70%',
        'temperature': '25°C',
        'p_code': 'PT 4',
        'image_path': 'assets\\thumbs\plants\McDowell_1_130x130.png'
    },
    {
        'id': 'PL 5',
        'name': 'Paraiso Verde',
        'sort': 'Philodendron',
        'humidity': '45%',
        'temperature': '20°C',
        'p_code': 'PT 5',
        'image_path': 'assets\\thumbs\plants\Paraiso_Verde_130x130.png'
    },
    {
        'id': 'PL 6',
        'name': 'White Wizard',
        'sort': 'Philodendron',
        'humidity': '65%',
        'temperature': '24°C',
        'p_code': 'PT 6',
        'image_path': 'assets\\thumbs\plants\White_Wizard_130x130.png'
    }]

    def create_plants_frame(self):
        #plants = self.session.query(Plants).all()

        #print(Plants)


        for i, plant in enumerate(self.plant_data):
            self.plant_frame = tk.LabelFrame(
                self.frame, text=f'{plant["id"]} - {plant["name"]}', width=450, height=140,
                font=self.font, bd=4)
            self.plant_frame.grid(row=i, column=0, padx=5, pady=1, ipadx=60, ipady=1, sticky="w")
            self.plant_frame.config(bg="skyblue2")

            image = tk.PhotoImage(file=plant['image_path'])
            image.configure(width=120, height=120)
            label_image = tk.Label(self.plant_frame, image=image, font=self.font)
            label_image.image = image
            label_image.grid(row=i, column=0, padx=5, pady=5)
        
            label_name = tk.Label(self.plant_frame, text=plant['sort'], font=self.font)
            label_name.grid(row=i, column=1, padx=5, ipadx=5)
            label_name.config(bg="skyblue2")
        
            label_humidity = tk.Label(self.plant_frame, text=f'Humidity: {plant["humidity"]}', font=self.font)
            label_humidity.grid(row=i, column=2, padx=5)
            label_humidity.config(bg="skyblue2")
        
            label_temperature = tk.Label(self.plant_frame, text=f'Temperature: {plant["temperature"]}', font=self.font)
            label_temperature.grid(row=i, column=3, padx=5)
            label_temperature.config(bg="skyblue2")