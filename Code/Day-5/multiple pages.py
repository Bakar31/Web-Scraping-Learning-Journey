import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.carpages.ca/used-cars/search/?category_id=1'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

# Dataframe
df = pd.DataFrame({'Name':[''], 'Description':[''], 'Price':[''], 'Color':[''], 'Link':['']})

counter = 0
#This loop goes through all pages and grabs all the details of each car
while counter < 51:
    
    cars = soup.find_all('div', class_ = 'media soft push-none rule')
    for car in cars:
        link = car.find('a', class_ = 'media__img media__img--thumb').get('href')
        link = 'https://www.carpages.ca' + link
        name = car.find('h4', class_ = 'hN').text.strip() # to remove the whitespace
        try:
            description = car.find('h5', class_ = 'hN grey').text
        except:
            description = ''
        price = car.find('strong', class_ = 'delta').text.strip()
        color = car.find_all('div', class_ = 'grey l-column l-column--small-6 l-column--medium-4')[1].text.strip()
        df = df.append({'Name':name, 'Description': description, 'Price':price, 'Color':color, 'Link':link, }, ignore_index = True)


    next_page = soup.find('a', class_ = 'nextprev').get('href')
    page = requests.get(next_page)
    soup = BeautifulSoup(page.text, 'lxml')
    counter += 1
    print('Page No. {} done.'.format(counter))

df.to_csv('car details.csv', index = False)
print(df.head())