from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models import Book
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

@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books():
    query = 'http://localhost:8983/solr/books_schema/query?q=*:*&q.op=OR&indent=true&wt=json'
    list_books= requests.get(query).json()['response']['docs']
    books=[]
    for book in list_books:
        books.append(Book(**book))
    return books

# pip install "fastapi[all]"
# Example of how to run a file: uvicorn main:app --reload