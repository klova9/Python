<<<<<<<< HEAD:Python-main/Automation/Extraction/extract_notes.py
import auto_login
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
========
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# WIP
# This code uses the Selenium library to automate a web browser. It sets up a Firefox browser instance, navigates to a webpage, and waits for a specific element on the page to become clickable before clicking it. The element is located using a CSS selector.
>>>>>>>> 6681c519131bad23a5d0f316109aa26c0227b571:Python-main/src/package_klova9/Automation/Other/extract_notes.py

CSS_SELECTOR = "css selector"
path = "/Python/geckodriver"
Service = Service(executable_path=path)
driver = webdriver.Firefox()

<<<<<<<< HEAD:Python-main/Automation/Extraction/extract_notes.py
visits = driver.find_element(
    By.CSS_SELECTOR, "li.shortcut:nth-child(1) > a:nth-child(1) > span:nth-child(2)").click()
========
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "li.shortcut:nth-child(1) > a:nth-child(1)"))).click()
>>>>>>>> 6681c519131bad23a5d0f316109aa26c0227b571:Python-main/src/package_klova9/Automation/Other/extract_notes.py
