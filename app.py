import requests
import time

api_address = "https://api.mixcloud.com/reynier-quintero/"
 
r = requests.get(api_address)

if r.status_code == 200:
    print(r.text)