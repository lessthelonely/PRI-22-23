from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re #to work with regular expressions

#we got the url from the csv
url="https://www.goodreads.com/book/show/1001053.Between_Two_Fire"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html5lib')

#Number of pages
num_pages= soup.find_all('meta',{'property':'books:page_count'}) #We get <meta content="304" property="books:page_count"/>
num_pages=num_pages[0]["content"] if num_pages else None
print(num_pages)

#Reviews?
