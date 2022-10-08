from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re #to work with regular expressions
import pandas
from concurrent.futures import ThreadPoolExecutor

database = pandas.read_csv('dataset/goodreads_with_prices.csv').dropna()
database = database.iloc[: , 1:]
links=database['link'].to_list()
data=[]

def getReviews(url):
    reviews=[]
    try:
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        for i in soup.find_all('span',{'class':'readable'}):
            spans=i.find_all('span')
            r=[]
            review=spans[-1].get_text(separator="\n")
            r+=[url]
            r+=[review]
            print(review)
            data.append(r)    
    except:
        return False
    return reviews      

def main():
    with ThreadPoolExecutor(max_workers=100) as p:
        p.map(getReviews,links)

main()
if(False in data):
    data.remove(False)

df=pandas.DataFrame(data,columns=['url','review'])
df = df.loc[:, ~df.columns.str.contains('^Unnamed')] #delete Unnamed columns pandas
df.to_csv('dataset/goodreads_with_review.csv')


