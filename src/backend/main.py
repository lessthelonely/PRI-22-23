from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import Book, Suggestions, Filter, Author
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get all the books (maybe do top 10 or something)
@app.get("/books", response_model = List[Book], status_code=status.HTTP_200_OK)
async def get_books():
    query = 'http://localhost:8983/solr/books_schema/query?q=*:*&q.op=OR&indent=true&rows=100&start=0'
    list_books= requests.get(query).json()['response']['docs']
    books=[]
    for book in list_books:
        books.append(Book(**book))
    return books

# Get a book by id
@app.get("/book/{book_id}", response_model = Book, status_code=status.HTTP_200_OK)
async def get_book(book_id: int):
    query = 'http://localhost:8983/solr/books_schema/query?q=id:' + str(book_id) + '&q.op=OR&indent=true&qt='
    book= requests.get(query).json()['response']['docs'][0]
    
    return book

@app.get("/author/{author_name}", response_model = Author, status_code=status.HTTP_200_OK)
async def get_author(author_name: str):
    query = 'http://localhost:8983/solr/books_schema/select?defType=edismax&indent=true&q.op=OR&q=' + author_name + '&qf=author'
    list_books= requests.get(query).json()['response']['docs']
    books=[]
    for book in list_books:
        books.append(Book(**book))

    if author_name != "Naomi King":
        print(author_name)
        author = author_name.split(' ')
        writer = author[0]+'_'+author[1]
        query= "https://dbpedia.org/page/" + writer
        abstract = ""
        image = ""
        birth= ""
        genre=""
        response = requests.get(query)
        soup=BeautifulSoup(response.content, 'html.parser')
        image = soup.find('a', {'rel': 'dbo:thumbnail'})
        if image is not None:
            image= image['resource']
        else:
            image = "" 
        language= soup.find_all('span', {'property': 'dbo:abstract', 'lang':'en'})
        if language is not None:
            for tag in language:
                abstract += tag.text.strip()
        birthPlace = soup.find_all('span', {'property': 'dbp:birthPlace', 'lang':'en'})
        if birthPlace is not None:
            for tag in birthPlace:
                birth += tag.text.strip()
        genres = soup.find_all('span', {'property': 'dbp:genre', 'lang':'en'})
        if genres is not None:
            for tag in genres:
                genre += tag.text.strip()

    author = Author(name=author_name, birth=birth, genres=genre, books=books, image=image, abstract=abstract)
    return author

# Search for filters
@app.post("/filter-search", status_code=status.HTTP_200_OK)
async def filter_search(filter: Filter):
    query = ""
    terms =""

    if filter.author:
        if '"' in filter.author:
            query += "author:" + filter.author + ' '
        else:
            query += "author:" +'"'+filter.author+'" '
        terms += "author "
    
    if filter.book_format:
        query += "book_format:"+filter.book_format+' '
        terms += "book_format "
    
    if filter.genre:
        if '"' in filter.genre:
            query += "genre:" + filter.genre + ' '
        else:
            query += "genre:" +'"'+filter.genre+'" '
        terms += "genre "

    if filter.isbn:
        query += "isbn:" +filter.isbn+' '
        terms += "isbn "

    if filter.page_count:
        query += "page_count:" +str(filter.page_count)+' '
        terms += "page_count "

    if filter.rating:
        query += "rating:" +str(filter.rating)+' '
        terms += "rating "

    if filter.review_count:
        query += "review_count:" +str(filter.review_count)+' '
        terms += "review_count "
    
    if filter.title:
        query += "title:" +filter.title+' '
        terms += "title "

    if filter.price:
        query += "price:" +str(filter.price)+' '
        terms += "price "

    if filter.sensitivity:
        if '"' in filter.sensitivity:
            query += "sensitivity:" + filter.sensitivity + ' '
        else:
            query += "sensitivity:" +'"'+filter.sensitivity+'" '
        terms += "sensitivity "

    if filter.pacing:
        if '"' in filter.pacing:
            query += "pacing:" + filter.pacing + ' '
        else:
            query += "pacing:" +'"'+filter.pacing+'" '
        terms += "pacing "

    if filter.buzzwords:
        if '"' in filter.buzzwords:
            query += "buzzwords:" + filter.buzzwords + ' '
        else:
            query += "buzzwords:" +'"'+filter.buzzwords+'" '
        terms += "buzzwords "
    
    if filter.mood:
        if '"' in filter.mood:
            query += "mood:" + filter.mood + ' '
        else:
            query += "mood:" +'"'+filter.mood+'" '
        terms += "mood "

    query_request = "http://localhost:8983/solr/books_schema/select?defType=edismax&indent=true&q.op=AND&q="+query+"&qf="+terms + "&rows=100&start=0"

    list_books= requests.get(query_request).json()['response']['docs']
    books=[]
    for book in list_books:
        books.append(Book(**book))
 
    return books

# Suggestions
@app.get("/suggestions/{query}", status_code=status.HTTP_200_OK) #response_model = List[Suggestions], 
async def get_suggestions(query: str):
    terms = 'http://localhost:8983/solr/books_schema/suggest?indent=true&q.op=OR&q='+query
    list_terms = requests.get(terms).json()['suggest']['mySuggester'][query]['suggestions']
    suggestions = []
    for term in list_terms:
        term_model = Suggestions(term=term['term'])
        suggestions.append(term_model)
    return suggestions

#Search by suggestion
@app.get("/suggestion-search/{query}", status_code=status.HTTP_200_OK)
async def suggestion_search(query: str):
    query_request = "http://localhost:8983/solr/books_schema/select?defType=edismax&indent=true&q.op=AND&q="+query+"&qf=title"+ "&rows=100&start=0"
    list_books= requests.get(query_request).json()['response']['docs']
    books=[]
    for book in list_books:
        books.append(Book(**book))
    return books

# Search for similar books (maybe send the book characteristics + book list of similar books?)
@app.get("/similar/{book_id}", status_code=status.HTTP_200_OK)
async def get_similar(book_id: int):
    query = 'http://localhost:8983/solr/books_schema/query?q=id:' + str(book_id) + '&q.op=OR&indent=true&qt='
    book= requests.get(query).json()['response']['docs'][0] # Get the book
    
    genre=''
    sensitivity=''

    # Get book's genre
    if 'genre' in book:
        genre = "(" + book['genre'][0]
        for g in book['genre'][1:]:
            genre += " OR " + g
        genre += ")"

    # Get book's sensitivity
    if 'sensitivity' in book:
        sensitivity = "(" + book['sensitivity'][0]
        for s in book['sensitivity'][1:]:
            sensitivity += " OR " + s
        sensitivity += ")"


    if genre == "" and sensitivity!="" :
        query = sensitivity 
    elif sensitivity == "" and genre!="" :
        query = genre
    else:
        query = genre + " OR " + sensitivity 

    q = 'http://localhost:8983/solr/books_schema/select?defType=edismax&indent=true&q.op=OR&q=' + query + '&qf=genre%20buzzwords%20sensitivity' + '&rows=100&start=0'
    print(q)

    list_books= requests.get(q).json()['response']['docs']
    books=[]
    for book in list_books:
        if book['id'] != str(book_id):
            books.append(Book(**book))
 
    return books

# Search with a query --> have to search for the query in every term
# Also does spell checking
@app.get("/search/{query}", status_code=status.HTTP_200_OK)
async def search_books(query: str):
    if query.find("&") != -1:
        query = query.replace("&", "%2F")

    print(query)

    query = 'http://localhost:8983/solr/books_schema/select?defType=edismax&indent=true&q.op=OR&q=' + query + '&qf=author%20title%20book_format%20description%20genre%20isbn%20page_count%20rating%20review_count%20rating_count%20price%20sensitivity%20pacing%20buzzwords%20mood%20review&rows=100&start=0'

    print(query)

    list_books= requests.get(query).json()['response']['docs']
    spell = requests.get(query).json()['spellcheck']['collations']
    spell_term=''
    if len(spell) > 0:
        spell_term = spell[1]
    print("spell: ", spell_term)
    books=[]
    for book in list_books:
        book_append = Book(**book)
        book_append.spellcheck = spell_term
        books.append(book_append)
    return books

# Search with a query with weights --> have to search for the query in every term
# Also does spell checking
@app.get("/search-weighted/{query}/{weighted}", status_code=status.HTTP_200_OK)
async def search_books(query: str, weighted: str):
    if query.find("&") != -1:
        query = query.replace("&", "%2F")

    print(query)

    terms= {
        'author',
        'title',
        'book_format',
        'description',
        'genre',
        'isbn',
        'page_count',
        'rating',
        'review_count',
        'rating_count',
        'price',
        'sensitivity',
        'pacing',
        'buzzwords',
        'mood',
        'review'
    }
    list_weighted = weighted.split(",")
    weight = 20/len(list_weighted)

    qf_terms = ""
    for term in terms:
        if term in list_weighted:
            qf_terms += term + "^" + str(weight) + " "
        else:
            qf_terms += term + " "
    query = 'http://localhost:8983/solr/books_schema/select?defType=edismax&indent=true&q.op=OR&q=' + query + '&qf=' + qf_terms + '&rows=100&start=0'

    print(query)

    

   
    list_books= requests.get(query).json()['response']['docs']
    spell = requests.get(query).json()['spellcheck']['collations']
    spell_term=''
    if len(spell) > 0:
        spell_term = spell[1]
    print("spell: ", spell_term)
    books=[]
    for book in list_books:
        book_append = Book(**book)
        book_append.spellcheck = spell_term
        books.append(book_append)
    return books
    

# pip install "fastapi[all]"
# Example of how to run a file: uvicorn main:app --reload