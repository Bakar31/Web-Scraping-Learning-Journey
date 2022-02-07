import requests
from bs4 import BeautifulSoup

url = 'https://www.marketwatch.com/investing/stock/aapl'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

stock_price = soup.find('bg-quote', class_ = 'value').text
print(stock_price)

closing_price = soup.find('td', class_ = 'table__cell u-semi').text
print(closing_price)

range_data = soup.find_all('div', class_ = 'range__header')[2]
range_data = [data.text for data in range_data ]
lower_range = range_data[1]
higher_range = range_data[5]
print(lower_range)
print(higher_range)

# Rating
rating = soup.find('li', class_ = 'analyst__option active').text
print(rating)