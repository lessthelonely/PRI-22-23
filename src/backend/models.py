from pydantic import BaseModel
from typing import Optional, List

class Book(BaseModel):
    id: Optional[int]
    author: List[str]
    book_format: str
    description: str
    genre: List[str]
    cover_img: str
    isbn: str
    link: str
    page_count: int
    rating: float 
    review_count: int
    title: str
    price: Optional[float]
    sensitivity: Optional[List[str]]
    pacing: str
    buzzwords: Optional[List[str]]
    mood: Optional[List[str]]
    review: Optional[List[str]]
    spellcheck: Optional[str]

    class Config:
        orm_mode = True

# make another model and use it with book stuff + quote about author

class Suggestions(BaseModel):
    term: str

class Filter(BaseModel):
    author: Optional[str]
    book_format: Optional[str]
    description: Optional[str]
    genre: Optional[str]
    isbn: Optional[str]
    page_count: Optional[int]
    rating:Optional[float] 
    review_count: Optional[int]
    title: Optional[str]
    price: Optional[float]
    sensitivity: Optional[str]
    pacing: Optional[str]
    buzzwords: Optional[str]
    mood: Optional[str]

    class Config:
        orm_mode = True