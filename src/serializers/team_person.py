from typing import Text
from src.restplus import api
from flask_restplus import fields

team_person_serializer = api.model('TeamPerson', {
    'id': fields.Integer(readonly=True),
    'name': fields.String(required=True, description='The Team Person name'),
    'description': fields.String(required=True, description='The Team Person description')
})
