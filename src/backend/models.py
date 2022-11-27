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
    price: float
    sensitivity: List[str]
    pacing: str
    buzzwords: List[str]
    mood: List[str]
    review: List[str]

    class Config:
        orm_mode = True