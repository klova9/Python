<<<<<<< HEAD:Python-main/Automation/auto_login.py
from selenium import webdriver
import auto_login_credentials
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
# This code uses the Selenium library to automate logging in to a website. It retrieves login credentials from a separate file, navigates to the website, inputs the username and password, and clicks the submit button.

firefox_binary = FirefoxBinary()
options = Options()
user_name = ""
pass_word = ""
path = "/Python/geckodriver"
website = ""

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
=======
from selenium import webdriver
import auto_login_credentials
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
# This code uses the Selenium library to automate logging in to a website. It retrieves login credentials from a separate file, navigates to the website, inputs the username and password, and clicks the submit button.

user_name = auto_login_credentials.username
pass_word = auto_login_credentials.password
path = "/Python/geckodriver"
website = auto_login_credentials.website

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
>>>>>>> 6681c519131bad23a5d0f316109aa26c0227b571:Python-main/src/package_klova9/Automation/AutoLogin/auto_login.py
