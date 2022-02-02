#Let's starts up our Driver and loads up our starting webpage
from selenium import webdriver

#driver
driver = webdriver.Chrome('D:/Programming/Scraping/Udemy Course-1/Driver/chromedriver.exe')
driver.get('https://www.batabd.com/collections/b-sneakers')
# price = driver.find_element_by_xpath('//*[@id="shopify-section-collection-template-default"]/div/div[2]/div[2]/div/div/div[2]/div[2]/div/span[2]').text
# print(price)

#multiple shoe prices
for i in range(1, 10):
    price = driver.find_element_by_xpath('//*[@id="shopify-section-collection-template-default"]/div/div[2]/div['+ str(i) +']/div/div/div[2]/div[2]/div/span[2]').text
    print(price)