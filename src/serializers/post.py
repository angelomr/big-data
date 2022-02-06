from typing import Text
from src.restplus import api
from flask_restplus import fields

post_serializer = api.model('Post', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True, description='The Blog Post title'),
    'preview': fields.String(required=True, description='The Blog Post preview'),
    'text': fields.String(required=True, description='The Blog Post text')
})
