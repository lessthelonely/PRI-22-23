from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re #to work with regular expressions
import pandas

#database = pandas.read_csv('data/goodreads_with_prices.csv').dropna()
url="https://www.goodreads.com/book/show/1001053.Between_Two_Fire"

def getReviews(url):
    try:
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        review = []
        for i in soup.find_all('span',{'class':'readable'}):
            spans=i.find_all('span')
            print(spans[-1].get_text(separator="\n"))
            review.append(spans[-1].text)
    except:
        return False
    return True      

getReviews(url)  

#database[database['link'].apply(getLanguage)]
#database.to_csv('data/goodreads_with_language.csv',encoding='utf-8')


