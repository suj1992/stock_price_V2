from selenium import webdriver
import warnings
warnings.filterwarnings("ignore")
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup
import pandas as pd
from flask import request
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import time

# Initialize the WebDriver outside the function


def screen_shot(name_company):
    firefox_options = Options()
    driver = webdriver.Firefox(options=firefox_options)

    driver.get("https://groww.in/")
    driver.implicitly_wait(5)
    
    #Stock name in the Search box
    search_box = driver.find_element(By.XPATH, '//*[@class="c-kHzvll inputTextColor bodyBase"]')
    search_box.send_keys(name_company)
    driver.implicitly_wait(2)
    
    #Hit the search box
    div_element = driver.find_element(By.XPATH, '//*[@class="valign-wrapper vspace-between width100 gsc23SuggestionContent"]')
    div_element.click()
    driver.implicitly_wait(2)
    print("ENETR IS HITTING")

    #Click the terminal button
    anchor_element = driver.find_element(By.XPATH, '//*[@class="valign-wrapper gr1TPAdvanceLink borderPrimary bodySmallHeavy contentPrimary cur-po"]')
    anchor_element.click()
    driver.implicitly_wait(15)
    print("Terminal is oppening")
    indicator_element = driver.find_element(By.XPATH, '//*[@class="group-HlcUjC8J"]')
    indicator_element.click()
    print("Indicator is oppening")
# class="button-TPBYkbxL button-gbkEfGm4 withText-gbkEfGm4 button-uO7HM85b apply-common-tooltip isInteractive-uO7HM85b"
# class="button-TPBYkbxL button-gbkEfGm4 withText-gbkEfGm4 button-uO7HM85b apply-common-tooltip isInteractive-uO7HM85b"
# class="button-TPBYkbxL button-gbkEfGm4 withText-gbkEfGm4 button-uO7HM85b apply-common-tooltip isInteractive-uO7HM85b"
# class="group-HlcUjC8J"
# group-HlcUjC8J