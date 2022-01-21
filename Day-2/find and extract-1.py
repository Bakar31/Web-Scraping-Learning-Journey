import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

header = soup.find('header')
#print(header)

#find tag specifically
find_1 = soup.find('div', {'class': 'container test-site'})
#print(find_1)

find_2 = soup.find('div', {'class': 'container test-site', 'class': 'col-md-9'})
#print(find_2)

#find price
price = soup.find('h4', {'class':'pull-right price'})
print(price.text)

# all prices
prices = soup.find_all('h4', {'class':'pull-right price'})
prices = [price.text for price in prices ]
print(prices)

# all names
names = soup.find_all('a', {'class':'title'})
names = [name.text for name in names ]
print(names)

# all descriptions
descriptions = soup.find_all('p', {'class':'description'})
descriptions = [description.text for description in descriptions ]
print(descriptions)

#Multiple tags
multi_tag = soup.find_all(['h4', 'p'])
#print(multi_tag)