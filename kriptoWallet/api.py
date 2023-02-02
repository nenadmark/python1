import requests

# https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=EUR
#response = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=USD,EUR")
#values = response.json()
#print(values["BTC"]["EUR"])


class Crypto:
    def __init__(self, currency, value):
        self.url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={currency}&tsyms={value}"
    
    def retrieve_data(self):
        response = requests.get(self.url)

        return response.json()

    def get_Crypto_values():
        btc_to_eur = Crypto("BTC", "EUR")
        btc_to_eur_data = btc_to_eur.retrieve_data()
        btc_to_eur_data_value = btc_to_eur_data.values()

        eth_to_eur = Crypto("ETH", "EUR")
        eth_to_eur_data = eth_to_eur.retrieve_data()
        eth_to_eur_data_value = eth_to_eur_data.values()

        sol_to_eur = Crypto("SOL", "EUR")
        sol_to_eur_data = sol_to_eur.retrieve_data()
        sol_to_eur_data_value = sol_to_eur_data.values()

        return (btc_to_eur_data_value, eth_to_eur_data_value, sol_to_eur_data_value)

Crypto.get_Crypto_values()
