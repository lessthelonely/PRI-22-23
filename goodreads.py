from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re #to work with regular expressions
import pandas

database = pandas.read_csv('data/GoodReads_100k_books.csv').dropna()
books_zero_pages = database.loc[database['pages'] == 0] #get the books with zero pages
books_zero_pages = books_zero_pages[['link']]
print(len(books_zero_pages))

def getPages(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')

        #Number of pages
        num_pages= soup.find_all('meta',{'property':'books:page_count'}) #We get <meta content="304" property="books:page_count"/>
        num_pages=num_pages[0]["content"] if num_pages else 0
        if num_pages !=0:
            database.loc[database.link == url, 'pages'] = num_pages
        print(num_pages)
    except:
        return False
    return True        

books_zero_pages[books_zero_pages['link'].apply(getPages)]
database = database.loc[:, ~database.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
database.to_csv('dataset/goodreads_with_pages.csv')




