import requests
from urllib.parse import quote_plus 

url = 'http://www.webscrapingfordatascience.com/paramhttp/' 
raw_string = "File System"
parameter = {
    'query' : 'esto es una prueba'
}
r = requests.get(url, params=parameter)
print(r.text)
