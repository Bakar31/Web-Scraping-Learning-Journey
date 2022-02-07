from operator import index
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('D:/Programming/Scraping/Udemy Course-1/Driver/chromedriver.exe')
driver.get('https://www.nike.com/w/mens-clothing-6ymx6znik1')

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'lxml')
product_card = soup.find_all('div', class_ = 'product-card__body')
print(len(product_card))

df = pd.DataFrame({'Name':[''], 'Subtitle':[''], 'Color':[''], 'Price':[''], 'Link':['']})
df.head()

for product in product_card:
    try:
        link = product.find('a', class_ = 'product-card__link-overlay').get('href')
        name = product.find('div', class_ = 'product-card__title').text
        subtitle = product.find('div', class_ = 'product-card__subtitle').text
        color = product.find('div', class_ = 'product-card__product-count').text 
        price = product.find('div', class_ = 'product-card__price-wrapper').text
        pos = [pos for pos, char in enumerate(price) if char == '$']
        if len(pos) == 1:
            price = price
        else:
            price = price[: pos[1]] 

        df = df.append({'Name':name, 'Subtitle':subtitle, 'Color': color, 'Price':price, 'Link':link},ignore_index = True)
    except:
        pass

df.head()
#exports the dataframe as a csv
df.to_csv('NIKE men products detail.csv', index = False)