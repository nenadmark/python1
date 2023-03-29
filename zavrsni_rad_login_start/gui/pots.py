import tkinter as tk

class PotsFrame:
    def __init__(self, parent, session):
        self.session = session
        self.frame = tk.Frame(parent)
        self.font = ("TimesNewRoman", 15, "bold")
        self.frame.config(bg="lightgreen")

        self.create_pots_frame()

    pots_data = [
    {
        'id': '001',
        'name': 'Pot 1',
        'plant_inside': 'Plant 1',
        'image_path': 'assets\pots\pot1_160x160.png'
    },
    {
        'id': '002',
        'name': 'Pot 2',
        'plant_inside': 'Plant 2',
        'image_path': 'assets\pots\pot2_160x160.png'
    },
    {
        'id': '003',
        'name': 'Pot 3',
        'plant_inside': 'Plant 3',
        'image_path': 'assets\pots\pot3_160x160.png'
    },
    {
        'id': '004',
        'name': 'Pot 4',
        'plant_inside': 'Plant 4',
        'image_path': 'assets\pots\pot4_160x160.png'
    },
    {
        'id': '005',
        'name': 'Pot 5',
        'plant_inside': 'Plant 5',
        'image_path': 'assets\pots\pot5_160x160.png'
    },
    {
        'id': '006',
        'name': 'Pot 6',
        'plant_inside': 'Plant 6',
        'image_path': 'assets\pots\pot6_160x160.png'
    }]

    def create_pots_frame(self):
        for i, pot in enumerate(self.pots_data):
            # Create a label to display the plant image
            image = tk.PhotoImage(file=pot['image_path'])
            image.configure(width=150, height=150)
            label_image = tk.Label(self.frame, image=image)
            label_image.image = image
            label_image.grid(row=i, column=0, padx=10, pady=10)
        
            # Create labels to display the plant name, humidity, and temperature
            label_name = tk.Label(self.frame, text=pot['id'])
            label_name.grid(row=i, column=1)
        
            label_humidity = tk.Label(self.frame, text=f'Name: {pot["name"]}')
            label_humidity.grid(row=i, column=2)
        
            label_temperature = tk.Label(self.frame, text=f'Plant inside: {pot["plant_inside"]}')
            label_temperature.grid(row=i, column=3)