from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import Book, Suggestions
import requests

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
    
    return book

# Search for filters


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

# Spellcheck

# Search for similar books (maybe send the book characteristics + book list of similar books?)

# Entity oriented search

# Search with a query --> have to search for the query in every term
@app.get("/search/{query}", response_model = List[Book], status_code=status.HTTP_200_OK)
async def search_books(query: str):
    query = 'http://localhost:8983/solr/books_schema/query?q=' + query+ '&q.op=OR&defType=edismax&indent=true&qf=author%20title%20book_format%20description%20genre%20isbn%20page_count%20rating%20review_count%20rating_count%20price%20sensitivity%20pacing%20buzzwords%20mood%20review&qt='
    print(requests.get(query).json())
    list_books= requests.get(query).json()['response']['docs']
    spell = requests.get(query).json()['spellcheck']['collations']
    spell_term=''
    if len(spell) > 0:
        spell_term = spell[1]
    books=[]
    for book in list_books:
        book_append = Book(**book)
        book_append.spellcheck = spell_term
        books.append(book_append)
    return books

# pip install "fastapi[all]"
# Example of how to run a file: uvicorn main:app --reload