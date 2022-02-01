from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:/Programming/Scraping/Udemy Course-1/Driver/chromedriver.exe')
driver.get('https://www.google.com/')

input_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_box.send_keys('web scraping')
input_box.send_keys(Keys.ENTER)