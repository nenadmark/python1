import tkinter as tk

class PlantsFrame:
    def __init__(self, parent, session):
        self.session = session
        self.frame = tk.Frame(parent)
        self.font = ("TimesNewRoman", 10, "bold")
        self.frame.config(bg="skyblue2")

        self.create_plants_frame()

    plant_data = [
    {
        'name': 'Plant 1',
        'humidity': '50%',
        'temperature': '22°C',
        'image_path': 'assets\\thumbs\plants\Crocatum_130x130.png'
    },
    {
        'name': 'Plant 2',
        'humidity': '60%',
        'temperature': '23°C',
        'image_path': 'assets\\thumbs\plants\Deliciosa_Variegated_130x130.png'
    },
    {
        'name': 'Plant 3',
        'humidity': '55%',
        'temperature': '21°C',
        'image_path': 'assets\\thumbs\plants\Fernwood_Mikado_130x130.png'
    },
    {
        'name': 'Plant 4',
        'humidity': '70%',
        'temperature': '25°C',
        'image_path': 'assets\\thumbs\plants\McDowell_1_130x130.png'
    },
    {
        'name': 'Plant 5',
        'humidity': '45%',
        'temperature': '20°C',
        'image_path': 'assets\\thumbs\plants\Paraiso_Verde_130x130.png'
    },
    {
        'name': 'Plant 6',
        'humidity': '65%',
        'temperature': '24°C',
        'image_path': 'assets\\thumbs\plants\White_Wizard_130x130.png'
    }]

    def create_plants_frame(self):
        for i, plant in enumerate(self.plant_data):

            self.plant_frame = tk.LabelFrame(
                self.frame, text=plant['name'], width=450, height=140,
                font=self.font)
            self.plant_frame.grid(row=i, column=0, padx=10, pady=1, ipadx=60, ipady=1)
            self.plant_frame.config(bg="skyblue2")

            image = tk.PhotoImage(file=plant['image_path'])
            image.configure(width=120, height=120)
            label_image = tk.Label(self.plant_frame, image=image, font=self.font)
            label_image.image = image
            label_image.grid(row=i, column=0, padx=7, pady=7)
        
            label_name = tk.Label(self.plant_frame, text=plant['name'], font=self.font)
            label_name.grid(row=i, column=1, padx=10)
            label_name.config(bg="skyblue2")
        
            label_humidity = tk.Label(self.plant_frame, text=f'Humidity: {plant["humidity"]}', font=self.font)
            label_humidity.grid(row=i, column=2, padx=10)
            label_humidity.config(bg="skyblue2")
        
            label_temperature = tk.Label(self.plant_frame, text=f'Temperature: {plant["temperature"]}', font=self.font)
            label_temperature.grid(row=i, column=3, padx=10)
            label_temperature.config(bg="skyblue2")