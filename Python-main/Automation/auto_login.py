from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

user_name = username
pass_word = password
path = "/Python/geckodriver"
website = website

Service = Service(executable_path=path)
driver = webdriver.Firefox()
driver.get(website)

CSS_SELECTOR = "css selector"
NAME = "name"

# Input Username
elements = driver.find_elements(By.CSS_SELECTOR, "#Login")
username = elements[0]
username.clear
username.send_keys(user_name)

# Input Password
elements = driver.find_elements(By.CSS_SELECTOR, "#Password")
password = elements[0]
password.clear
password.send_keys(pass_word)

# Click Sumbit
elements = driver.find_elements(By.NAME, "submit")
submit = elements[0]
submit.click()
