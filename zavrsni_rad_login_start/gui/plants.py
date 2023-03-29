import tkinter as tk

class PlantsFrame:
    def __init__(self, parent, session):
        self.session = session
        self.frame = tk.Frame(parent)
        self.font = ("TimesNewRoman", 15, "bold")
        self.frame.config(bg="lightblue")

        self.create_plants_frame()

    plant_data = [
    {
        'name': 'Plant 1',
        'humidity': '50%',
        'temperature': '22°C',
        'image_path': 'assets\plants\plant1_160x160.png'
    },
    {
        'name': 'Plant 2',
        'humidity': '60%',
        'temperature': '23°C',
        'image_path': 'assets\plants\plant2_160x160.png'
    },
    {
        'name': 'Plant 3',
        'humidity': '55%',
        'temperature': '21°C',
        'image_path': 'assets\plants\plant3_160x160.png'
    },
    {
        'name': 'Plant 4',
        'humidity': '70%',
        'temperature': '25°C',
        'image_path': 'assets\plants\plant4_160x160.png'
    },
    {
        'name': 'Plant 5',
        'humidity': '45%',
        'temperature': '20°C',
        'image_path': 'assets\plants\plant5_160x160.png'
    },
    {
        'name': 'Plant 6',
        'humidity': '65%',
        'temperature': '24°C',
        'image_path': 'assets\plants\plant6_160x160.png'
    }]

    def create_plants_frame(self):
        for i, plant in enumerate(self.plant_data):
            # Create a label to display the plant image
            image = tk.PhotoImage(file=plant['image_path'])
            image.configure(width=150, height=150)
            label_image = tk.Label(self.frame, image=image)
            label_image.image = image
            label_image.grid(row=i, column=0, padx=10, pady=10)
        
            # Create labels to display the plant name, humidity, and temperature
            label_name = tk.Label(self.frame, text=plant['name'])
            label_name.grid(row=i, column=1)
        
            label_humidity = tk.Label(self.frame, text=f'Humidity: {plant["humidity"]}')
            label_humidity.grid(row=i, column=2)
        
            label_temperature = tk.Label(self.frame, text=f'Temperature: {plant["temperature"]}')
            label_temperature.grid(row=i, column=3)