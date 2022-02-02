from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from transformers import DeiTConfig

driver = webdriver.Chrome('D:/Programming/Scraping/Udemy Course-1/Driver/chromedriver.exe')
driver.get('https://www.google.com/')

# text in search bar
input_box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
input_box.send_keys('football')
input_box.send_keys(Keys.ENTER)

images_tab = driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
images_tab.click()

#find_pic
pic = driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[3]/a[1]/div[1]/img')
pic.screenshot('D:/Programming/Scraping/Udemy Course-1/Day-6/football_1.png')