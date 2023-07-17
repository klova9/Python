from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import booking_constants
import os
# WIP
class Booking(webdriver.Chrome):
   
    def __init__(self, driver_path = r"c:\Users\USER\Documents\Drivers\chromedriver.exe"):
        self.driver_path = driver_path
        os.environ["PATH"] += self.driver_path
        super(Booking, self,).__init__()
   
    def land_first_page(self):
       self.get(booking_constants.website + f'/searchresults.html?ss={booking_constants.place}/&ssne={booking_constants.place}')
   
    def select_dates(self, check_in, check_out):
       check_in_element = self.find_element(By.XPATH,f'//*[@id="calendar-searchboxdatepicker"]/div/div[1]/div/div[1]/table/tbody/tr[5]/td[6]/span').click()
