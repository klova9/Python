import auto_login
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
CSS_SELECTOR = "css selector"
path = "/Python/geckodriver"
Service = Service(executable_path=path)
driver = webdriver.Firefox()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "li.shortcut:nth-child(1) > a:nth-child(1)"))).click()
