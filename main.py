from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str

books = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

@app.post("/books")
def create_book(book: Book):
    books.append(book)
    return book

@app.get("/books")
def get_books():
    return books


# Endpoint to update a book by its ID
@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    for b in books:
        if b.id == book_id:
            b.title = book.title
            return b
    raise HTTPException(status_code=404, detail="Book not found")

# Endpoint to delete a book by its ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for b in books:
        if b.id == book_id:
            books.remove(b)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")
    