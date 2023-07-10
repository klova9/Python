from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# WIP
# This code uses the Selenium library to automate a web browser. It sets up a Firefox browser instance, navigates to a webpage, and waits for a specific element on the page to become clickable before clicking it. The element is located using a CSS selector.

CSS_SELECTOR = "css selector"
path = "/Python/geckodriver"
Service = Service(executable_path=path)
driver = webdriver.Firefox()

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "li.shortcut:nth-child(1) > a:nth-child(1)"))).click()
