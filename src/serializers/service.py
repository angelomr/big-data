from typing import Text
from src.restplus import api
from flask_restplus import fields

service_serializer = api.model('Service', {
    'id': fields.Integer(readonly=True),
    'title': fields.String(required=True, description='The Service title'),
    'preview': fields.String(required=True, description='The Service preview'),
    'text': fields.String(required=True, description='The Service text')
})
