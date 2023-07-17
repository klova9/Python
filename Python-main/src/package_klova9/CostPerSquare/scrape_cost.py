from selenium import webdriver
from selenium.webdriver.common.by import By
import os
# WIP
website = f'https://www.costco.com/CatalogSearch?dept=All&keyword=vinyl+plank+flooring"'
path = r"c:\Users\USER\Documents\Drivers\chromedriver.exe"
driver = webdriver.Chrome()
items = driver.find_elements(By.CLASS_NAME, value='product-tile-set')
descriptions = []
for item in items:
    print(item.find_element(By.XPATH, value='//*[@class=description]/a') .text)   

