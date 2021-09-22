import requests
from bs4 import BeautifulSoup


url = 'https://www.expedia.mx/Hotel-Search?SEMDTL=a112476355771.b1119036740775.g1kwd-63345650.l1.e1c.m1Cj0KCQjwqKuKBhCxARIsACf4XuGd_D6skiKB1K69LKWfbtaMPqreZMZRgnXqA0RlWzbk52fed-QcWaIaAn2HEALw_wcB.r13de053073ce1be06c242b94f6a368fd5cad9e1c6619f8e24ec5f6e53fe78386b.c1fobt311GDgJok3O3AxaHbw.j11010116.k1.d1502801818899.h1e.i1.n1.o1.p1.q1.s1.t1.x1.f1.u1.v1.w1&destination=M%C3%A9xico&endDate=2021-10-07&gclid=Cj0KCQjwqKuKBhCxARIsACf4XuGd_D6skiKB1K69LKWfbtaMPqreZMZRgnXqA0RlWzbk52fed-QcWaIaAn2HEALw_wcB&locale=es_MX&regionId=117&semcid=MX.UB.GOOGLE.DT-c-ES.HOTEL&semdtl=&siteid=12&sort=RECOMMENDED&startDate=2021-10-06&theme=&useRewards=false&userIntent='

r = requests.get(url)
content = r.text

try:
    html_soup = BeautifulSoup(content,'html.parser')

    class_li ='uitk-spacing listing uitk-spacing-margin-blockstart-three horizontal'
    hotel_items = html_soup.find('ol', class_='results-list no-bullet')
    
    #Scraping hotels names from expedia.mx
    li_hotels = [li_hotel for li_hotel in hotel_items.find_all('li', class_=class_li)]
    h_items =  [h_items.find_all('h3', class_='uitk-heading-5 is-visually-hidden') for h_items in li_hotels]
    h_item_name = [h_item[0].get_text() for h_item in h_items]
    print (h_item_name)
    
except TimeoutError as e:
    print(f'Error con la conexion !!!{e}')
