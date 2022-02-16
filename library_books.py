#library.py
from app import app, db
from app.models import Book_title, Post

@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Book_title": Book_title,
        "Post": Post
    }