from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re

word='absorbing'
syns=[]

url = 'https://www.thesaurus.com/browse/' + word
response = requests.get(url)
soup=BeautifulSoup(response.content, 'html.parser')
language= soup.find_all('a', {'class': 'css-1kg1yv8 eh475bn0'})
#l1=language.find('a', {'class': 'css-1kg1yv8 eh475bn0'})
for tag in language:
    syns.append(tag.text.strip())

file_word = word + ', '
for s in syns:
    file_word += s + ', '

print(file_word)
