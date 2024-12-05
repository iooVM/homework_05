from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Модель книги
class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str

# Временное хранилище для книг
books_db = []

# Получение списка книг
@router.get("/books/", response_model=List[Book])
async def get_books():
    return books_db

# Получение книги по ID
@router.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# Создание новой книги
@router.post("/books/", response_model=Book)
async def create_book(book: Book):
    books_db.append(book)
    return book
