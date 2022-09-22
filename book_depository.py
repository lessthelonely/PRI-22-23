from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import re #to work with regular expressions

'''
So the url formula only works if we know the exact way the title and the author's name is written in the website url
For example Verity has a way longer title than just Verity, the actual title in the book depository page is "Verity : The thriller that will capture your heart and blow your mind"
I think the actual book title is just Verity but who knows what the title of this book would be in the dataset
When we use the search bar, there's an intermediate link...We can search only using the ISBN so perhaps there's an url with only the ISBN which we have and it's unique'''

ibsn="9780593358573"
#intermediate url formula (searchTerm= to the ISBN13):
url ="https://www.bookdepository.com/search?searchTerm=" + ibsn +"&search=Find+book"

#url formula: 
#url = "https://www.bookdepository.com/Verity-Colleen-Hoover/9781408726600?ref=grid-view"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html5lib')
divs = soup.find_all('div')

#Using sale-price we will get the normal price if the book isn't on sale and the sale price if the book is on sale
ratings = soup.find_all('span',{'class':'sale-price'})  
if(len(ratings)):
    print(ratings[0].get_text())
else:
    ratings = soup.find_all('p',{'class':'list-price'})  
    if(len(ratings)):
        list_price=ratings[0].get_text()
        price=list_price[65]+list_price[66]+list_price[67]+list_price[68]+list_price[69]+' '+list_price[71]
        print(price)
    else:
        print("NA")    
    
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


