from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re #to work with regular expressions

#headers = {
 #   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
#}

#page = requests.get("https://www.amazon.com/dp/B000F83SZQ", headers = headers)

#soup = BeautifulSoup(page.content, 'html.parser')
#print(page.text)

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})

URL = "https://www.amazon.com/dp/B000F83SZQ"
webpage = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(webpage.content, "lxml")

# Outer Tag Object
title = soup.find("span", attrs={"id":'productTitle'})
print(title.string)

