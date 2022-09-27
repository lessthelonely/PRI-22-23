# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:06:28 2022

@author: Utilizador
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

browser = webdriver.Chrome("C:\\Users\\Utilizador\\Downloads\\chromedriver.exe") # path to chromedriver.exe (https://chromedriver.chromium.org/)

browser.get('https://www.goodreads.com/') # website

search_field = browser.find_element_by_id("sitesearch_field")

search_field.send_keys("9780545251327") # book we're looking for
search_field.send_keys(Keys.RETURN)
time.sleep(2)

try:
    close_popup_button = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div/div/button")
    close_popup_button.click()
except:
    close_popup_button2 = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/button")
    close_popup_button2.click()

more_details_button = browser.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div[2]/div[2]/div[2]/div[6]/div/div/button")
more_details_button.click()

language = browser.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div[2]/div[2]/div[2]/div[6]/div/span[2]/div[1]/span/div/dl/div[4]/dd/ul/span[1]").text

print(language)

"""
df = pd.read_csv('test/goodreads_with_prices.csv')
languages = []

for index in df.index:
    search_field2 = browser.find_element_by_xpath("/html/body/div[1]/header/div[2]/div[2]/section/form/input[1]")
    isbn = df.loc[index, 'isbn']
    while (len(isbn) != 10):
        isbn = "0" + isbn
    search_field2.send_keys(isbn)
    search_field2.send_keys(Keys.RETURN)
    time.sleep(1)
    more_details_button = browser.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div[2]/div[2]/div[2]/div[6]/div/div/button")
    more_details_button.click()
    language = browser.find_element_by_xpath("/html/body/div[1]/div/main/div[1]/div[2]/div[2]/div[2]/div[6]/div/span[2]/div[1]/span/div/dl/div[4]/dd/ul/span[1]").text
    languages.append(language)
    time.sleep(1)
    print("isbn: " + df.loc[index, 'isbn'] + " language: " + language)
    
df['Language'] = languages
"""