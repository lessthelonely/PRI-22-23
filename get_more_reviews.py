from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re #to work with regular expressions
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

reviews=pd.read_csv('data/cleaned_reviews_translated.csv')
clean_book = pd.read_csv('data/current_data.csv')

r_list=list(reviews['url'].unique())

links=[]
for i in clean_book.index:
    if (clean_book.loc[i,'link'] not in r_list):
        links.append(i)
        
        
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
    with ThreadPoolExecutor(max_workers=65) as p:
        p.map(getReviews,links)

main()
if(False in data):
    data.remove(False)

df=pd.DataFrame(data,columns=['url','review'])
df.to_csv('data/more_reviews.csv')
