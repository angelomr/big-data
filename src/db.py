from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def config_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    db.init_app(app)
    db.create_all(app=app)
