import requests
import time

address = {    
    1: 'https://notiremedios.com/QXpa',
    2: 'https://notiremedios.com/Jk8UGgCK',
    3: 'https://notiremedios.com/Ammeg',
    4: 'https://notiremedios.com/uCqm',
    5:'https://notiremedios.com/5XLWiA'
}
i = 0
while True:
    for v in address.values():
        time.sleep(5)
        try:
            print("Accediendo ...")
            r = requests.get(v)
            print (f'--> {v}')
            print(f'Accedio {i} veces')
            i += 1
        except:
            print("Error :( ")
