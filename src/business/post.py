
from src.models.post import Post
from src.db import db

ITEM_NOT_FOUND = 'Post not Found'

class PostBus(object):

    def add(self, title, preview, text):
        post = Post(title=title, preview=preview, text=text)
        db.session.add(post)
        db.session.commit()
        return post

    def get_all(self):
        return Post.query.all()

    def get_by_id(self, id):
        post = Post.query.get(id)
        if post:
            return post
        return {'message': ITEM_NOT_FOUND}, 404 

    def update(self, id, title, preview, text):
        post = Post.query.get(id)
        if post:
            post.title = title
            post.preview = preview
            post.text = text
            db.session.add(post)
            db.session.commit()
            return post
        return {'message': ITEM_NOT_FOUND}, 404
    
    def delete(self, id):
        post = Post.query.get(id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404
