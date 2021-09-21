import requests
from bs4 import BeautifulSoup
import json

url = 'https://en.wikipedia.org/w/index.php' + \
      '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'
#url = 'https://www.kdnuggets.com/2017/03/structural-equation-modeling.html'      
r = requests.get(url)
html_contents = r.text
html_soup = BeautifulSoup(html_contents, 'html.parser')

def extract_tables(class_name):
    episodes = []
    ep_tables = html_soup.find_all('table',class_=class_name)

    for table in ep_tables:
        headers = []
        row = table.find_all('tr')
        #Start by fetching the header cells from the first row
        #to determine the field names
        for header in table.find('tr').find_all('th'):
            headers.append(header.text)
        #Then go through all the rows except the first one
        for row in table.find_all('tr')[1:]:
            values = []
            #And get the column cells, the first one big inside a th-tag
            for col in row.find_all(['th','td']):
                values.append(col.text)
            if values:
                episodes_dict = {headers[i]:values[i] for i in 
                                range(len(values))}
                episodes.append(episodes_dict)
    #show results
    for episode in  episodes:
        print(episode)
        
    with open('episodes.json','w') as f:
        f.write(json.dumps(episodes))
        
def extract_links():
    links = []
    ep_links = html_soup.find_all('a')
    for ep_link in ep_links:
        links.append(ep_link.get('href'))
    links_dict = {i:links[i] for i in range(len(links))}   
    print (links_dict)

#Main
if __name__ == '__main__':
    #extract_tables(class_name='wikiepisodetable')
    extract_links()
