from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('D:/Programming/Scraping/Udemy Course-1/Driver/chromedriver.exe')
driver.get('https://www.indeed.com/')
time.sleep(5)

job_search = driver.find_element_by_xpath('//*[@id="text-input-what"]')
job_search.send_keys('Machine Learning Engineer')

location = driver.find_element_by_xpath('//*[@id="text-input-where"]')
location.send_keys('United States')
location.send_keys(Keys.ENTER)
time.sleep(5)

#Creates a dataframe
df = pd.DataFrame({'Job Title':[''], 'Company':[''], 'Company Rating':[''], 'Job Snippet':[''], 'Location':[''],'Salary':['']})

while True:
    time.sleep(5)
    try:
        driver.find_element_by_xpath('//*[@id="popover-x"]/button').click()
    except:
        pass

    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', class_ = 'job_seen_beacon')

    for posting in postings:
        title = posting.find('h2', class_ = 'jobTitle').text

        try:
            company_name = posting.find('span', class_ = 'companyName').text       
        except:
            company_name = 'N/A'

        try:
            company_rating = posting.find('span', class_ = 'ratingNumber').text           
        except:
            company_rating = 'N/A'

        try:
            company_location = posting.find('div', class_ = 'companyLocation').text        
        except:
            company_location = 'N/A'

        try:
            job_snippet = posting.find('div', class_ = 'job-snippet').text      
        except:
            job_snippet = 'N/A'

        try:
            salary = posting.find('div', class_ = 'attribute_snippet').text     
        except:
            salary = 'N/A'

        df = df.append({'Job Title':title, 'Company':company_name, 'Company Rating': company_rating,  'Job Snippet': job_snippet, 'Location':company_location,'Salary':salary},
                       ignore_index = True)

    try:
        next_page = soup.find('a', attrs = {'aria-label': 'Next'}).get('href')
        driver.get('https://indeed.com'+next_page)
    except:
        break

df.to_csv('Indeed Machine Learing Jobs.csv', index=False)