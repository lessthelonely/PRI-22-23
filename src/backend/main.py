from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import Book, Suggestions, Filter
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
    query = 'http://localhost:8983/solr/books_schema/query?q=*:*&q.op=OR&indent=true&wt=json'
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
    abstracts=[]

    author = book['author']
    author = author[0].split(' ')
    writer = author[0]+'_'+author[1]
    query= "https://dbpedia.org/page/" + writer
    abstract = ""

    response = requests.get(query)
    soup=BeautifulSoup(response.content, 'html.parser')
    language= soup.find_all('span', {'property': 'dbo:abstract', 'lang':'en'})
    for tag in language:
        abstract += tag.text.strip()
        if(abstract != ""):
            book['abstract'] = abstract
    
    return book

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

    query_request = "http://localhost:8983/solr/books_schema/select?defType=edismax&indent=true&q.op=AND&q="+query+"&qf="+terms

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

# Search for similar books (maybe send the book characteristics + book list of similar books?)
@app.get("/similar/{book_id}", status_code=status.HTTP_200_OK)
async def get_similar(book_id: int):
    query = 'http://localhost:8983/solr/books_schema/query?q=id:' + str(book_id) + '&q.op=OR&indent=true&qt='
    book= requests.get(query).json()['response']['docs'][0] # Get the book
    
    # Get book's genre
    genre = "(" + book['genre'][0]
    for g in book['genre'][1:]:
        genre += " OR " + g
    genre += ")"

    # Get book's sensitivity
    sensitivity = "(" + book['sensitivity'][0]
    for s in book['sensitivity'][1:]:
        sensitivity += " OR " + s
    sensitivity += ")"

    # Get book's buzzwords
    buzzwords = "(" + book['buzzwords'][0]
    for b in book['buzzwords'][1:]:
        buzzwords += " OR " + b
    buzzwords += ")"

    if genre == "" and (sensitivity!="" or buzzwords!=""):
        query = sensitivity + " OR " + buzzwords
    elif sensitivity == "" and (genre!="" or buzzwords!=""):
        query = genre + " OR " + buzzwords
    elif buzzwords == "" and (genre!="" or sensitivity!=""):
        query = genre + " OR " + sensitivity
    elif (genre == "" and sensitivity == "") and buzzwords!="":
        query = buzzwords
    elif (genre == "" and buzzwords == "") and sensitivity!="":
        query = sensitivity
    elif (sensitivity == "" and buzzwords == "") and genre!="":
        query = genre
    else:
        query = genre + " OR " + sensitivity + " OR " + buzzwords

    q = 'http://localhost:8983/solr/books_schema/select?defType=edismax&indent=true&q.op=AND&q=' + query + '&qf=genre%20buzzwords%20sensitivity'

    list_books= requests.get(q).json()['response']['docs']
    books=[]
    for book in list_books:
        if book['id'] != str(book_id):
            books.append(Book(**book))
 
    return books

# Entity oriented search


# Search with a query --> have to search for the query in every term
# Also does spell checking
@app.get("/search/{query}", status_code=status.HTTP_200_OK)
async def search_books(query: str):
    query = 'http://localhost:8983/solr/books_schema/select?defType=edismax&indent=true&q.op=OR&q=' + query + '&qf=author%20title%20book_format%20description%20genre%20isbn%20page_count%20rating%20review_count%20rating_count%20price%20sensitivity%20pacing%20buzzwords%20mood%20review'

   
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