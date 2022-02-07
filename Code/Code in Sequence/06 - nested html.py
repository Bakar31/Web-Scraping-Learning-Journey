import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

#extracted data from nested HTML tags
boxes = soup.find_all('div', class_ = 'col-sm-4 col-lg-4 col-md-4')
box_1 = boxes[0]
#print(box_1)

name = box_1.find('a', class_ = 'title').text  
print(name)

# Navigation menu
box2 = soup.find_all('ul', class_ = 'nav', id = 'side-menu')[0]    
print(box2.find_all('li')[1].text)