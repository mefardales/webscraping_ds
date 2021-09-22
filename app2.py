import requests
from bs4 import BeautifulSoup

url = 'http://www.webscrapingfordatascience.com/postform2/'
r = requests.get(url)

if r.status_code == 200:
      formdata = {
            'name': 'Pepe',
            'gender': 'M',
            'pizza': 'like',
            'haircolor': 'brown',
            'comment': ''
      }
      r = requests.post(url,data=formdata)
      print(r.text)