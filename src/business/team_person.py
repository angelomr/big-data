
from src.models.team_person import TeamPerson
from src.db import db

ITEM_NOT_FOUND = 'Book not Found'

class TeamPersonBus(object):

    def add(self, name, description):
        team_person = TeamPerson(name=name, description=description)
        db.session.add(team_person)
        db.session.commit()
        return team_person

    def get_all(self):
        return TeamPerson.query.all()

    def get_by_id(self, id):
        team_person = TeamPerson.query.get(id)
        if team_person:
            return team_person
        return {'message': ITEM_NOT_FOUND}, 404 

    def update(self, id, name, description):
        team_person = TeamPerson.query.get(id)
        if team_person:
            team_person.name = name
            team_person.description = description
            db.session.add(team_person)
            db.session.commit()
            return team_person
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        team_person = TeamPerson.query.get(id)
        if team_person:
            db.session.delete(team_person)
            db.session.commit()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404
