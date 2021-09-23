import requests
from bs4 import BeautifulSoup

url = 'http://www.webscrapingfordatascience.com/postform2/'
r = requests.get(url)

#scraping with post request 
def send_data_post():
      paramdata = {'name':'Totally Not Seppe'}
      formdata = {'name':'Seppe'}
      r = requests.post(url,params=paramdata, data=formdata)
      return r.text
#example send picture profile to server
def set_profile_picture():
      formdata = {'name': 'Seppe'}
      filedata = {'profile_picture': open('me.jpg','rb')}
      r = requests.post(url, data=formdata, file=filedata)
      return r.text

#modifing http headers to prevent 
#website block by header check
def header_new():
      my_header ={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64;64) AppleWebKit/537.36'+
            '(KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
      }
      r = requests.get(url, headers=my_header)
      #print(r.text)
      print(r.request.headers)
#authentication 
def auth():
      url = 'http://www.webscrapingfordatascience.com/authentication/'
      r = requests.get(url,auth=('myusername','mypassword'))
      print(r.text)
      print(r.request.headers)
      
if __name__ == '__main__':
      #print(send_data_post())
      #print(set_profile_picture())
      #header_new()
      auth()

