from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pandas as pd

firefox_binary = FirefoxBinary()

options = Options()
options.headless = True
username = "username"
password = "password"

website = "https://www.thesun.co.uk/sport/football/"
path = "/Python/geckodriver"

Service = Service(executable_path=path)
driver = webdriver.Firefox(firefox_binary=firefox_binary, options=options)
driver.get(website)

ontainers = driver.find_elements(by="xpath", value='//div[@class="teaser__copy-container"]')

titles = []
subtitles = []
links = []

for container in containers:
    title = container.find_element(
        by="xpath", value='./a/h3').text
    subtitle = container.find_element(
        by="xpath", value='./a/p').text
    link = container.find_element(
        by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)
    
element_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_tagline = pd.DataFrame(element_dict)
df_tagline.to_csv('headings_headless.csv')
driver.quit()