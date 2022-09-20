from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re #to work with regular expressions

#url formula: 
url = "https://www.bookdepository.com/Verity-Colleen-Hoover/9781408726600?ref=grid-view"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html5lib')
divs = soup.find_all('div')

ratings = soup.find_all('span',{'class':'list-price'})  
  
print(ratings[0].get_text())
'''page = urlopen(url) #opens the url
html = page.read().decode("utf-8") #reads html
soup = BeautifulSoup(html, "html.parser") #Creates a BeautifulSoup object and assigns it to the soup variable

print(page)'''

#print(html)
#print(soup.get_text())
#print(soup.title.string) #.string cleans up the tags

'''
url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

print(html)

title_index = html.find("<title>") #index of the <title> tag
start_index = title_index + len("<title>") #index of the first letter in the title
end_index = html.find("</title>") #index of the closing </title> tag
title = html[start_index:end_index]
'''


'''
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

pattern = "<title.*?>.*?</title.*?>"
match_results = re.search(pattern, html, re.IGNORECASE)
title = match_results.group()
title = re.sub("<.*?>", "", title) # Remove HTML tags

print(title)'''


