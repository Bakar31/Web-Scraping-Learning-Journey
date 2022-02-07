import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

# check if the website is scrapable or not
print(requests.get(url))

# getting the page
page = requests.get(url)

# formatting the texts
soup = BeautifulSoup(page.text, 'lxml')
print(soup)