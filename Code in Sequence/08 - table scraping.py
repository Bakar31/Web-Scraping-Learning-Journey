import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.worldometers.info/world-population/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table', class_ = 'table table-striped table-bordered table-hover table-condensed table-list')
#print(table)

headers = table.find_all('th')
headers = [th.text for th in headers]
#print(headers)

df = pd.DataFrame(columns = headers)

rows = table.find_all('tr')[1:]
for row in rows:
    single_row = row.find_all('td')
    single_row = [td.text for td in single_row]
    length = len(df)
    df.loc[length] = single_row
    
print(df.head())