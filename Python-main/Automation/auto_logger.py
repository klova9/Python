from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import pandas as pd

firefox_binary = FirefoxBinary()

options = Options()
username = "username"
password = "password"
