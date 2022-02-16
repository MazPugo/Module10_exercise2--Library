# app/models.py
from datetime import datetime
from app import db

   
class Book_title(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   book_title = db.Column(db.String(100), index=True, unique=True)
   author = db.Column(db.String(200), index=True, unique=True)
   posts = db.relationship("Post", backref="author", lazy="dynamic")

   def __str__(self):
     return f"<User {self.book_title}>"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    book_id = db.Column(db.Integer, db.ForeignKey('book_title.id'))

    def __str__(self):
        return f"<Post {self.id} {self.body[:50]} ...>"