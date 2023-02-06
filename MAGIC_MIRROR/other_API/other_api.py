from logging import root
import requests

class Covid:
    def __init__(self):
        self.url = "https://covid-193.p.rapidapi.com/statistics"
        self.querystring = {"country":"Croatia"}
        self.headers = {
	        "X-RapidAPI-Key": "7989735847mshdebe1660860efd1p15f9ccjsn7dd3d67423ac",
	        "X-RapidAPI-Host": "covid-193.p.rapidapi.com"
        }
    
    def retrieve_data(self):
        response = requests.request("GET", self.url, headers=self.headers, params=self.querystring)
        response_json = response.json()

        return response_json
    
    def get_Covid_values(self):
        covid_data = self.retrieve_data()
        covid_country = covid_data["parameters"]["country"]
        covid_population = covid_data["response"][0]["population"]
        covid_cases_total = covid_data["response"][0]["cases"]["total"]
        covid_deaths_total = covid_data["response"][0]["deaths"]["total"]
        covid_cases_new = covid_data["response"][0]["cases"]["new"]

        return (covid_country, covid_population, covid_cases_total, covid_deaths_total, covid_cases_new)