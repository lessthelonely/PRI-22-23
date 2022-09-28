from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re #to work with regular expressions
import pandas

database = pandas.read_csv('data/goodreads_with_prices.csv').dropna()
data=[]

def getReviews(url):
    try:
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        for i in soup.find_all('span',{'class':'readable'}):
            spans=i.find_all('span')
            review=spans[-1].get_text(separator="\n")
            reviews=[]
            reviews+=[url]
            reviews+=[review]
            print(reviews)
            data.append(reviews)    
    except:
        return False
    return True      


database[database['link'].apply(getReviews)]
df=pandas.DataFrame(data,columns=['url','review'])
df.to_csv('data/goodreads_with_review.csv',encoding='utf-8')


