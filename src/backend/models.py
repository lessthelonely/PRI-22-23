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

    class Config:
        orm_mode = True