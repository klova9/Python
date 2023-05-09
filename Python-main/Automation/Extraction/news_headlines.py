from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import pandas as pd
import os
import sys
from datetime import datetime

application_path = os.path.dirname(sys.executable)
now = datetime.now()
month_day_year = now.strftime('%m%d%y')

options = Options()
options.headless = True


website = "https://www.thesun.co.uk/sport/football/"
path = "/Python/geckodriver"

Service = Service(executable_path=path)
driver = webdriver.Firefox(options=options)
driver.get(website)

containers = driver.find_elements(
    by="xpath", value='//div[@class="teaser__copy-container"]')

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

file_name = f'{application_path}headings_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_tagline.to_csv(final_path)
driver.quit()
