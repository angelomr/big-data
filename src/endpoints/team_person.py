from src.restplus import api
from flask_restplus import Resource
from src.serializers.team_person import team_person_serializer
from src.business.team_person import TeamPersonBus

ns_team_person = api.namespace('team_person', description='Operations related to Team Person')

@ns_team_person.route('/')
class TeamPersonCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(TeamPersonCollection, self).__init__(api, args, kwargs)
        self.bus = TeamPersonBus()

    @api.marshal_list_with(team_person_serializer)
    def get(self):
        return self.bus.get_all()

    @api.expect(team_person_serializer)
    @api.marshal_with(team_person_serializer, code=201)
    def post(self):
        return self.bus.add(api.payload['name'], api.payload['description'])
    

@ns_team_person.route('/<int:id>')
@api.response(404, 'Person not found.')
class TeamPersonItem(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(TeamPersonItem, self).__init__(api, args, kwargs)
        self.bus = TeamPersonBus()

    @api.marshal_with(team_person_serializer)
    def get(self, id):
        return self.bus.get_by_id(id)

    @api.marshal_with(team_person_serializer)
    def delete(self, id):
        return self.bus.delete(id)

    @api.expect(team_person_serializer)
    @api.marshal_with(team_person_serializer, code=201)
    def put(self, id):
        return self.bus.update(id, api.payload['name'], api.payload['description'])
