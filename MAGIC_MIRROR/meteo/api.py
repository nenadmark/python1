import requests

class Meteo:
    def __init__(self):
        self.url = f"https://api.open-meteo.com/v1/forecast?latitude=45.81&longitude=15.98&current_weather=True"
    
    def retrieve_data(self):
        response = requests.get(self.url)

        return response.json()

    def get_Meteo_values(self):
        meteo_data = self.retrieve_data()

        meteo_temp = meteo_data["current_weather"]["temperature"]
        meteo_wind_speed = meteo_data["current_weather"]["windspeed"]
        meteo_wind_dir = meteo_data["current_weather"]["winddirection"]
        meteo_weather_code = meteo_data["current_weather"]["weathercode"]

        #print(f"THE DATA IS: {meteo_data}")

        return (meteo_temp, meteo_wind_speed, meteo_weather_code, meteo_wind_dir)