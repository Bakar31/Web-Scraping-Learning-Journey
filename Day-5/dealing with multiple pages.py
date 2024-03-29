import requests
from bs4 import BeautifulSoup

url = "https://www.airbnb.com/s/Honolulu--HI--United-States/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=february&flexible_trip_dates%5B%5D=march&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Honolulu%2C%20HI%2C%20United%20States&place_id=ChIJTUbDjDsYAHwRbJen81_1KEs&checkin=2022-01-27&checkout=2022-01-31&source=structured_search_input_header&search_type=autocomplete_click"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

next_page = soup.find_all('a', {'aria-label':'Next'})
print(next_page)