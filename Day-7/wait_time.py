import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('D:/Programming/Scraping/Udemy Course-1/Driver/chromedriver.exe')
driver.get('https://www.google.com/')

# text in search bar
input_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_box.send_keys('football')
input_box.send_keys(Keys.ENTER)

# wait 5 seconds
time.sleep(5)

#wait until finding id 'cnt'
# element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'cnt')))

images_tab = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
images_tab.click()