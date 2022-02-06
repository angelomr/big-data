from src.restplus import api
from flask_restplus import Resource
from src.serializers.post import post_serializer
from src.business.post import PostBus

ns_post = api.namespace('post', description='Operations related to blog post')

@ns_post.route('/')
class PostCollection(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(PostCollection, self).__init__(api, args, kwargs)
        self.bus = PostBus()

    @api.marshal_list_with(post_serializer)
    def get(self):
        return self.bus.get_all()

    @api.expect(post_serializer)
    @api.marshal_with(post_serializer, code=201)
    def post(self):
        return self.bus.add(api.payload['title'], api.payload['preview'], api.payload['text'])

@ns_post.route('/<int:id>')
@api.response(404, 'Post not found.')
class PostItem(Resource):

    def __init__(self, api=None, *args, **kwargs):
        super(PostItem, self).__init__(api, args, kwargs)
        self.bus = PostBus()

    @api.marshal_with(post_serializer)
    def get(self, id):
        return self.bus.get_by_id(id)

    @api.marshal_with(post_serializer)
    def delete(self, id):
        return self.bus.delete(id)

    @api.expect(post_serializer)
    @api.marshal_with(post_serializer, code=201)
    def put(self, id):
        return self.bus.update(id, api.payload['title'], api.payload['preview'], api.payload['text'])
