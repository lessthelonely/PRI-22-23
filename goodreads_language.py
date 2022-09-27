from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import re #to work with regular expressions
import pandas

database = pandas.read_csv('data/goodreads_with_prices.csv').dropna()

def getPages(url):
    try:
        response = urllib.request.urlopen(url)
        soup = BeautifulSoup(response, 'html.parser')
        language=soup.find_all('div',{'itemprop':'inLanguage'})
        database.loc[database.link==url,'language']=language[0].text
        print(language)
    except:
        return False
    return True        

database.to_csv('data/goodreads_with_language.csv',encoding='iso 8859-8')


