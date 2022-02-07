import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers'

# getting the page
page = requests.get(url)

# formatting the texts
soup = BeautifulSoup(page.text, 'lxml')

#Tags
header_section = soup.header
#print(header_section)

# Navigable String(String within a tag)
p_tag_string = soup.header.p
print(p_tag_string.text)

#Attributes
attributes = header_section.a.attrs
print(attributes)