import tkinter as tk


#from PIL import imageTk, Image


#from tkinter import PhotoImage

#from assets import succulent_1


class PlantsFrame:
    def __init__(self, parent, session):
        self.session = session
        self.frame = tk.Frame(parent)
        self.font = ("TimesNewRoman", 15, "bold")
        self.frame.config(bg="skyblue")
        self.create_plants_frame()


    plant_data = [
    {
        'name': 'Plant 1',
        'humidity': '50%',
        'temperature': '22°C',
        'image_path': 'assets\mythic-ninja-alocasia-alocasia-reginula-jewel-alocasia-proven-winners_17329.jpg'
    },
    {
        'name': 'Plant 2',
        'humidity': '60%',
        'temperature': '23°C',
        'image_path': 'assets\chamaedorea-elegans-indoor-palm-alamy-stock-photo_12384.jpg'
    },
    {
        'name': 'Plant 3',
        'humidity': '55%',
        'temperature': '21°C',
        'image_path': 'path/to/plant3.jpg'
    },
    {
        'name': 'Plant 4',
        'humidity': '70%',
        'temperature': '25°C',
        'image_path': 'path/to/plant4.jpg'
    },
    {
        'name': 'Plant 5',
        'humidity': '45%',
        'temperature': '20°C',
        'image_path': 'path/to/plant5.jpg'
    },
    {
        'name': 'Plant 6',
        'humidity': '65%',
        'temperature': '24°C',
        'image_path': 'path/to/plant6.jpg'
    }]

    def create_plants_frame(self):
        for i, plant in enumerate(self.plant_data):
            # Create a label to display the plant image
            image = tk.Image(file=plant['image_path'])
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




"""


import tkinter as tk

# Define a list of dictionaries containing plant data
plant_data = [
    {
        'name': 'Plant 1',
        'humidity': '50%',
        'temperature': '22°C',
        'image_path': 'path/to/plant1.jpg'
    },
    {
        'name': 'Plant 2',
        'humidity': '60%',
        'temperature': '23°C',
        'image_path': 'path/to/plant2.jpg'
    },
    {
        'name': 'Plant 3',
        'humidity': '55%',
        'temperature': '21°C',
        'image_path': 'path/to/plant3.jpg'
    },
    {
        'name': 'Plant 4',
        'humidity': '70%',
        'temperature': '25°C',
        'image_path': 'path/to/plant4.jpg'
    },
    {
        'name': 'Plant 5',
        'humidity': '45%',
        'temperature': '20°C',
        'image_path': 'path/to/plant5.jpg'
    },
    {
        'name': 'Plant 6',
        'humidity': '65%',
        'temperature': '24°C',
        'image_path': 'path/to/plant6.jpg'
    }
]

# Create the main window
root = tk.Tk()

# Create a frame to hold the plant thumbnails and labels
frame = tk.Frame(root)
frame.pack()

# Loop through the plant data and create a thumbnail and labels for each plant
for i, plant in enumerate(plant_data):
    # Create a label to display the plant image
    image = tk.PhotoImage(file=plant['image_path'])
    label_image = tk.Label(frame, image=image)
    label_image.image = image
    label_image.grid(row=i, column=0, padx=10, pady=10)
   
    # Create labels to display the plant name, humidity, and temperature
    label_name = tk.Label(frame, text=plant['name'])
    label_name.grid(row=i, column=1)
   
    label_humidity = tk.Label(frame, text=f'Humidity: {plant["humidity"]}')
    label_humidity.grid(row=i, column=2)
   
    label_temperature = tk.Label(frame, text=f'Temperature: {plant["temperature"]}')
    label_temperature.grid(row=i, column=3)

# Start the main event loop
root.mainloop()



"""








# old code:

"""


        # Create left and right frames
        left_frame = tk.Frame(self.frame, width=200, height=400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        right_frame = tk.Frame(self.frame, width=650, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        # Create frames and labels in left_frame
        tk.Label(left_frame, text="Plant Image").grid(row=0, column=0, padx=5, pady=5)

        # load image to be "edited"
        image = tk.PhotoImage(file="assets\succulent_1.png")
        original_image = image.subsample(3,3)  # resize image using subsample
        tk.Label(left_frame, image=original_image).grid(row=1, column=0, padx=5, pady=5)

        # Display image in right_frame
        tk.Label(right_frame, image=image).grid(row=0,column=0, padx=5, pady=5)

        # Create tool bar frame
        tool_bar = tk.Frame(left_frame, width=180, height=185)
        tool_bar.grid(row=2, column=0, padx=5, pady=5)

        # Example labels that serve as placeholders for other widgets
        tk.Label(tool_bar, text="info1", relief=tk.RAISED).grid(row=0, column=0, padx=5, pady=3, ipadx=10)  # ipadx is padding inside the Label widget

        # Example labels that could be displayed under the "Tool" menu
        tk.Label(tool_bar, text="info1").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(tool_bar, text="info1").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(tool_bar, text="info1").grid(row=3, column=0, padx=5, pady=5)


"""
