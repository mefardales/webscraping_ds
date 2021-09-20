import requests


address = {    
    1: 'https://notiremedios.com/QXpa',
    2: 'https://notiremedios.com/Jk8UGgCK',
    3: 'https://notiremedios.com/Ammeg',
    4: 'https://notiremedios.com/uCqm',
    5:'https://notiremedios.com/5XLWiA'
}
i = 0
for v in address.values():
    try:
        r = requests.get(v)
        print (f'--> {v}')
        print(f'Accedio {i} veces')
        print("Ok !!!")
        i += 1
    except:
        print("Error :( ")
