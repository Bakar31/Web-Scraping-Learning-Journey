import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('D:/Programming/Scraping/Udemy Course-1/Driver/chromedriver.exe')
driver.get('https://www.google.com/')

input_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_box.send_keys('top 100 movies of all times')
input_box.send_keys(Keys.ENTER)

imdb_link = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a/h3').click()
time.sleep(5)

#Scrolls until Jaws the movie is on the screen
driver.execute_script('window.scrollTo(0,15000)')

poster = driver.find_element_by_xpath('//*[@id="main"]/div/div[3]/div/div[50]/div[2]/a/img').screenshot('D:/Programming/Scraping/Udemy Course-1/Day-7/casablanca.png')