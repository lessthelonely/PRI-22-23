from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re #to work with regular expressions
import pandas
from concurrent.futures import ThreadPoolExecutor

database = pandas.read_csv('data/goodreads_with_prices.csv').dropna()
database = database.iloc[: , 1:]
links=database['link'].to_list()

def getLanguage(url):
    try:
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        language=soup.find_all('div',{'itemprop':'inLanguage'})
        database.loc[database.link==url,'language']=language[0].text
        print(language[0].text)
    except:
        return False
    return True        

def main():
    with ThreadPoolExecutor(max_workers=100) as p:
        p.map(getLanguage,links)

main()

database.to_csv('data/goodreads_with_language.csv',encoding='utf-8')


