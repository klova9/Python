from selenium import webdriver
<<<<<<<< HEAD:Python-main/Automation/Extraction/news_headlines.py
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
========
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
website = "https://www.thesun.co.uk/sport/football/"
path = "/Python/geckodriver"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
>>>>>>>> 6681c519131bad23a5d0f316109aa26c0227b571:Python-main/src/package_klova9/Automation/Headlines/news_headlines.py
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
<<<<<<<< HEAD:Python-main/Automation/Extraction/news_headlines.py

file_name = f'{application_path}headings_{month_day_year}.csv'
final_path = os.path.join(application_path, file_name)
df_tagline.to_csv(final_path)
========
df_tagline.to_csv('headings_headless.csv')
>>>>>>>> 6681c519131bad23a5d0f316109aa26c0227b571:Python-main/src/package_klova9/Automation/Headlines/news_headlines.py
driver.quit()
