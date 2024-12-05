import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Тестирование получения списка книг
def test_get_books_empty():
    response = client.get("/api/books/")
    assert response.status_code == 200
    assert response.json() == []

# Тестирование создания новой книги
def test_create_book():
    book_data = {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "description": "Dystopian novel."
    }
    response = client.post("/api/books/", json=book_data)
    assert response.status_code == 200
    assert response.json() == book_data

# Тестирование получения книги по ID
def test_get_book():
    response = client.get("/api/books/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "1984",
        "author": "George Orwell",
        "description": "Dystopian novel."
    }

# Тестирование получения несуществующей книги
def test_get_nonexistent_book():
    response = client.get("/api/books/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}
