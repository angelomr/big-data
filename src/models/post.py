from src.db import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    preview = db.Column(db.String(255), nullable=False)
    text = db.Column(db.Text(), nullable=False)
