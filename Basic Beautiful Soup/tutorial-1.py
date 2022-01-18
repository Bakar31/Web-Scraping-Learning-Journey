import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

# check if the website is scrapable or not
print(requests.get(url))
