import requests
from bs4 import BeautifulSoup

url = "https://www.algebra.hr"

# HTTP requests ( get, post, put, delete)
response = requests.get(url)

#print(response)
#print(type(response))
#print(response.status_code)



# web scraping
# BEAUTIFUL SOUP 4
# pip install beautiful


stranica = BeautifulSoup(response.content, "html.parser")
#print(type(stranica))
#print(stranica)

# iz objekta koji dobijemo sada tu hvatamo npr sve h3 tagove
h3_tags = stranica.find_all("h3")

print(type(h3_tags))
print(h3_tags[3].get_text()) 