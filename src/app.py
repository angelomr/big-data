from flask import Flask, Blueprint
from src.restplus import api
from src.endpoints.service import ns_service
from src.endpoints.post import ns_post
from src.endpoints.team_person import ns_team_person
from src.db import config_db
from src.log import log

app = Flask(__name__)

def initialize_app(app):
    app.config['RESTPLUS_VALIDATE'] = True
    app.config['ERROR_404_HELP'] = False

    config_db(app)
    blueprint = Blueprint('api', __name__)
    api.init_app(blueprint)
    app.register_blueprint(blueprint)

    api.add_namespace(ns_service)
    api.add_namespace(ns_post)
    api.add_namespace(ns_team_person)

def main():
    initialize_app(app)
    log.info(
        '>>>>> Starting development server at http://localhost:5000 <<<<<')
    app.run(debug=True)


if __name__ == '__main__':
    main()
