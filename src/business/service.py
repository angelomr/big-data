
from src.models.service import Service
from src.db import db

ITEM_NOT_FOUND = 'Service not Found'

class ServiceBus(object):

    def add(self, title, preview, text):
        service = Service(title=title, preview=preview, text=text)
        db.session.add(service)
        db.session.commit()
        return service

    def get_all(self):
        return Service.query.all()

    def get_by_id(self, id):
        service = Service.query.get(id)
        if service:
            return service
        return {'message': ITEM_NOT_FOUND}, 404 

    def update(self, id, title, preview, text):
        service = Service.query.get(id)
        if service:
            service.title = title
            service.preview = preview
            service.text = text
            db.session.add(service)
            db.session.commit()
            return service
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        service = Service.query.get(id)
        if service:
            db.session.delete(service)
            db.session.commit()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404
