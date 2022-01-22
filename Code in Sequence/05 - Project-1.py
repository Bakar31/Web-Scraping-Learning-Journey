# Scrape all product detail and store in a pandas dataframe

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

#extracting useful informations
names = soup.find_all('a', {'class': 'title'})
prices = soup.find_all('h4', {'class':'pull-right price'})
reviews = soup.find_all('p', {'class':'pull-right'})
descriptions = soup.find_all('p', {'class':'description'})

names = [name.text for name in names]
prices = [price.text for price in prices]
reviews = [review.text for review in reviews]
descriptions = [description.text for description in descriptions]

table = pd.DataFrame({'Product Name': names, 'Description':descriptions, 'Reviews':reviews, 'Price':prices})
print(table.head())