from markupsafe import string
import requests
from bs4 import BeautifulSoup
import re

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

#find by sring
strsearch_1 = soup.find_all(string = 'Iphone')
print(strsearch_1)

strsearch_2 = soup.find_all(string = re.compile('Ip'))
print(strsearch_2)

strsearch_3 = soup.find_all(string = re.compile('Nokia'))
print(strsearch_3)

# find class name
classes_1 = soup.find_all(class_ = re.compile('pull'))
#print(classes_1)

classes_2 = soup.find_all('p', class_ = re.compile('pull'))
print(classes_2)

# find_all limit
classes_2 = soup.find_all('p', class_ = re.compile('pull'), limit=2)
print(classes_2)
