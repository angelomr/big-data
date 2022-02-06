from src.restplus import api
from flask_restplus import Resource
from src.serializers.service import service_serializer
from src.business.service import ServiceBus

ns_service = api.namespace('service', description='Operations related to service')

@ns_service.route('/')
class ServiceCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(ServiceCollection, self).__init__(api, args, kwargs)
        self.bus = ServiceBus()

    @api.marshal_list_with(service_serializer)
    def get(self):
        return self.bus.get_all()

    @api.expect(service_serializer)
    @api.marshal_with(service_serializer, code=201)
    def post(self):
        return self.bus.add(api.payload['title'], api.payload['preview'], api.payload['text'])

@ns_service.route('/<int:id>')
@api.response(404, 'Service not found.')
class ServiceItem(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(ServiceItem, self).__init__(api, args, kwargs)
        self.bus = ServiceBus()

    @api.marshal_with(service_serializer)
    def get(self, id):
        return self.bus.get_by_id(id)

    @api.marshal_with(service_serializer)
    def delete(self, id):
        return self.bus.delete(id)

    @api.expect(service_serializer)
    @api.marshal_with(service_serializer, code=201)
    def put(self, id):
        return self.bus.update(id, api.payload['title'], api.payload['preview'], api.payload['text'])
