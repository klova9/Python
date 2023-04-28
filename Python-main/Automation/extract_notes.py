import auto_login
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By

CSS_SELECTOR = "css selector"
path = "/Python/geckodriver"
Service = Service(executable_path=path)
driver = webdriver.Firefox()

visits = driver.find_element(
    By.CSS_SELECTOR, "li.shortcut:nth-child(1) > a:nth-child(1) > span:nth-child(2)").click()
