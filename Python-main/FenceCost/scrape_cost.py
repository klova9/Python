from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import pandas as pd
website = "https://www.menards.com/main/building-materials/fencing/vinyl-fencing/c-5772.htm?Spec_ProductType_facet=Vinyl+Privacy+Fence+Panel"
path = "/Python/geckodriver"

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get(website)
containers = driver.find_elements(
    by="xpath", value='//*[@id="searchItems"]')

prices = []
names = []
sizes = []
for container in containers:
    price = container.find_element(
        by="xpath", value='/html/body/main/div/section/div/div/div[4]/div/div[2]/div/div[3]/div[1]/div/div/div[4]/span/span/span').text
    name = container.find_element(by='css path', value = 'html body main div#content.container section div#search div div.sticky div.d-md-flex div.col div div#searchItems.result-grid.row.w-100 div#1480663227589.search-item div.border-bottom.border-bottom-4.d-flex.h-100.mb-3.mx-3.search-item-container div.details a div.row.pb-variations div.col-12.multilines-3.text-truncate-multilines.xs-single-col-8 strong.text-dark')
   # size = container.find_element(
   #     by="xpath", value='./a').get_attribute("href")
    prices.append(price)
    names.append(name)
    #sizes.append(size)

element_dict = {'price': prices, 'name': names }
df_tagline = pd.DataFrame(element_dict)
print(df_tagline)
