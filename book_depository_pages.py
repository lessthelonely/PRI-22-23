from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re #to work with regular expressions
import pandas

'''
So the url formula only works if we know the exact way the title and the author's name is written in the website url
For example Verity has a way longer title than just Verity, the actual title in the book depository page is "Verity : The thriller that will capture your heart and blow your mind"
I think the actual book title is just Verity but who knows what the title of this book would be in the dataset
When we use the search bar, there's an intermediate link...We can search only using the ISBN so perhaps there's an url with only the ISBN which we have and it's unique'''

database = pandas.read_csv('data/goodreads_with_pages.csv').dropna()
books_zero_pages = database.loc[database['pages'] == 0] #get the books with zero pages

def getPages(isbn):
    try:
        #intermediate url formula (searchTerm= to the ISBN13):
        url ="https://www.bookdepository.com/search?searchTerm=" + isbn +"&search=Find+book"

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html5lib')
        num_pages=soup.find('span', itemprop='numberOfPages')
        num_pages=re.findall("\d+",num_pages.text)[0]
        if num_pages != 0:
            database.loc[database.isbn == isbn,'pages']=num_pages
        print(num_pages)    
    except:
        return False
    return True 


books_zero_pages[books_zero_pages['isbn'].apply(getPages)]
database.to_csv('data/book_depository_pages.csv',encoding='utf-8')        