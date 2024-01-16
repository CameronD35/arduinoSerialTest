from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Temp(db.Model):

    __tablename__ = "temps"

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.String, nullable=False)

def connect_db(app):
    db.app = app
    db.init_app(app)